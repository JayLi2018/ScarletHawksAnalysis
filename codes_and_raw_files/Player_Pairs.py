import psycopg2
import pandas as pd 
from MinHeap import MinHeap
from MaxHeap import MaxHeap
from Pairs_Dict import Metrics_Dict


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
				connection=conn
				):

		self.team_name = team_name
		self.rosters = rosters
		self.conn = connection

	def generate_2_player_pairs(self,num_of_pairs=5,direction ='high',metric_formula=None,metric_alias=None,metric_desc=None):  
		
		"""
		 num_of_pairs: the number of pairs you want to have
		 direction: the specified metrics orientation, 'low': the lower the better, 'high': the higher the better
		 metric: is the attribute in the table that you want to based on when you rank

		"""

		heap_list = []
		for n in self.rosters:
			if(direction=='high'):
				heap = MinHeap(key='metric_value',data_list=[])
			else:
				heap = MaxHeap(key='metric_value',data_list=[])
			for m in self.rosters:
				if(m==n):
					continue
				else:
					candidate_pair = [n,m]
					candidate_pair.sort()
					Q = '''
					SELECT '{}' AS chosen_player,'{}' AS pair,SUM(min) AS min, '{}' AS metric_name, '{}' as metric_desc, {} AS metric_value \
					FROM season_lineups \
					WHERE lineup_players like '%{}%'
					'''.format(n,','.join(candidate_pair),metric_alias,metric_desc,metric_formula,'%'.join(candidate_pair))
					
					df = pd.read_sql(Q,self.conn)
					if(df.isnull().values.any()):
						pass
					else:
						df['metric_value'] = pd.to_numeric(df['metric_value'])
						if(heap.size()<num_of_pairs):
							heap.add(df)
						else:
							if(df['metric_value'].loc[0]>=heap.peek()['metric_value'].loc[0]):
								heap.pop()
								heap.add(df)
			player_result = heap.get_result()

			print(player_result)
			if(player_result is not None):
				heap_list.append(player_result)

		result_df = pd.concat(heap_list)

		return result_df

	def generate_3_player_pairs(self,num_of_pairs=5,direction ='high',metric_formula=None,metric_alias=None,metric_desc=None):

		"""

		 num_of_pairs: the number of pairs you want to have
		 direction: the specified metrics orientation, 'low': the lower the better, 'high': the higher the better
		 metric: is the attribute in the table that you want to based on when you rank

		"""

		heap_list = []
		for n in range(len(self.rosters)):
			if(direction=='high'):
				heap = MinHeap(key='metric_value',data_list=[])
			else:
				heap = MaxHeap(key='metric_value',data_list=[])

			for m in range(len(self.rosters)):
				if(m==n):
					continue
				else:
					for p in range(m+1,len(self.rosters)):
						candidate_pair = [self.rosters[n],self.rosters[m],self.rosters[p]]
						candidate_pair.sort()
						Q = '''
						SELECT '{}' AS chosen_player,'{}' AS pair,SUM(min) AS min, '{}' AS metric_name, '{}' as metric_desc, {} AS metric_value \
						FROM season_lineups \
						WHERE lineup_players like '%{}%'
						'''.format(self.rosters[n],','.join(candidate_pair),metric_alias,metric_desc,metric_formula,'%'.join(candidate_pair))

						df = pd.read_sql(Q,self.conn)
						if(df.isnull().values.any()):
							pass
						else:
							df['metric_value'] = pd.to_numeric(df['metric_value'])
							if(heap.size()<num_of_pairs):
								heap.add(df)
							else:
								if(df['metric_value'].loc[0]>=heap.peek()['metric_value'].loc[0]):
									heap.pop()
									heap.add(df)

			player_result = heap.get_result()


			print(player_result)
			if(player_result is not None):
				heap_list.append(player_result)

		result_df = pd.concat(heap_list)

		return result_df


if __name__ == "__main__":

	pr = Pair_Rankings(team_name='Illinois Tech Scarlet Hawks',rosters=IIT_Rosters,connection=conn)

	list_of_2_pairs = []
	for n in Metrics_Dict.values():

		direction=n[0]
		metric_formula=n[1]
		metric_alias=n[2]
		metric_desc=n[3]

		result_2 = pr.generate_2_player_pairs(num_of_pairs=5,direction =direction,metric_formula=metric_formula,
			metric_alias=metric_alias,metric_desc=metric_desc)

		list_of_2_pairs.append(result_2)

	list_of_3_pairs = []
	for n in Metrics_Dict.values():

		direction=n[0]
		metric_formula=n[1]
		metric_alias=n[2]
		metric_desc=n[3]

		result_3 = pr.generate_3_player_pairs(num_of_pairs=5,direction=direction,metric_formula=metric_formula,
			metric_alias=metric_alias,metric_desc=metric_desc)

		list_of_3_pairs.append(result_3)


	result_df_2 = pd.concat(list_of_2_pairs)
	result_df_2.to_csv('all_result_2.csv')

	result_df_3 = pd.concat(list_of_3_pairs)
	result_df_3.to_csv('all_result_3.csv')














		


