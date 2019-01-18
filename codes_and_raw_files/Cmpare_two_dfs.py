import pandas as pd
import os

os.chdir('/home/chenjie/Desktop/ScarletHawksAnalysis/IIT_Site_Scout/CSVs/')

# pg = pd.read_csv('Player_Game_Names.csv')
pgame = pd.read_csv('Player_Games.csv')
# p = pd.read_csv('Players.csv')


# df = pd.concat([pg,p])
# df = df.reset_index(drop=True)

# df_gpby = df.groupby(list(df.columns))

# idx = [x[0] for x in df_gpby.groups.values() if len(x)==1]

# df.reindex(idx)
# print(df.reindex(idx))

# gp_pg = pg.groupby(['Player_Name']).sum()
# print(gp_pg)
# gp_pg.to_csv('sum_names.csv')

gp_pgame = pgame.groupby(['Game_ID','Lineup_ID']).sum()

gp_pgame.to_csv('find_missing_player.csv')