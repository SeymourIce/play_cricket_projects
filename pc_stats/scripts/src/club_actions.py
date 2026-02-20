import pandas as pd
import numpy as np
from pc_stats.config import *
from Tools.scripts.nm2def import export_list
from pandas import DataFrame
from typing import List
from playcric.playcricket import pc
import requests
import csv
from datetime import datetime
import os

from pc_stats.scripts.src.match_actions import Match

now = datetime.today()
today = datetime.today().strftime('%Y-%m-%d')
current_year = datetime.now().year

# def save_new_matches(matches_df):


def categorise_batsman(position) -> str:

    if position <= 3:
        return 'top order'
    elif position <= 7:
        return 'middle order'
    else:
        return 'tail'


class Club:

    def __init__(self, site_id: int, club_name: str = None, selected_team_names: list = [], start_season: int = None, end_season: int = current_year, last_updated_date: str = None):

        self.site_id: int = site_id
        self.club_name: str = self.get_club_name(club_name)
        self.root_folder = f"{project_root}/club_directory/{self.club_name}/"
        self.matches_output_folder = f"{project_root}/data/results/"

        print(f"Getting teams")

        self.teams_df: DataFrame = self.get_teams_df(selected_team_names)
        self.team_ids: list[int] = self.teams_df['id'].to_list()
        self.team_names: list[int] = self.teams_df['team_name'].to_list()
        self.start_season: int = start_season
        self.end_season: int = end_season

    def get_club_name(self, club_name) -> str:

        print(f"Initialising {club_name}")

        if club_name is None:

            clubs_url = f"https://www.play-cricket.com/api/v2/clubs.json?&api_token={api_key}"

            response = requests.get(clubs_url)

            if response.status_code != 200:
                print(f"Error fetching {clubs_url}: {response.status_code}")
                return None

            clubs_df = pd.DataFrame(response.json()['clubs'])

            clubs_df = clubs_df[clubs_df['id'] == self.site_id]

            club_name = str(clubs_df['name'].iloc[0])

        return club_name

    def get_last_updated_date(self, season: int) -> DataFrame:

        print(f"Checking activity log")

        try: # to pull max date from activity log

            df = pd.read_csv(f'{self.root_folder}activity_log.csv', sep=',')

            df = df[df['season'] == season]

            df['scan_date'] = pd.to_datetime(df['scan_date'], format='%Y-%m-%d')

            lud_df = df.groupby('team_id')['scan_date'].max().reset_index()

        except FileNotFoundError:
            lud_df = None

        return lud_df

    def get_teams_df(self, team_names) -> DataFrame:

        teams_url = f"https://www.play-cricket.com/api/v2/sites/{self.site_id}/teams?api_token={api_key}"

        response = requests.get(teams_url)

        if response.status_code != 200:
            print(f"Error fetching {teams_url}: {response.status_code}")
            return None

        teams_df = pd.DataFrame(response.json()['teams'])

        # If team names have been specified, filter the full list down to those names
        if team_names:

        #TODO: Add logic to raise warning when requested team names haven't been found in API data

            teams_df = teams_df[teams_df['team_name'].isin(team_names)]

        return teams_df

    def get_new_matches(self, season: int = None) -> DataFrame:

        if season is None:

            season = self.end_season

        print(f"Getting new {season} matches for {self.team_names}")

        pc_api: object = pc(api_key=api_key, site_id=self.site_id)

        season_matches_df = pc_api.get_all_matches(season=season)

        # Drop unrequired columns
        season_matches_df = season_matches_df.drop(columns=[
        'umpire_1_name',
        'umpire_1_id',
        'umpire_2_name',
        'umpire_2_id',
        'umpire_3_name',
        'umpire_3_id',
        'referee_name',
        'referee_id',
        'scorer_1_name',
        'scorer_1_id',
        'scorer_2_name',
        'scorer_2_id'])

        # Convert the 'last_updated' and match_date columns to datetime
        season_matches_df['last_updated'] = pd.to_datetime(season_matches_df['last_updated'])
        season_matches_df['match_date'] = pd.to_datetime(season_matches_df['match_date'])

        # Only keep matches that have a current or historic match_date
        completed_matches_df = season_matches_df[season_matches_df['match_date'] <= today]

        # Get last updated date for each team
        team_lud_df = self.get_last_updated_date(season)

        try:

            # Merge team_lud_df with matches to compare last updated dates with match_dates
            merged_games = completed_matches_df.merge(
                team_lud_df.rename(columns={'team_id': 'home_team_id', 'scan_date': 'home_scan_date'}),
                on='home_team_id',
                how = 'inner')

            merged_games = merged_games.merge(
                team_lud_df.rename(columns={'team_id': 'away_team_id', 'scan_date': 'away_scan_date'}),
                on='away_team_id',
                how = 'inner')

            new_matches_df = merged_games[
                (merged_games['match_date'] <= merged_games['home_scan_date']) &
                (merged_games['match_date'] <= merged_games['away_scan_date'])
            ]

            # Check for teams that are in the team_id list, but haven't been scanned before
            new_teams_list = list(set(self.team_ids) - set(team_lud_df['team_id']))

            new_team_matches_df = completed_matches_df[
                (completed_matches_df['home_team_id'].isin(new_teams_list)) | (
                    completed_matches_df['away_team_id'].isin(new_teams_list))]

            all_new_matches_df = pd.concat([new_matches_df, new_team_matches_df])

        except AttributeError:
        # When activity log is empty, just filter on current team selections

            all_new_matches_df = completed_matches_df[
                (completed_matches_df['home_team_id'].isin(self.team_ids)) | (
                    completed_matches_df['away_team_id'].isin(self.team_ids))]



        # Reset the index
        all_new_matches_df = all_new_matches_df.sort_values(by='match_date', ascending=False).reset_index(drop=True)

        all_new_matches_df = all_new_matches_df.replace('', np.nan).astype({
            'league_id': 'Int64',
            'competition_id': 'Int64',
            'season': 'int',
            'ground_id': 'Int64',
            'home_team_id': 'int',
            'home_club_id': 'int',
            'away_team_id': 'int',
            'away_club_id': 'int'
        })

        print(f"{len(all_new_matches_df)} new matches found")

        return all_new_matches_df

    def stage_new_matches(self, season, new_matches: DataFrame) -> str:

        output_dir = os.path.join(self.matches_output_folder, f"new_matches/{season}/")

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        filename = f"{today}_{self.club_name}.csv".replace(" ", "_").replace("-", "")

        target_location = os.path.join(output_dir, filename)

        if os.path.isfile(target_location):
            new_matches.to_csv(target_location, mode='a', header=False, index=False)

        else:
            new_matches.to_csv(target_location, index=False)

        # for index, row in df.iterrows():
        #
        #     print(f"Processing match {index + 1}/{len(df)}")
        #
        #     if row['home_club_id'] == self.site_id:
        #         home = True
        #     else:
        #         home = False
        #
        #     match_id = row['id']
        #     match_date = row['match_date'].strftime('%Y%m%d')
        #     if home:
        #         team_name, opposition_club, opposition_team, location = row['home_team_name'], row['away_club_name'], row['away_team_name'], 'H'
        #     else:
        #         team_name, opposition_club, opposition_team, location = row['away_team_name'], row['home_club_name'], row['home_team_name'], 'A'
        #
        #     filename = f"{match_date}_{team_name}_vs_{opposition_club}_{opposition_team}_({location})_{match_id}.csv".replace(" ", "_")
        #
        #     path = os.path.join(output_dir, filename)
        #
        #     row_df = pd.DataFrame([row])
        #
        #     row_df.to_csv(path, index=False)

        return target_location

    def update_activity_log(self, team_name: str, team_id: int, season: int, new_matches: DataFrame) -> bool:

            # Define the file name
            filename = os.path.join(self.root_folder, 'activity_log.csv')

            # Define the headers and the data to append
            headers = ['club_name', 'club_id', 'team_name', 'team_id', 'season', 'scan_date', 'new_matches']
            data = [self.club_name, self.site_id, team_name, team_id, season, today, new_matches]

            # Create the directory if it doesn't exist
            if not os.path.exists(self.root_folder):
                print(f"Creating {self.root_folder}")
                os.makedirs(self.root_folder)

            # Create the file if it doesn't exist and write headers
            if not os.path.isfile(filename):
                with open(filename, 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(headers)

            # Write data to the file
            with open(filename, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                # Write the data row
                writer.writerow(data)

            return True

    def update_new_matches(self, all_seasons: int = 0):

        if all_seasons == 0:
            start_season = self.end_season
        else:
            start_season = self.start_season

        season = self.end_season

        while season >= start_season:

            new_matches_df = self.get_new_matches(season)
            success = self.stage_new_matches(season, new_matches_df)

            if success:

                print(f"{self.club_name} results ready for loading to match archive")

            # Update activity log for each team and season
            for index, team_name in enumerate(self.team_names):

                team_id = self.team_ids[index]

                new_matches = len(new_matches_df[(new_matches_df['home_team_id'] == team_id) | (
                        new_matches_df['away_team_id'] == team_id)])

                print(f"{new_matches} new matches found for {team_name}")

                self.update_activity_log(team_name, team_id, season, new_matches)

            season =- 1