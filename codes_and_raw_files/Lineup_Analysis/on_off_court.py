import psycopg2
import pandas as pd 

class on_off_court:


	def __init__(self, conn, rosters):
		self.conn = conn
		self.rosters = rosters

	def get_on_off_court_value(self,metric_formula=None,metric_alias=None,metric_desc=None):

		list_of_dfs = []
		for n in self.rosters:
			
			On_Court_Query = '''
			SELECT '{}' AS player, SUM(min) AS min, '{}' AS metric_name, 'on_court' AS type, '{}' as metric_desc, {} AS metric_value \
			FROM season_lineups \
			WHERE lineup_players like '%{}%' and team_name='Illinois Tech Scarlet Hawks'
			'''.format(n,metric_alias,metric_desc,metric_formula,n)

			df1 = pd.read_sql(On_Court_Query,self.conn)
			list_of_dfs.append(df1)


			Off_Court_Query ='''
			SELECT '{}' AS player, SUM(min) AS min, '{}' AS metric_name, 'off_court' AS type, '{}' as metric_desc, {} AS metric_value \
			FROM season_lineups \
			WHERE lineup_players not like '%{}%' and team_name='Illinois Tech Scarlet Hawks'
			'''.format(n,metric_alias,metric_desc,metric_formula,n)

			df2 = pd.read_sql(Off_Court_Query,self.conn)
			list_of_dfs.append(df2)


		result_df = pd.concat(list_of_dfs)

		return result_df


if __name__ == '__main__':

	conn = psycopg2.connect(dbname="jaybball",user="lchenjie",host="localhost",port="5432",password='lcj53242')

	IIT_Rosters = ['Anthony Mosley', 'Ben Wagner', 'Heath Sheridan', 'Ahmad Muhammad','Jake Bruns', 'Jalen Lomax',
	 'Calvin Schmitz', 'Capriest Gardner', 'Brett Ott', 'Jake Digiorgio', 'Max Hisatake',
	  'Otis Reale', 'Milos Dugalic', 'Cody Mattson', 'Parker Joncus', 'Guy Ostroff', 'Ricardo Whitehead', 
	  'Kohl Linder', 'Zach Parduhn']

	ooc = on_off_court(conn=conn,rosters=IIT_Rosters)

	arg_list = ['sum(plusminus)','plusminus','Net performance Evaluation Metric']

	df = ooc.get_on_off_court_value(metric_formula=arg_list[0],metric_alias=arg_list[1],metric_desc=arg_list[2])

	df.to_csv('on_off_court.csv',index=False)




