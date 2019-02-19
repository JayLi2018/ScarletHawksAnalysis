import pandas as pd
import os
import re


os.chdir('/home/chenjie/Desktop/ScarletHawksAnalysis/codes_and_raw_files/Updates/2.17 package/Team_Player_Average/')

player_average = pd.read_csv('/home/chenjie/Desktop/ScarletHawksAnalysis/codes_and_raw_files/Updates/2.17 package/Team_Player_Average/player_average_results.csv')
print(player_average)


df = player_average.groupby(['Player_Name']).size().reset_index(name='counts')

# df = df['Player_Name']

formats = pd.read_csv('/home/chenjie/Desktop/ScarletHawksAnalysis/codes_and_raw_files/CSVs/format.csv')

category = pd.read_csv('/home/chenjie/Desktop/ScarletHawksAnalysis/codes_and_raw_files/CSVs/Category.csv')

element = pd.read_csv('/home/chenjie/Desktop/ScarletHawksAnalysis/codes_and_raw_files/CSVs/Element.csv')

player = pd.read_csv('/home/chenjie/Desktop/ScarletHawksAnalysis/codes_and_raw_files/CSVs/player.csv')

# player = player['Player_Name']

pa_and_f = pd.merge(player_average,formats,on=['Format_Name'])

print(pa_and_f)

pa = pa_and_f.drop(['Format_Name'],axis=1)

pa_and_e = pd.merge(pa,category,on=['Category_Name'])

pa = pa_and_e.drop(['Category_Name'],axis=1)

pa_and_e = pd.merge(pa,element,on=['Element_Name'])

pa = pa_and_e.drop(['Element_Name'],axis=1)


pa_and_p = pd.merge(pa,player,on=['Player_Name'])

pa = pa_and_p.drop(['Player_Name','Team_ID','Team_Name'],axis=1)


print(pa)


pa.to_csv('pa.csv',index=False)

# print(df[~df.isin(player)].dropna())

# dif = pd.concat([df,player]).drop_duplicates(keep=False)
# print(dif)
# print(dif.shape)
