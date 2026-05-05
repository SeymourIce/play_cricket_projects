import json
import sys
from datetime import datetime
from pathlib import Path

import pytest

# Ensure scripts directory is importable when running tests from the project root
script_dir = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(script_dir))

import pull_season_player_data as ps


def test_get_team_ids_from_response_filters_by_site_and_team_name():
    teams_response = {
        'teams': [
            {'id': 1, 'site_id': 3931, 'team_name': '1st XI', 'other_team_name': '', 'nickname': ''},
            {'id': 2, 'site_id': 3931, 'team_name': '2nd XI', 'other_team_name': '', 'nickname': ''},
            {'id': 3, 'site_id': 9999, 'team_name': '1st XI', 'other_team_name': '', 'nickname': ''},
            {'id': 4, 'site_id': 3931, 'team_name': 'Other', 'other_team_name': 'Sunday 1st XI', 'nickname': ''},
        ]
    }

    result = ps.get_team_ids_from_response(teams_response, ['1st XI', 'Sunday 1st XI'], '3931')

    assert result == ['1', '4']


def test_format_match_label_uses_club_team_name_and_opponent_club_name():
    match = {
        'id': 123,
        'home_club_id': 3931,
        'home_team_name': '1st XI',
        'away_club_name': 'Opponent CC',
        'away_team_name': '2nd XI',
    }

    label = ps.format_match_label(match, '3931')

    assert label == 'Processing match 123 (1st XI vs Opponent CC 2nd XI)...'


def test_extract_player_data_applies_requested_season():
    match_summary = {
        'id': 1,
        'home_club_id': 3931,
        'home_team_name': '1st XI',
        'away_club_name': 'Opponent CC',
        'away_team_name': '2nd XI',
        'home_team_id': 11,
        'away_team_id': 22,
        'match_date': '2025-05-01',
    }
    match_detail_response = {
        'match_details': [
            {
                'innings': [
                    {
                        'team_batting_id': 11,
                        'bat': [
                            {'batsman_name': 'Alice', 'runs': '42', 'balls': '50', 'fours': '5', 'sixes': '1', 'how_out': 'caught', 'position': '1'},
                        ],
                    },
                    {
                        'team_batting_id': 22,
                        'bowl': [
                            {'bowler_name': 'Alice', 'overs': '8.0', 'maidens': '1', 'runs': '24', 'wickets': '2', 'wides': '0', 'no_balls': '0'},
                        ],
                    },
                ]
            }
        ]
    }

    rows = ps.extract_player_data(match_detail_response, match_summary, 3931, 2025)

    assert rows
    assert all(row['season'] == 2025 for row in rows)
    assert rows[0]['team_name'] == '1st XI'
    assert rows[0]['opposition_team_name'] == '2nd XI'


def test_save_and_load_last_run_date_per_season_and_team(tmp_path, monkeypatch):
    metadata_file = tmp_path / 'ley_hill_cc_metadata.json'

    def fake_get_metadata_file(club_name):
        return metadata_file

    monkeypatch.setattr(ps, 'get_metadata_file', fake_get_metadata_file)

    ps.save_last_run_date('Ley Hill CC', 2025, ['1st XI', '2nd XI'])
    file_content = metadata_file.read_text()
    data = json.loads(file_content)

    assert 'teams' in data
    assert '1st XI' in data['teams']
    assert '2025' in data['teams']['1st XI']

    loaded = ps.load_last_run_date('Ley Hill CC', 2025, '1st XI')
    assert isinstance(loaded, datetime)
    assert loaded == datetime.fromisoformat(data['teams']['1st XI']['2025'])

    # If no team_name passed, should return the earliest timestamp among teams
    loaded_all = ps.load_last_run_date('Ley Hill CC', 2025)
    assert loaded_all == loaded
