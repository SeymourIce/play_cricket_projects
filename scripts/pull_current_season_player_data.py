import pandas as pd
import requests
import json
from datetime import datetime
from config import api_key, cricket_club_dict

class PlayCricketAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'http://play-cricket.com/api/v2/'

    def fetch_data(self, endpoint, params=None):
        if params is None:
            params = {}
        params['api_token'] = self.api_key
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print(f"Error fetching {url}: {response.status_code}")
            return None
        return response.json()

    def get_results(self, site_id, team_ids=None, season=2026):
        """Returns all match results for a season"""
        results_params = {
            'site_id': site_id,
            'season': season
        }
        full_results = self.fetch_data('result_summary.json', results_params)
        season_results = []

        if full_results and 'result_summary' in full_results:
            for match in full_results['result_summary']:
                if team_ids is None or match.get('home_team_id') in team_ids or match.get('away_team_id') in team_ids:
                    season_results.append(match)

        return season_results

    def get_match_detail(self, match_id):
        """Returns detailed match information including player stats"""
        match_params = {'match_id': match_id}
        return self.fetch_data('match_detail.json', match_params)

def extract_player_data(match_detail_response, match_summary, club_id):
    """Extract player data from match detail JSON"""
    players_data = []

    if not match_detail_response or 'match_details' not in match_detail_response:
        return players_data

    match_detail = match_detail_response['match_details'][0]

    def safe_int(val, default=0):
        """Safely convert value to int, handling empty strings"""
        if val == '' or val is None:
            return default
        try:
            return int(val)
        except (ValueError, TypeError):
            return default

    def safe_float(val, default=0):
        """Safely convert value to float, handling empty strings"""
        if val == '' or val is None:
            return default
        try:
            return float(val)
        except (ValueError, TypeError):
            return default

    try:
        # Determine if club is home or away
        if match_summary.get('home_club_id') == club_id:
            ha_flag = 'home'
            opp_flag = 'away'
            team_id = match_summary.get('home_team_id')
        elif match_summary.get('away_club_id') == club_id:
            ha_flag = 'away'
            opp_flag = 'home'
            team_id = match_summary.get('away_team_id')
        else:
            return players_data

        # Process innings data
        innings_list = match_detail.get('innings', [])
        
        for inning in innings_list:
            if inning.get('team_batting_id') == team_id:
                # Get batting data
                if 'bat' in inning:
                    for bat_record in inning.get('bat', []):
                        player_data = {
                            'match_id': match_summary.get('id'),
                            'season': 2026,
                            'match_date': match_summary.get('match_date'),
                            'team_name': match_summary.get(f"{ha_flag}_team_name"),
                            'opposition_team_name': match_summary.get(f"{opp_flag}_team_name"),
                            'player_name': bat_record.get('batsman_name', ''),
                            'player_id': '',
                            'position': 'Batter',
                            'runs_scored': safe_int(bat_record.get('runs', 0)),
                            'balls_faced': safe_int(bat_record.get('balls', 0)),
                            'fours': safe_int(bat_record.get('fours', 0)),
                            'sixes': safe_int(bat_record.get('sixes', 0)),
                            'how_out': bat_record.get('how_out', ''),
                            'batting_position': bat_record.get('position', ''),
                            'overs': 0,
                            'maidens': 0,
                            'runs_conceded': 0,
                            'wickets': 0,
                            'wides': 0,
                            'no_balls': 0
                        }
                        players_data.append(player_data)
                
                # Get bowling data
                if 'bowl' in inning:
                    for bowl_record in inning.get('bowl', []):
                        # Find if this bowler already exists in players_data
                        bowler_name = bowl_record.get('bowler_name', '')
                        existing_player = None
                        for p in players_data:
                            if p['player_name'] == bowler_name:
                                existing_player = p
                                break
                        
                        if existing_player:
                            # Update existing player with bowling data
                            existing_player.update({
                                'overs': safe_float(bowl_record.get('overs', 0)),
                                'maidens': safe_int(bowl_record.get('maidens', 0)),
                                'runs_conceded': safe_int(bowl_record.get('runs', 0)),
                                'wickets': safe_int(bowl_record.get('wickets', 0)),
                                'wides': safe_int(bowl_record.get('wides', 0)),
                                'no_balls': safe_int(bowl_record.get('no_balls', 0))
                            })
                        else:
                            # Create new player entry for bowler
                            player_data = {
                                'match_id': match_summary.get('id'),
                                'season': 2026,
                                'match_date': match_summary.get('match_date'),
                                'team_name': match_summary.get(f"{ha_flag}_team_name"),
                                'opposition_team_name': match_summary.get(f"{opp_flag}_team_name"),
                                'player_name': bowler_name,
                                'player_id': '',
                                'position': 'Bowler',
                                'runs_scored': 0,
                                'balls_faced': 0,
                                'fours': 0,
                                'sixes': 0,
                                'how_out': '',
                                'batting_position': '',
                                'overs': safe_float(bowl_record.get('overs', 0)),
                                'maidens': safe_int(bowl_record.get('maidens', 0)),
                                'runs_conceded': safe_int(bowl_record.get('runs', 0)),
                                'wickets': safe_int(bowl_record.get('wickets', 0)),
                                'wides': safe_int(bowl_record.get('wides', 0)),
                                'no_balls': safe_int(bowl_record.get('no_balls', 0))
                            }
                            players_data.append(player_data)
    except (KeyError, ValueError, TypeError) as e:
        print(f"Error extracting player data: {e}")

    return players_data

