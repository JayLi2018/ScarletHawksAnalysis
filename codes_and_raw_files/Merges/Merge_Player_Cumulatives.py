import pandas as pd
import os
import re

os.chdir('/home/chenjie/Desktop/ScarletHawksAnalysis/codes_and_raw_files/Updates/2.21 package/Player_Cumulative/')

Player_Cumulative = pd.read_csv('player_cumulatives.csv')

player = pd.read_csv('/home/chenjie/Desktop/ScarletHawksAnalysis/codes_and_raw_files/CSVs/player.csv')

p_t = pd.merge(Player_Cumulative,player,on=['Player_Name'])

result = p_t.drop(['Player_Name','Team_Name'],axis=1)

print(result.head())

result.to_csv('Player_Cumulative.csv',index=False)
