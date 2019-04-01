import psycopg2
import pandas as pd 
from MinHeap import MinHeap


conn = psycopg2.connect(dbname="jaybball",user="lchenjie",host="localhost",port="5432",password='lcj53242')

IIT_Rosters = ['Anthony Mosley', 'Ben Wagner', 'Heath Sheridan', 'Ahmad Muhammad','Jake Bruns', 'Jalen Lomax',
 'Calvin Schmitz', 'Capriest Gardner', 'Brett Ott', 'Jake Digiorgio', 'Max Hisatake',
  'Otis Reale', 'Milos Dugalic', 'Cody Mattson', 'Parker Joncus', 'Guy Ostroff', 'Ricardo Whitehead', 
  'Kohl Linder', 'Zach Parduhn']

test_query = 'SELECT * FROM season_lineups;'

test_df = pd.read_sql(test_query,conn)


class Pair_Rankings:

	def __init__(self,team_name='Illinois Tech Scarlet Hawks',
				rosters=IIT_Rosters,
				connection=conn,
				metric='plusminus'):

		self.team_name = team_name
		self.rosters = rosters
		self.metric = metric
		self.conn = connection


	def generate_2_player_pairs(self,num_of_pairs=5):

		heap_list = []
		for n in self.rosters:
			heap = MinHeap(key='plusminus',data_list=[])
			for m in self.rosters:
				if(m==n):
					continue
				else:
					candidate_pair = [n,m]
					candidate_pair.sort()
					Q = "SELECT '{}' AS chosen_player,'{}' AS pair,SUM(min) AS min, SUM(".format(n,','.join(candidate_pair))+self.metric+") AS "+self.metric+\
					 " FROM season_lineups WHERE lineup_players like '%{}%'".format('%'.join(candidate_pair))
					df = pd.read_sql(Q,self.conn)
					if(df.isnull().values.any()):
						pass
					else:
						df[self.metric] = pd.to_numeric(df[self.metric])
						if(heap.size()<num_of_pairs):
							heap.add(df)
						else:
							if(df[self.metric].loc[0]>=heap.peek()[self.metric].loc[0]):
								heap.pop()
								heap.add(df)
			player_result = heap.get_result()

			print(player_result)
			if(player_result is not None):
				heap_list.append(player_result)

		result_df = pd.concat(heap_list)

		return result_df

	def generate_3_player_pairs(self,num_of_pairs=5):

		heap_list = []
		for n in range(len(self.rosters)):
			heap = MinHeap(key='plusminus',data_list=[])
			for m in range(len(self.rosters)):
				if(m==n):
					continue
				else:
					for p in range(m+1,len(self.rosters)):
						candidate_pair = [self.rosters[n],self.rosters[m],self.rosters[p]]
						candidate_pair.sort()
						Q = "SELECT '{}' AS chosen_player,'{}' AS pair,SUM(min) AS min, SUM(".format(self.rosters[n],','.join(candidate_pair))+self.metric+") AS "+self.metric+\
						 " FROM season_lineups WHERE lineup_players like '%{}%'".format('%'.join(candidate_pair))
						print(Q)
						df = pd.read_sql(Q,self.conn)
						if(df.isnull().values.any()):
							pass
						else:
							df[self.metric] = pd.to_numeric(df[self.metric])
							if(heap.size()<num_of_pairs):
								heap.add(df)
							else:
								if(df[self.metric].loc[0]>=heap.peek()[self.metric].loc[0]):
									heap.pop()
									heap.add(df)

			player_result = heap.get_result()


			print(player_result)
			if(player_result is not None):
				heap_list.append(player_result)

		result_df = pd.concat(heap_list)

		return result_df


if __name__ == "__main__":

	pr = Pair_Rankings(team_name='Illinois Tech Scarlet Hawks',rosters=IIT_Rosters,connection=conn,metric='plusminus')

	result_2 = pr.generate_2_player_pairs()
	result_2.to_csv('result_2.csv')

	# result_3 = pr.generate_3_player_pairs()
	# result_3.to_csv('result_3.csv')














		


