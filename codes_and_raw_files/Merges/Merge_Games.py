import pandas as pd
import os

os.chdir('/home/chenjie/Desktop/ScarletHawksAnalysis/codes_and_raw_files/Updates/2.6 package/')

lineups = pd.read_csv('/home/chenjie/Desktop/ScarletHawksAnalysis/codes_and_raw_files/Updates/2.6 package/lineups.csv')

player_games = pd.read_csv('/home/chenjie/Desktop/ScarletHawksAnalysis/codes_and_raw_files/Updates/2.6 package/player_games.csv')

teams = pd.read_csv('/home/chenjie/Desktop/ScarletHawksAnalysis/codes_and_raw_files/CSVs/Team.csv')

players = pd.read_csv('/home/chenjie/Desktop/ScarletHawksAnalysis/codes_and_raw_files/CSVs/player.csv')

l_and_t = pd.merge(lineups,teams,on=['Team_Name'])

l = l_and_t.drop(['Team_Name'],axis=1)

pg = player_games.drop(['Team_Name'],axis=1)

pg_and_p = pd.merge(pg,players,on=['Player_Name'])

pg = pg_and_p.drop(['Player_Name','Team_ID'],axis=1)

l.to_csv('Lineups.csv',index=False)
pg.to_csv('Player_Games.csv',index=False)