import pandas as pd

# Load the data
df = pd.read_csv('../data/ley_hill_cc/2026/player_data/ley_hill_cc_2026_player_data.csv')

# Filter for 2026 season
df = df[df['season'] == 2026]

# Batting stats
batting_df = df[df['position'] == 'Batter'].copy()
batting_stats = batting_df.groupby('player_name').agg({
    'runs_scored': 'sum',
    'balls_faced': 'sum',
    'fours': 'sum',
    'sixes': 'sum',
    'batting_position': 'count'  # innings
}).reset_index()

# Count not outs
not_out_conditions = batting_df['how_out'].isin(['not out', 'retired not out'])
not_outs = batting_df.groupby('player_name')['how_out'].apply(lambda x: (x.isin(['not out', 'retired not out'])).sum()).reset_index(name='not_outs')

batting_stats = batting_stats.merge(not_outs, on='player_name', how='left')
batting_stats['dismissals'] = batting_stats['batting_position'] - batting_stats['not_outs']
batting_stats['average'] = batting_stats.apply(lambda row: row['runs_scored'] / row['dismissals'] if row['dismissals'] > 0 else (row['runs_scored'] if row['runs_scored'] > 0 else 0), axis=1)
batting_stats['strike_rate'] = batting_stats.apply(lambda row: (row['runs_scored'] / row['balls_faced']) * 100 if row['balls_faced'] > 0 else 0, axis=1)

# Sort by average descending
batting_stats = batting_stats.sort_values('average', ascending=False)

# Bowling stats
bowling_df = df[df['position'] == 'Bowler'].copy()
bowling_stats = bowling_df.groupby('player_name').agg({
    'overs': 'sum',
    'maidens': 'sum',
    'runs_conceded': 'sum',
    'wickets': 'sum',
    'wides': 'sum',
    'no_balls': 'sum'
}).reset_index()

bowling_stats['average'] = bowling_stats.apply(lambda row: row['runs_conceded'] / row['wickets'] if row['wickets'] > 0 else 0, axis=1)
bowling_stats['economy'] = bowling_stats.apply(lambda row: row['runs_conceded'] / row['overs'] if row['overs'] > 0 else 0, axis=1)

# Sort by average ascending (lower is better)
bowling_stats = bowling_stats.sort_values('average', ascending=True)

# Generate HTML
html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ley Hill CC 2026 Season Stats</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        table { border-collapse: collapse; width: 100%; margin-bottom: 20px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        h2 { color: #333; }
    </style>
</head>
<body>
    <h1>Ley Hill CC 2026 Season Statistics</h1>

    <h2>Batting Averages</h2>
    <table>
        <tr>
            <th>Player</th>
            <th>Innings</th>
            <th>Runs</th>
            <th>Average</th>
            <th>Strike Rate</th>
            <th>4s</th>
            <th>6s</th>
        </tr>
"""

for _, row in batting_stats.iterrows():
    html += f"""
        <tr>
            <td>{row['player_name']}</td>
            <td>{int(row['batting_position'])}</td>
            <td>{int(row['runs_scored'])}</td>
            <td>{row['average']:.2f}</td>
            <td>{row['strike_rate']:.2f}</td>
            <td>{int(row['fours'])}</td>
            <td>{int(row['sixes'])}</td>
        </tr>
"""

html += """
    </table>

    <h2>Bowling Averages</h2>
    <table>
        <tr>
            <th>Player</th>
            <th>Overs</th>
            <th>Wickets</th>
            <th>Average</th>
            <th>Economy</th>
            <th>Runs</th>
            <th>Maidens</th>
        </tr>
"""

for _, row in bowling_stats.iterrows():
    html += f"""
        <tr>
            <td>{row['player_name']}</td>
            <td>{row['overs']:.1f}</td>
            <td>{int(row['wickets'])}</td>
            <td>{row['average']:.2f}</td>
            <td>{row['economy']:.2f}</td>
            <td>{int(row['runs_conceded'])}</td>
            <td>{int(row['maidens'])}</td>
        </tr>
"""

html += """
    </table>
</body>
</html>
"""

# Write to file
with open('../tables.html', 'w') as f:
    f.write(html)

print("Tables generated in tables.html")