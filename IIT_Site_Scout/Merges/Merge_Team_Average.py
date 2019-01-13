import pandas as pd
import os
import re

team_average = pd.read_csv('/home/chenjie/Desktop/ScarletHawksAnalysis/IIT_Site_Scout/1.9 Package/Missing/team_average_results.csv')
print(list(team_average))

formats = pd.read_csv('/home/chenjie/Desktop/ScarletHawksAnalysis/IIT_Site_Scout/CSVs/format.csv')

category = pd.read_csv('/home/chenjie/Desktop/ScarletHawksAnalysis/IIT_Site_Scout/CSVs/Category.csv')

element = pd.read_csv('/home/chenjie/Desktop/ScarletHawksAnalysis/IIT_Site_Scout/CSVs/Element.csv')

team = pd.read_csv('/home/chenjie/Desktop/ScarletHawksAnalysis/IIT_Site_Scout/CSVs/Team.csv')

ta_and_f = pd.merge(team_average,formats,on=['Format_Name'])

ta = ta_and_f.drop(['Format_Name'],axis=1)

ta_and_e = pd.merge(ta,category,on=['Category_Name'])

ta = ta_and_e.drop(['Category_Name'],axis=1)

ta_and_e = pd.merge(ta,element,on=['Element_Name'])

ta = ta_and_e.drop(['Element_Name'],axis=1)

ta_and_t = pd.merge(ta,team,on=['Team_Name'])

ta = ta_and_t.drop(['Team_Name'],axis=1)


print(ta.head())

ta.to_csv('ta.csv',index=False)
