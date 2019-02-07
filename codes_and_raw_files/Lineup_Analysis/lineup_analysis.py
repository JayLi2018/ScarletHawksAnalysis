import pandas as pd

lineups = pd.read_csv('lineups_1_30.csv')

lineups = lineups.drop(['started','game_id','lineup_id','ended','session_number','team_id'],axis=1)

lineups=lineups.groupby(['lineup_players'],as_index=False).sum()

lineups.reset_index()

print(list(lineups))

# lineups = lineups[~lineups['lineup_players'].str.contains('Anthony', na = False)]

# lineups = lineups[~lineups['lineup_players'].str.contains('Capriest', na = False)]

# lineups = lineups[~lineups['lineup_players'].str.contains('Brett', na = False)]

# lineups = lineups[lineups['min']>=3]

# lineups.reset_index(inplace=True,drop=True)

# lineups['scale_factor'] = 40/lineups['min']

# for column in lineups:
# 	if((column == 'lineup_players') or (column=='scale_factor')):
# 		print("continue")
# 		continue
# 	else:
# 		print('else?')
# 		lineups[column] = lineups[column]*lineups['scale_factor']



lineups.to_csv('original_cumulative_lineups.csv')

print(lineups.plusminus)