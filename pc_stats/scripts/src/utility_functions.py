from datetime import datetime
from typing import TextIO, Tuple

import pandas as pd
import requests
import json
from pandas import DataFrame

club_details = {
    'Ley_Hill_CC':{
        'site_id': '3931',
        'team_ids': ['54824','119465','216373','232724']
    }
}

current_year = datetime.now().year
today = datetime.today().date().strftime("%d/%m/%Y")

def save_json(data, filename):

    with open(filename, "w") as f:
        json.dumps(data, file=f, indent=4)

class PlayCricketAPI:

    def __init__(self,api_key):
        self.api_key = api_key
        self.base_url = 'http://play-cricket.com/api/v2/'

    def fetch_data(self, endpoint:str, params:dict=None, base_url:str=None)->json:

        if params is None:
            params = {}

        if base_url is None:
            base_url = self.base_url

        params['api_token'] = self.api_key

        url = f"{base_url}{endpoint}"

        response = requests.get(url, params=params)

        if response.status_code != 200:
            print(f"Error fetching {url}: {response.status_code}")
            return None
        else:
            return response.json()

    def get_match_ids(self, site_id:str, team_ids:list=None, start_date:str = '01/01/1900', end_date:str = today, season:int = current_year)->list:
        """Returns results list df and grounds list df for a single season"""

        start_date = datetime.strptime(str(start_date), '%d/%m/%Y').strftime('%d/%m/%Y')
        end_date = datetime.strptime(str(end_date), '%d/%m/%Y').strftime('%d/%m/%Y')

        print(f"Fetching data for {site_id} from {season} season, that has been updated between {start_date} - {end_date}")

        results_params = {
            'site_id': site_id,
            'from_entry_date': start_date,
            'end_entry_date': end_date,
            'season': season
        }

        full_results = self.fetch_data('matches', results_params)

        season_match_id_list = []

        try:

            for match in full_results['matches']:
                if team_ids is None or match['home_team_id'] in team_ids or match['away_team_id'] in team_ids:
                    season_match_id_list.append(str(match['id']))

        except TypeError:

            print(f"No results for {season}")
            return [],[]

        if len(season_match_id_list) == 0:

            output = f"No results retrieved for {season}"
            return [],[]

        else:

            output = f"{len(season_match_id_list)} New or updated results retrieved"

        print(output)

        return season_match_id_list

    def get_match_details(self, match_id:str)->json:

        match_params = {'match_id': match_id,
                        'api_token': self.api_key}

        json_match = self.fetch_data('match_detail', match_params)

        return json_match

    def get_club_name(self, site_id:str)->str:

        site_name = None
        target_season = current_year + 1
        match_index = 0

        while site_name is None:

            match_summary = self.fetch_data('matches', params={'season':target_season ,'site_id':site_id })

            try:
                if match_summary['matches'][match_index]['season'] == str(target_season):

                    if match_summary['matches'][match_index]['home_club_id'] == str(site_id):

                        site_name = match_summary['matches'][match_index]['home_club_name']

                    elif match_summary['matches'][match_index]['away_club_id'] == str(site_id):

                        site_name = match_summary['matches'][match_index]['away_club_name']

                else:
                    target_season -= 1

            except IndexError:
                target_season -= 1

        return site_name

