import pandas as pd
import requests
import json
from datetime import datetime
from pathlib import Path
from config import api_key, cricket_club_dict
import sys

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

def extract_player_data(match_detail_response, match_summary, club_id, season):
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
        
        # Process batting data from the innings where our team batted
        for inning in innings_list:
            if inning.get('team_batting_id') == team_id:
                # Get batting data
                if 'bat' in inning:
                    for bat_record in inning.get('bat', []):
                        player_data = {
                            'match_id': match_summary.get('id'),
                            'season': season,
                            'match_date': match_summary.get('match_date'),
                            'team_name': match_summary.get(f"{ha_flag}_team_name"),
                            'opposition_team_name': match_summary.get(f"{opp_flag}_team_name"),
                            'player_name': bat_record.get('batsman_name', ''),
                            'player_id': '',
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
        
        # Process bowling data from the innings where opposition batted (and our team bowled)
        for inning in innings_list:
            if inning.get('team_batting_id') != team_id and 'bowl' in inning:
                # Get bowling data from the opposing team's innings
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
                            'season': season,
                            'match_date': match_summary.get('match_date'),
                            'team_name': match_summary.get(f"{ha_flag}_team_name"),
                            'opposition_team_name': match_summary.get(f"{opp_flag}_team_name"),
                            'player_name': bowler_name,
                            'player_id': '',
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

def get_metadata_file(club_name):
    """Get the path to the metadata file for storing last run date"""
    return Path(__file__).parent.parent / 'data' / f".{club_name.lower().replace(' ', '_')}_metadata.json"


def write_metadata_file(metadata_file, data):
    """Write metadata file using pretty JSON formatting."""
    with open(metadata_file, 'w') as f:
        json.dump(data, f, indent=2, sort_keys=True)
        f.write('\n')


def load_last_run_date(club_name, season, team_name=None):
    """Load the last run date from metadata file for a specific season and team"""
    metadata_file = get_metadata_file(club_name)
    if metadata_file.exists():
        try:
            with open(metadata_file, 'r') as f:
                data = json.load(f)
                # Check new format with teams/seasons dict
                if 'teams' in data:
                    if team_name and team_name in data['teams']:
                        last_run = data['teams'][team_name].get(str(season))
                        if last_run:
                            return datetime.fromisoformat(last_run)
                    else:
                        # If no specific team, check all teams and return earliest (most conservative)
                        earliest = None
                        for team_data in data['teams'].values():
                            if str(season) in team_data:
                                last_run = team_data[str(season)]
                                dt = datetime.fromisoformat(last_run)
                                if earliest is None or dt < earliest:
                                    earliest = dt
                        if earliest:
                            return earliest
                # Fallback to old format for backward compatibility
                elif 'seasons' in data:
                    last_run = data['seasons'].get(str(season))
                    if last_run:
                        return datetime.fromisoformat(last_run)
                elif season == datetime.now().year:
                    last_run = data.get('last_run_date')
                    if last_run:
                        return datetime.fromisoformat(last_run)
        except (json.JSONDecodeError, ValueError):
            pass
    return None

def save_last_run_date(club_name, season, team_names=None):
    """Save the current run date to metadata file for a specific season and teams"""
    metadata_file = get_metadata_file(club_name)
    metadata_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Load existing data
    existing_data = {}
    if metadata_file.exists():
        try:
            with open(metadata_file, 'r') as f:
                existing_data = json.load(f)
        except (json.JSONDecodeError, ValueError):
            pass
    
    # Ensure teams dict exists
    if 'teams' not in existing_data:
        existing_data['teams'] = {}
    
    # If no teams specified, use a default "all" entry
    if not team_names:
        team_names = ['all']
    
    # Update each team with current season's date
    current_time = datetime.now().isoformat()
    for team_name in team_names:
        if team_name not in existing_data['teams']:
            existing_data['teams'][team_name] = {}
        existing_data['teams'][team_name][str(season)] = current_time
    
    write_metadata_file(metadata_file, existing_data)

def parse_date(date_str):
    """Parse date string from API response"""
    if not date_str:
        return None
    try:
        # Try common date formats
        for fmt in ['%Y-%m-%d %H:%M:%S', '%Y-%m-%dT%H:%M:%S', '%d/%m/%Y', '%Y-%m-%d']:
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue
    except (ValueError, TypeError):
        pass
    return None

def filter_matches_by_date(matches, last_run_date):
    """Filter matches to only include those updated since last run"""
    if not last_run_date:
        return matches
    
    filtered_matches = []
    for match in matches:
        updated_date_str = match.get('updated_date') or match.get('match_date')
        if updated_date_str:
            updated_date = parse_date(updated_date_str)
            if updated_date and updated_date > last_run_date:
                filtered_matches.append(match)
        else:
            # If no date info, include it to be safe
            filtered_matches.append(match)
    
    return filtered_matches

def get_csv_output_path(club_name, current_season):
    """Get the path for the CSV output file"""
    return Path(__file__).parent.parent / 'data' / club_name.lower().replace(' ', '_') / str(current_season) / 'player_data' / f"{club_name.lower().replace(' ', '_')}_{current_season}_player_data.csv"

def load_existing_player_data(csv_path):
    """Load existing player data from CSV"""
    if csv_path.exists():
        return pd.read_csv(csv_path)
    return pd.DataFrame()

def update_player_data(df_existing, df_new):
    """Update existing player data with new data, removing old entries for same matches"""
    if df_existing.empty:
        return df_new
    
    # Get match IDs from new data
    new_match_ids = set(df_new['match_id'].unique())
    
    # Remove old entries for matches that are being updated
    df_updated = df_existing[~df_existing['match_id'].isin(new_match_ids)]
    
    # Combine with new data
    df_combined = pd.concat([df_updated, df_new], ignore_index=True)
    
    return df_combined

def pull_player_data(club_id, season=None):
    """Pull player data for a given club and season, updating incrementally based on last run date."""
    if season is None:
        season = datetime.now().year
    
    club_info = cricket_club_dict[club_id]
    club_name = club_info['club_name']

    # Team IDs mapping
    team_names = club_info.get('team_names', [])
    team_ids = []

    # Load last run date for this season and teams
    last_run_date = load_last_run_date(club_name, season, team_names[0] if team_names else None)
    print(f"Last run date for {season} season ({', '.join(team_names) if team_names else 'all teams'}): {last_run_date if last_run_date else 'Never'}")

    # Initialize API
    api = PlayCricketAPI(api_key)

    if team_names:
        teams_response = api.fetch_data('teams.json', {'site_id': club_id})
        if teams_response and 'teams' in teams_response:
            for team in teams_response['teams']:
                if team.get('site_id') != int(club_id):
                    continue
                candidate_names = {
                    team.get('team_name', ''),
                    team.get('other_team_name', ''),
                    team.get('nickname', ''),
                    team.get('name', '')
                }
                if any(name in team_names for name in candidate_names if name):
                    team_ids.append(str(team.get('id') or team.get('team_id')))
        team_ids = list(dict.fromkeys(team_ids))
        print(f"Found team IDs: {team_ids}")
        if not team_ids:
            print('Warning: no matching team IDs found for configured teams; this will return 0 matches.')
    else:
        print("No team names found in cricket_club_dict")
        team_ids = None

    print(f"Fetching player data for {club_name} - {season} season...")

    # Get match results for the season
    all_match_results = api.get_results(club_id, team_ids, season)
    print(f"Found {len(all_match_results)} total matches for {season}")

    # Filter matches by last run date
    match_results = filter_matches_by_date(all_match_results, last_run_date)
    print(f"Found {len(match_results)} matches to process (updated since last run)")

    all_players_data = []

    # Process each match result
    for match in match_results:
        if str(match.get('home_club_id')) == str(club_id):
            club_team_name = match.get('home_team_name')
            opponent_club_name = match.get('away_club_name')
            opponent_team_name = match.get('away_team_name')
        else:
            club_team_name = match.get('away_team_name')
            opponent_club_name = match.get('home_club_name')
            opponent_team_name = match.get('home_team_name')

        print(f"Processing match {match.get('id')} ({club_team_name} vs {opponent_club_name} {opponent_team_name})...")
        match_detail = api.get_match_detail(match.get('id'))
        if match_detail:
            players_data = extract_player_data(match_detail, match, club_id, season)
            all_players_data.extend(players_data)

    # Create DataFrame and update CSV if there's new data
    if all_players_data:
        df_new = pd.DataFrame(all_players_data)
        
        # Get CSV path and load existing data
        csv_path = get_csv_output_path(club_name, season)
        csv_path.parent.mkdir(parents=True, exist_ok=True)
        
        df_existing = load_existing_player_data(csv_path)
        
        # Combine with existing data
        df = update_player_data(df_existing, df_new)
        
        # Save to CSV
        df.to_csv(csv_path, index=False)
        print(f"Player data saved to {csv_path}")
        print(f"Total player records: {len(df)}")
        
        # Update last run date for this season and all processed teams
        save_last_run_date(club_name, season, team_names if team_names else None)
        print(f"Updated last run date for {season} season ({', '.join(team_names) if team_names else 'all teams'})")

        # Basic analysis
        print("\nSample of player data:")
        print(df.head())

        if 'player_name' in df.columns:
            player_match_counts = df['player_name'].value_counts()
            print(f"\nTop 10 players by appearances in {season}:")
            print(player_match_counts.head(10))

            # Summary stats
            if 'runs_scored' in df.columns:
                total_runs = df.groupby('player_name')['runs_scored'].sum().sort_values(ascending=False)
                print(f"\nTop 10 run scorers in {season}:")
                print(total_runs.head(10))

            if 'wickets' in df.columns:
                total_wickets = df.groupby('player_name')['wickets'].sum().sort_values(ascending=False)
                print(f"\nTop 10 wicket takers in {season}:")
                print(total_wickets.head(10))

        return csv_path  # Return the path to the updated CSV
    else:
        print("No new player data found to process.")
        return None

# Main execution
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pull_season_player_data.py <club_id> [season]")
        sys.exit(1)

    club_id = sys.argv[1]
    season = int(sys.argv[2]) if len(sys.argv) > 2 else None
    pull_player_data(club_id, season)