import sys
from datetime import datetime
from pathlib import Path
from pull_season_player_data import pull_player_data, get_csv_output_path, cricket_club_dict
from generate_tables import generate_tables


def run_data_pipeline(club_id, season=None):
    """Run the full data pipeline for a club and season."""
    csv_path = pull_player_data(club_id, season)

    if csv_path is None:
        club_info = cricket_club_dict[club_id]
        club_name = club_info['club_name']
        if season is None:
            season = datetime.now().year
        csv_path = get_csv_output_path(club_name, season)
        if not csv_path.exists():
            print(f"No existing CSV found at {csv_path}; nothing to generate.")
            return None

    output_path = Path(__file__).parent.parent / 'tables.html'
    output_path = generate_tables(csv_path, output_path, season)
    print(f"Data pipeline completed. Generated tables at {output_path}")
    return output_path


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python run_data_pipeline.py <club_id> [season]')
        sys.exit(1)

    club_id = sys.argv[1]
    season = int(sys.argv[2]) if len(sys.argv) > 2 else None
    run_data_pipeline(club_id, season)