class Club:

    def __init__(self, site_id:str, team_ids:list=None):

        if team_ids is None:
            team_ids = []
        self.site_id = site_id
        self.team_list = team_ids
        self.first_pc_season = 0
        self.latest_pc_season = 0
        self.last_updated_date = '01/01/1900'
        self.match_details = pd.DataFrame()
        self.player_details = pd.DataFrame()
        # self.club_name = pc_api.get_club_name(self.site_id)

    def __str__(self) -> str:
        return f"{self.site_id}: {self.club_name}"

    def find_new_pc_results(self, start_season:int=1900, end_season:int=current_year):

        # Set variables used to break loop
        target_season = end_season
        stop = False

        # Track back through seasons, pulling all match details
        while stop is False and target_season >= start_season:

            season_results = pc_api.get_match_ids(self.site_id, self.team_list, season=target_season)

            if len(season_results) > 0:

                for match in season_results:

                    new_match_details, new_player_details = self.process_match_details_df(match)

                    try:

                        if match in self.match_details['match_id']:

                            # Remove any existing records from the same match_id
                            self.match_details = self.match_details.drop([self.match_details['match_id'] == new_match_details['match_id']].index)
                            self.player_details = self.player_details.drop([self.player_details['match_id'] == new_player_details['match_id']].index)

                    except KeyError:
                        pass

                    # Add new match to dfs
                    self.match_details = pd.concat([self.match_details, new_match_details], ignore_index=True)
                    self.player_details = pd.concat([self.player_details, new_player_details], ignore_index=True)

                target_season -= 1

            else:
                print(f"No results found for {target_season}")
                stop = True

    def process_match(self, match_id:str)->Tuple[DataFrame, DataFrame]:

        json_match = pc_api.get_match_details(match_id)

        match_info_df = pd.DataFrame()
        player_info_df = pd.DataFrame()

        root = json_match['match_details'][0]

        # Not all matches have recorded innings
        try:
            first_innings = root['innings'][0]
            second_innings = root['innings'][1]
            innings_recorded = 1
            print(f"Got innings data")
        except IndexError:
            print("innings IndexError")
            innings_recorded = 0
            first_innings = None
            second_innings = None

        ha_flag = 'home'
        opp_flag = 'away'
        if json_match['match_details'][0]['home_club_id'] != self.site_id:
            ha_flag = 'home'
            opp_flag = 'away'

        try:
            home_players = [root['players'][0][f"{ha_flag}_team"]][0]
            away_players = [root['players'][1][f"{opp_flag}_team"]][0]

            if len(home_players) > 0:
                players_recorded = 1
                if ha_flag == 'home':
                    team_players = home_players
                    opp_players = away_players
                else:
                    team_players = away_players
                    opp_players = home_players
            else:
                players_recorded = 0
                team_players = None
                opp_players = None
        except KeyError:
            players_recorded = 0
            team_players = None
            opp_players = None

        club_name = root[f"{ha_flag}_club_name"]
        team_id = root[f"{ha_flag}_team_id"]
        team_name = root[f"{ha_flag}_team_name"]
        opposition_club_id = root[f"{opp_flag}_club_id"]
        opposition_team_id = root[f"{opp_flag}_team_id"]
        opposition_club_name = root[f"{opp_flag}_club_name"]
        opposition_team_name = root[f"{opp_flag}_team_name"]

        # Find out if subject team won the toss
        if json_match['match_details'][0]['toss_won_by_team_id'] == opposition_team_id:
            won_toss = 0
        else:
            won_toss = 1

        print(f"Own team id:{team_id}")
        print(f"Opp team id:{opposition_team_id}")
        print(f"Won toss:{won_toss}")

        # Find out if subject team batted first
        if json_match['match_details'][0]['batted_first'] == opposition_team_id:
            batted_first = 0
        else:
            batted_first = 1

        # Find out the result of the game
        result = str([root['result_description']])

        if result.find(club_name) >= 0 and result.find("Won") >= 0:
            result_short = "Won"
            if first_innings is not None and batted_first == 1:
                gap = int(first_innings['runs']) - int(second_innings['runs'])
                result_detail = f"by {gap} runs"
            elif first_innings is not None:
                gap = 10 - int(second_innings['wickets'])
                result_detail = f"by {gap} wickets"
            else:
                result_detail = None

        elif result.find(opposition_club_name) >= 0 and result.find("Won") >= 0:
            result_short = "Lost"
            if first_innings is not None and batted_first == 0:
                gap = int(second_innings['runs']) - int(first_innings['runs'])
                result_detail = f"by {gap} runs"
            elif first_innings is not None:
                gap = 10 - int(second_innings['wickets'])
                result_detail = f"by {gap} wickets"
            else:
                result_detail = None

        elif result.find(opposition_club_name) and result.find("Conceded") > 0:
            result_short = "Won"
            result_detail = "Conceded"
        elif result.find(club_name) and result.find("Conceded") > 0:
            result_short = "Lost"
            result_detail = "Conceded"
        else:
            result_short = result
            result_detail = None

        match_info_df['season'] = []
        match_info_df['match_id'] = [root['id']]
        match_info_df['team_id'] = team_id
        match_info_df['opposition_club_id'] = opposition_club_id
        match_info_df['opposition_team_id'] = opposition_team_id
        match_info_df['match_date'] = [root['match_date']]
        match_info_df['league_name'] = root.get('league_name',None)
        match_info_df['competition_name'] = root.get('competition_name', None)
        match_info_df['competition_type'] = root.get('competition_type', None)
        match_info_df['location'] = ha_flag.title()
        match_info_df['team_name'] = team_name
        match_info_df['opposition_club_name'] = opposition_club_name
        match_info_df['opposition_team_name'] = opposition_team_name
        match_info_df['won_toss'] = won_toss
        match_info_df['batted_first'] = batted_first
        match_info_df['result'] = result_short
        match_info_df['result_detail'] = result_detail

        player_info_df['match_id'] = [root['id']]

        if team_players is not None:
            player_list_df = pd.DataFrame(team_players)
            player_list_df['match_id'] = root['id']


        if first_innings is not None:
            print(f"Getting batting and bowling data")
            if batted_first == 1:
                batting_info_df = pd.DataFrame(first_innings['bat'])
                bowling_info_df = pd.DataFrame(second_innings['bowl'])
                print(bowling_info_df)
            else:
                batting_info_df = pd.DataFrame(first_innings['bowl'])
                bowling_info_df = pd.DataFrame(second_innings['bat'])
                print(bowling_info_df)

            if not batting_info_df.empty:

                batting_info_df = batting_info_df.drop(['position', 'batsman_id', 'bowler_id', 'fielder_id', 'position'],
                                                   axis=1)
                batting_info_df = batting_info_df.rename(
                    columns={'bowler_name': 'opposition_bowler_name', 'runs': 'runs_scored'})

                bowling_info_df = bowling_info_df.drop(['bowler_id'], axis=1)
                bowling_info_df = bowling_info_df.rename(columns={'runs': 'runs_conceded'})

            if team_players is not None:

                player_info_df = pd.merge(player_list_df, batting_info_df, left_on='player_name', right_on='batsman_name',
                                          how='left')
                player_info_df = pd.merge(player_info_df, bowling_info_df, left_on='player_name', right_on='bowler_name',
                                          how='left')

                player_info_df = player_info_df.drop(['batsman_name', 'bowler_name'], axis=1)

        # match_info_df.to_csv(f"{match_id}_match_info.csv", index=False)
        # player_info_df.to_csv(f"{match_id}_player_info.csv", index=False)

        return match_info_df, player_info_df

    def process_match_json(self,json_match:json)->DataFrame:

        # Create empty df to hold match info
        match_info_df: DataFrame = pd.DataFrame()

        # Define root of json
        root: tuple = json_match['match_details'][0]

        # Find out if subject team were playing at home or away
        if root['home_club_id'] == self.site_id:
            ha_flag = 'home'
            opp_flag = 'away'
        elif root['away_club_id'] == self.site_id:
            ha_flag = 'away'
            opp_flag = 'home'
        else:
            print(f"{self.site_id} not found")

        # Use the ha_flag to find team_id
        team_id = root[f"{ha_flag}_team_id"]

        # Use the team_id to determine whether they won the toss
        if root['toss_won_by_team_id'] == team_id:
            won_toss = 1
        else:
            won_toss = 0

        # Use the team_id to determine whether they batted first
        if root['batted_first'] == team_id:
            batted_first = 1
            batting_innings_index = 0
            bowling_innings_index = 1
        else:
            batted_first = 0
            batting_innings_index = 1
            bowling_innings_index = 0

        try:
            batting_data = root['innings'][batting_innings_index]['bat']
            batting_details_flag = 1
            # extract_batting_info(batting_data)
        except KeyError:
            batting_details_flag = 0
            print(f"No batting data available in innings {bowling_innings_index+1}")

        try:
            bowling_data = root['innings'][bowling_innings_index]['bowl']
            bowling_details_flag = 1
            # extract_bowling_info(bowling_data)
        except KeyError:
            print(f"No bowling data available in innings {bowling_innings_index+1}")
            bowling_details_flag = 0

        match_info_df.loc[0, 'season'] = str(datetime.strptime(root['match_date'], "%d/%m/%Y").year)
        match_info_df['match_date'] = root['match_date']
        match_info_df['location'] = ha_flag.title()
        match_info_df['team_id'] = team_id
        match_info_df['team_name'] = root[f"{ha_flag}_team_name"]
        match_info_df['opp_club_name'] = root[f"{opp_flag}_club_name"]
        match_info_df['opp_team_id'] = root[f"{opp_flag}_team_id"]
        match_info_df['opp_team_name'] = root[f"{opp_flag}_team_name"]
        match_info_df['won_toss'] = won_toss
        match_info_df['batted_first'] = batted_first





        # Find out the result of the game
        result = str([root['result_description']])

        if result.find(club_name) >= 0 and result.find("Won") >= 0:
            result_short = "Won"
            if first_innings is not None and batted_first == 1:
                gap = int(first_innings['runs']) - int(second_innings['runs'])
                result_detail = f"by {gap} runs"
            elif first_innings is not None:
                gap = 10 - int(second_innings['wickets'])
                result_detail = f"by {gap} wickets"
            else:
                result_detail = None

        elif result.find(opposition_club_name) >= 0 and result.find("Won") >= 0:
            result_short = "Lost"
            if first_innings is not None and batted_first == 0:
                gap = int(second_innings['runs']) - int(first_innings['runs'])
                result_detail = f"by {gap} runs"
            elif first_innings is not None:
                gap = 10 - int(second_innings['wickets'])
                result_detail = f"by {gap} wickets"
            else:
                result_detail = None

        elif result.find(opposition_club_name) and result.find("Conceded") > 0:
            result_short = "Won"
            result_detail = "Conceded"
        elif result.find(club_name) and result.find("Conceded") > 0:
            result_short = "Lost"
            result_detail = "Conceded"
        else:
            result_short = result
            result_detail = None

        return match_info_df

    # def get_next_fixtures(self):
    #
    #     new_fars_df = pc_api.get_match_ids(self.site_id, self.team_list, start_date=self.last_updated_date,
    #                                                        season=current_year)
    #
    #     new_fixtures = new_fars_df[new_fars_df['match_date'] > datetime.now()]
    #
    #     self.last_updated_date = datetime.now()
    #
    #     if len(new_results) == 0:
    #         print("No new resutls found")
    #         new_results = None
    #
    #     if len(new_fixtures) == 0:
    #         print("No new fixtures found")
    #         new_fixtures = None
    #
    #     return new_results, new_fixtures

pc_api = PlayCricketAPI("7068b85d44186c4d96eef29a6c3da106")
#
# lhcc = club_details['Ley_Hill_CC']
# lhcc = Club(lhcc['site_id'],lhcc['team_ids'])
#
# lhcc.update_pc_results(2024,2024)
#
# lhcc.player_details.to_csv(f"lhcc_data.csv", index=False)