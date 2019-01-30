import pandas as pd

lineups = pd.read_csv('lineups_1_29.csv')

lineups = lineups.drop(['started','game_id','lineup_id','ended','session_number','team_id'],axis=1)

print(list(lineups))

lineups=lineups.groupby(['lineup_players']).sum()

# lineups['reb_rate'] = lineups['ttlreb']/(lineups['ttlreb']+lineups['oppo_ttlreb'])

lineups.to_csv('cumulative_lineups.csv')

print(lineups)