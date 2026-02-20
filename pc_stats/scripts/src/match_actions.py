import pandas as pd
import numpy as np
from pc_stats.config import *
from pandas import DataFrame
from typing import List
from playcric.playcricket import pc
import requests
from datetime import datetime
import os

results_root = f"{project_root}/data/results"

def get_new_matches(season):

    season_folder = f"{results_root}/new_matches/{season}"

    new_matches_list = []

    # Loop through each year folder
    for file in season_folder.iterdir():
        if file.is_file():
            print(f" Reading file: {file.name}")
            new_matches_df = pd.read_csv(file)

            new_matches_list.append(new_matches_df)

    all_new_matches_list = pd.concat(new_matches_list, ignore_index=True)

    return all_new_matches_list

def get_new_match_details():

    new_results_root = f"{results_root}/new_matches"

    for season_folder in new_results_root.iterdir():
        df = get_new_matches(season_folder)

         # TODO: Check for previous matches and only replace if the last_updated dates are not the same

        for row in df.itertuples():
            match_id = row.id
            match_lud = row.lud

            match = Match(match_id)

            match.process_match()

class Match:

    def __init__(self, match_id: int, subject_site_id: int = None):
        self.match_id = match_id
        self.site_id = subject_site_id

    def fetch_match_details(self):

        # Define the API endpoint and parameters
        url = "http://play-cricket.com/api/v2/match_detail.json?"
        params = {
            "match_id": self.match_id,
            "api_token": api_key  # Replace with your actual API token
        }

        # Make the GET request
        response = requests.get(url, params=params)

        # Check the response
        if response.status_code != 200:
            print(f"Request failed with status code {response.status_code}")
        else:
            match_json = response.json()
            match_details = pd.json_normalize(match_json['match_details'][0])

            match_detail_headers = [
                'id',
                'last_updated'

            ]




    # def build_bowling_data(self, bowling: DataFrame, batting: DataFrame) -> DataFrame:
    #
    #     bowling_headers = ['match_id', 'innings', 'bowler_id', 'bowler_name', 'overs', 'maidens', 'runs', 'wickets',
    #                        'wides', 'no_balls', 'innings']
    #
    #     own_bowling_df = bowling[bowling['team_id'].isin(self.team_ids)]
    #     bowling_main_df = own_bowling_df[bowling_headers]
    #
    #     bowling_details_raw = batting[batting['opposition_id'].isin(self.team_ids)]
    #
    #     bowling_details_raw['opposition_batsman_position'] = bowling_details_raw['position'].apply(categorise_batsman)
    #
    #     bowling_details_raw_subset = bowling_details_raw[['match_id', 'bowler_id', 'how_out', 'position']]
    #
    #
    #     wicket_method = bowling_details_raw_subset.pivot_table(index=['bowler_id', 'match_id'], columns='how_out',
    #                                                            aggfunc='size', fill_value=0).reset_index()
    #     batsman_dismissed = bowling_details_raw_subset.pivot_table(index=['bowler_id', 'match_id'], columns='position',
    #                                                                aggfunc='size', fill_value=0).reset_index()
    #
    #     bowling_details_df = pd.merge(wicket_method, batsman_dismissed, on=['bowler_id', 'match_id'], how='left')
    #
    #     full_bowling_df = pd.merge(bowling_main_df, bowling_details_df, on=['bowler_id', 'match_id'], how='left')
    #
    #     full_bowling_df = full_bowling_df.rename(columns={'bowler_id': 'player_id'})
    #
    #     full_bowling_df = full_bowling_df.rename(columns={'ct': 'caught', 'b': 'bowled', 'std': 'stumped'})
    #
    #     return full_bowling_df
    #
    # def build_batting_data(self, batting: DataFrame) -> DataFrame:
    #
    #     batting_headers = ['match_id', 'innings', 'batsman_id', 'batsman_name', 'position', 'how_out', 'runs', 'fours',
    #                        'sixes', 'balls', 'not_out']
    #
    #     own_batting_df = batting[batting['team_id'].isin(self.team_ids)]
    #     batting_main_df = own_batting_df[batting_headers]
    #
    #     batting_main_df = batting_main_df.rename(columns={'batsman_id': 'player_id'})
    #
    #     return batting_main_df
    #
    # def build_fielding_data(self, batting: DataFrame) -> DataFrame:
    #
    #     fielding_headers = ['match_id', 'fielder_id', 'how_out']
    #
    #     fielding_details_raw = batting[batting['opposition_id'].isin(self.team_ids)]
    #
    #     fielding_details_raw_subset = fielding_details_raw[fielding_headers]
    #
    #     fielding_pivot = fielding_details_raw_subset.pivot_table(index=['fielder_id', 'match_id'], columns='how_out',
    #                                                            aggfunc='size', fill_value=0).reset_index()
    #
    #     fielding_pivot = fielding_pivot.rename(columns={'fielder_id': 'player_id'})
    #
    #     full_fielding_df = fielding_pivot.rename(columns={'ct': 'catches_taken', 'std': 'stumpings', 'runs_out': 'run_outs'})
    #
    #     return full_fielding_df
    #
    # def create_match_player_output(self, match_ids: list) -> DataFrame:
    #
    #     pc_api: object = pc(api_key=api_key, site_id=self.site_id)
    #
    #     batting, bowling, fielding = pc_api.get_individual_stats_from_all_games([match_ids])
    #
    #     full_batting_df = self.build_batting_data(batting)
    #     full_fielding_df = self.build_fielding_data(batting)
    #     full_bowling_df = self.build_bowling_data(bowling, batting)
    #
    #     full_match_output = pd.merge(full_batting_df, full_fielding_df, on=['player_id', 'match_id'], how='left')
    #
    #     full_match_output = pd.merge(full_match_output, full_bowling_df, on=['player_id', 'match_id'], how='left')
    #
    #     return full_match_output