# Main execution
current_season = datetime.now().year
club_id = '3931'
club_info = cricket_club_dict[club_id]
club_name = club_info['club_name']

# Team IDs mapping (you may need to update these)
# Fetch team IDs from API based on team names in cricket_club_dict
team_names = club_info.get('team_names', [])
team_ids = []

if team_names:
    teams_response = api.fetch_data('teams.json', {'site_id': club_id})
    if teams_response and 'teams' in teams_response:
        for team in teams_response['teams']:
            if team.get('name') in team_names:
                team_ids.append(str(team.get('team_id')))
    print(f"Found team IDs: {team_ids}")
else:
    print("No team names found in cricket_club_dict")
    team_ids = None

# Initialize API
api = PlayCricketAPI(api_key)

print(f"Fetching player data for {club_name} - {current_season} season...")

# Get match results for current season
match_results = api.get_results(club_id, team_ids, current_season)
print(f"Found {len(match_results)} matches for {current_season}")

all_players_data = []

# Process each match result
for match in match_results:
    print(f"Processing match {match.get('id')} ({match.get('home_team_name')} vs {match.get('away_team_name')})...")
    match_detail = api.get_match_detail(match.get('id'))
    if match_detail:
        players_data = extract_player_data(match_detail, match, club_id)
        all_players_data.extend(players_data)

# Create DataFrame
if all_players_data:
    df = pd.DataFrame(all_players_data)

    # Save to CSV
    output_file = f"{club_name.lower().replace(' ', '_')}_{current_season}_player_data.csv"
    df.to_csv(output_file, index=False)
    print(f"Player data saved to {output_file}")
    print(f"Total player records: {len(df)}")

    # Basic analysis
    print("\nSample of player data:")
    print(df.head())

    if 'player_name' in df.columns:
        player_match_counts = df['player_name'].value_counts()
        print(f"\nTop 10 players by appearances in {current_season}:")
        print(player_match_counts.head(10))

        # Summary stats
        if 'runs_scored' in df.columns:
            total_runs = df.groupby('player_name')['runs_scored'].sum().sort_values(ascending=False)
            print(f"\nTop 10 run scorers in {current_season}:")
            print(total_runs.head(10))

        if 'wickets' in df.columns:
            total_wickets = df.groupby('player_name')['wickets'].sum().sort_values(ascending=False)
            print(f"\nTop 10 wicket takers in {current_season}:")
            print(total_wickets.head(10))

else:
    print("No player data found for the current season.")