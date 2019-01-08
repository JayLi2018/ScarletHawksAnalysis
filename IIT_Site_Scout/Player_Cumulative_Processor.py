import pandas as pd 
import os
import glob
import re

os.chdir('/home/chenjie/Desktop/ScarletHawksAnalysis/IIT_Site_Scout/Team_Cumulative/')


hashtag = re.compile(r'\#')
player = re.compile(r'\#[0-9][0-9]? ([A-Z][a-z]+ [A-Z][a-z]+)')

class FileProcessor:

	def __init__(self,file):

		self.file = file
		self.opened_file = open(self.file,"r")

	def process(self):

		first_list = []
		for line in self.opened_file:
			if(hashtag.search(line) is not None):
				first_list.append(line)
			else:
				continue

		players = []
		Header = ['Team_Name','Player_Name','GP','Min','SST','SSTexPts','Pts','Ast','TO','Ast_Turnover_Ratio','Stl','StlPos','Blk','TtlReb',
		'OffReb','DefReb','FGA','FG_Made','FG_miss','FG','adjusted_FG','Two_FGA','Two_FG_Made','Two_FG_miss','Two_FG','Three_FGA',
		'Three_FG_Made','Three_FG_miss','Three_FG','FTA','FT_Made','FT_miss','FT','AndOne','PFTkn','PFCom']

		rows=[Header]

		for cur_line in first_list:
			cur_player = player.search(cur_line).group(1)
			# print("cur_number: "+cur_player)
			if(cur_player in players):
				for line in rows[1:]:
					if(player.search(line[0]).group(1)==cur_player):
						line.extend(cur_line.strip().split('\t')[2:])
			if(cur_player not in players):
				players.append(cur_player)
				rows.append(cur_line.strip().split('\t'))
				# print(rows)
				# row.append(' '.join(cur_line.split('\t')[0].split(' ')[1:]))
				# rest_of_line = cur_line.split('\t')[1:]
				# row.extend(rest_of_line)
				# final_list.append(row)
		for row in rows[1:]:
			row[0] = ' '.join(row[0].split(' ')[1:])
		# print(rows)

		headers = rows.pop(0)
		for row in rows:
			row[0] = ' '.join(row[0].split(' ')[:2])
			row.insert(0,self.file.split('.')[0])
		df = pd.DataFrame(rows, columns=headers)
		print(str(self.file.split('.')[0])+': ')
		print(players)
		return df
		# df.to_csv(self.file.split('.')[0]+'.csv',index=False)



if __name__ == '__main__':
	
	df_list = []

	for file in glob.glob('*.txt'):
		processor = FileProcessor(file)
		df = processor.process()
		df_list.append(df)

	result = pd.concat(df_list)

	result.to_csv('player_avg.csv')
 









