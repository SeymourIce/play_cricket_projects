import pandas as pd
from pathlib import Path
import sys

def aggregate_data(csv_path, season=None):

    df = pd.read_csv(csv_path)

    if season:
        df = df[df['season'] == int(season)]

    batting_df = df[df['how_out'] != 'did not bat'].copy()
    batting_stats = batting_df.groupby('player_name').agg({        
        'runs_scored': 'sum',
        'balls_faced': 'sum',
        'fours': 'sum',
        'sixes': 'sum',
        'batting_position': 'count'
    }).reset_index()

    not_outs = batting_df.groupby('player_name')['how_out'].apply(
        lambda x: (x.isin(['not out', 'retired not out'])).sum()
    ).reset_index(name='not_outs')

    batting_stats = batting_stats.merge(not_outs, on='player_name', how='left')
    batting_stats['dismissals'] = batting_stats['batting_position'] - batting_stats['not_outs']
    batting_stats['average'] = batting_stats.apply(
        lambda row: row['runs_scored'] / row['dismissals'] if row['dismissals'] > 0 else (row['runs_scored'] if row['runs_scored'] > 0 else 0),
        axis=1
    )
    batting_stats['strike_rate'] = batting_stats.apply(
        lambda row: (row['runs_scored'] / row['balls_faced']) * 100 if row['balls_faced'] > 0 else 0,
        axis=1
    )
    batting_stats['boundary_%'] = batting_stats.apply(
        lambda row: ((row['fours'] * 4 + row['sixes'] * 6 ) / row['runs_scored']) * 100 if (row['fours']+row['sixes']) > 0 else 0,
        axis=1
    )

    batting_stats = batting_stats.sort_values('average', ascending=False)

    bowling_df = df[df['overs'] > 0].copy()
    bowling_stats = bowling_df.groupby('player_name').agg({
        'overs': 'sum',
        'maidens': 'sum',
        'runs_conceded': 'sum',
        'wickets': 'sum',
        'wides': 'sum',
        'no_balls': 'sum'
    }).reset_index()

    bowling_stats['average'] = bowling_stats.apply(
        lambda row: row['runs_conceded'] / row['wickets'] if row['wickets'] > 0 else 0,
        axis=1
    )
    bowling_stats['economy'] = bowling_stats.apply(
        lambda row: row['runs_conceded'] / row['overs'] if row['overs'] > 0 else 0,
        axis=1
    )

    bowling_stats = bowling_stats.sort_values('average', ascending=True)

    return batting_stats, bowling_stats

def generate_averages_tables(batting_stats, bowling_stats, output_path=None, season=None):

    if output_path is None:
        output_path = Path(__file__).root / 'data' / club_name.lower().replace(' ', '_') / str(season) / 'reports' / f"{club_name.lower().replace(' ', '_')}_{season}_averages_tables.html"
    else:
        output_path = Path(output_path)

    if not season and 'season' in df.columns and not df.empty:
        season = int(df['season'].iloc[0])

    title = f"{csv_path.stem.replace('_', ' ').title()} {season} Season Stats" if season else f"{csv_path.stem.replace('_', ' ').title()} Season Stats"

    html = [
        '<!DOCTYPE html>',
        '<html lang="en">',
        '<head>',
        '    <meta charset="UTF-8">',
        '    <meta name="viewport" content="width=device-width, initial-scale=1.0">',
        f'    <title>{title}</title>',
        '    <style>',
        '        body { font-family: Arial, sans-serif; margin: 20px; }',
        '        table { border-collapse: collapse; width: 100%; margin-bottom: 20px; }',
        '        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }',
        '        th { background-color: #f2f2f2; }',
        '        h2 { color: #333; }',
        '    </style>',
        '</head>',
        '<body>',
        f'    <h1>{title}</h1>',
        '    <h2>Batting Averages</h2>',
        '    <table>',
        '        <tr>',
        '            <th>Player</th>',
        '            <th>Innings</th>',
        '            <th>Runs</th>',
        '            <th>Average</th>',
        '            <th>Strike Rate</th>',
        '            <th>4s</th>',
        '            <th>6s</th>',
        '        </tr>'
    ]

    for _, row in batting_stats.iterrows():
        html.append('        <tr>')
        html.append(f'            <td>{row["player_name"]}</td>')
        html.append(f'            <td>{int(row["batting_position"])}</td>')
        html.append(f'            <td>{int(row["runs_scored"])}</td>')
        html.append(f'            <td>{row["average"]:.2f}</td>')
        html.append(f'            <td>{row["strike_rate"]:.2f}</td>')
        html.append(f'            <td>{int(row["fours"])}</td>')
        html.append(f'            <td>{int(row["sixes"])}</td>')
        html.append('        </tr>')

    html.extend([
        '    </table>',
        '    <h2>Bowling Averages</h2>',
        '    <table>',
        '        <tr>',
        '            <th>Player</th>',
        '            <th>Overs</th>',
        '            <th>Wickets</th>',
        '            <th>Average</th>',
        '            <th>Economy</th>',
        '            <th>Runs</th>',
        '            <th>Maidens</th>',
        '        </tr>'
    ])

    for _, row in bowling_stats.iterrows():
        html.append('        <tr>')
        html.append(f'            <td>{row["player_name"]}</td>')
        html.append(f'            <td>{row["overs"]:.1f}</td>')
        html.append(f'            <td>{int(row["wickets"])}</td>')
        html.append(f'            <td>{row["average"]:.2f}</td>')
        html.append(f'            <td>{row["economy"]:.2f}</td>')
        html.append(f'            <td>{int(row["runs_conceded"])}</td>')
        html.append(f'            <td>{int(row["maidens"])}</td>')
        html.append('        </tr>')

    html.extend([
        '    </table>',
        '</body>',
        '</html>'
    ])

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text('\n'.join(html), encoding='utf-8')

    print(f"Generated averages tables at {output_path}")
    
    return output_path

def generate_leaderboards(batting_stats_df, bowling_stats_df):

    top_runscorers = batting_stats_df.sort_values('runs_scored', ascending=False).head(10)
    most_sixes = batting_stats_df.sort_values('sixes', ascending=False).head(10)

    top_wicket_takers = bowling_stats_df.sort_values('wickets', ascending=False).head(10)

    return top_runscorers, top_wicket_takers

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python generate_tables.py <csv_path> <season> [output_html]')
        sys.exit(1)

    csv_path = sys.argv[1]
    season = sys.argv[2] 
    output_html = sys.argv[3] if len(sys.argv) > 3 else None

    batting_stats, bowling_stats = aggregate_data(csv_path, season)

    averages_output_path = generate_averages_tables(batting_stats, bowling_stats, output_html, season)
    
