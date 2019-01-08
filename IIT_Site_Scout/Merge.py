import pandas as pd
import os
import re

player_game = pd.read_csv('/home/chenjie/Desktop/ScarletHawksAnalysis/IIT_Site_Scout/CSVs/GAME_CSVs/1.4/player_games.csv')

lineups = pd.read_csv('/home/chenjie/Desktop/ScarletHawksAnalysis/IIT_Site_Scout/CSVs/GAME_CSVs/1.4/lineups.csv')

tracter = pd.read_csv('/home/chenjie/Desktop/ScarletHawksAnalysis/IIT_Site_Scout/CSVs/GAME_CSVs/1.4/game_trackers.csv')

team = pd.read_csv('/home/chenjie/Desktop/ScarletHawksAnalysis/IIT_Site_Scout/CSVs/Team.csv')

player = pd.read_csv('/home/chenjie/Desktop/ScarletHawksAnalysis/IIT_Site_Scout/CSVs/player.csv')


pg_p = pd.merge(player_game,player,on='Player_Name')

l_t = pd.merge(lineups,team,on='Team_Name')

pg_p.to_csv('Player_Game.csv')
l_t.to_csv('Lineup.csv')