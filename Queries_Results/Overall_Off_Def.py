import pandas as pd 

raw = pd.read_csv("/home/chenjie/Desktop/ScarletHawksAnalysis/Queries_Results/Overall_Off_Def.csv")

df = pd.DataFrame(columns=['Team','Offensive','Defensive'])

df['Team'] = raw['team_name']


# df.loc[df['column_name'] == some_value]