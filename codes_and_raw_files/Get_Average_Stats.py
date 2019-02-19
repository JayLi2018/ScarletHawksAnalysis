import re
import pandas as pd 
import os
import glob

formats = ['Offensive','Defensive']

team_defensive_categories = ['Overall Defense','Play Types','Offense Including Passes','During Pass Out Situations',
'During Trapping Situations','Shot Attempt - Half Court','Catch and Shoot - Half Court',
'Dribble Jumper - Half Court','Jump Shot Range - half court']

team_offensive_categories = ['Overall Offense','Play Types','Offense Including Passes','During Pass Out Situations',
'During Trapping Situations','Shot Attempt - Half Court','Catch and Shoot - Half Court',
'Dribble Jumper - Half Court','Jump Shot Range - half court']

player_element = ['Cut','Offensive Rebounds (put backs)','Transition','Overall','Spot Up','P&R Ball Handler','Post-Up','Isolation','Off Screen','Hand Off','P&R Roll Man','Miscellaneous']

Team_First_Row = ['Team_Name','Uploaded_Date','Format_Name','Category_Name','Element_Name','Percentage_Time','Poss_Per_Game','Points','PPP','Rank','Rating','FG_miss','FG_Made',
'FGA','FG','Adjusted_FG','Percent_Turnover','Percent_FT','Percent_Shooting_Foul','Percent_Score']

Player_First_Row = ['Team_Name','Player_Name','Uploaded_Date','Category_Name','Format_Name','Element_Name','Percentage_Time','Poss_Per_Game','Points','PPP','Rank','Rating','FG_miss','FG_Made',
'FGA','FG','Adjusted_FG','Percent_Turnover','Percent_FT','Percent_Shooting_Foul','Percent_Score']



tab = re.compile(r'(\t+)')
hashtag = re.compile(r'\#')
unidentified =re.compile(r'Unidentifiable Player')


class Average_File_Converter:

	def __init__(self,Uploaded_Date):
		self.Uploaded_Date = Uploaded_Date


	def team_average_generator(self,file):
	   
		self.file = file
		self.Team_Name= file.split('_')[-2]
		self.opened_file = open(self.file,"r")
		if(file.split('_')[-1]=='Defensive'):
			# print("found Defensive")
			self.format = 'Defensive'
			self.categories = team_defensive_categories
			self.player_element = player_element
		elif(file.split('_')[-1]=='Offensive'):
			# print("found Offensive")
			self.format = "Offensive"
			self.categories = team_offensive_categories
			self.player_element = player_element
		phase1_list = []
		for line in self.opened_file:
			if(tab.search(line) is None):
				# print("No tab is found!")
				if(line.strip() in self.categories or line.strip() in self.player_element):
					# print("found a category")
					phase1_list.append(line)
			else:
				phase1_list.append(line)
		
		# print(phase1_list)
		cur_category = None
		initial_list = []
		full_list = []
		last_element = None
		cur_element = None
		list_of_lists = [Team_First_Row]
		
		for line in phase1_list:
			if(line.strip() not in self.categories and cur_category==None):
				continue
			elif(line.strip() in self.categories and cur_category==None):
				cur_category = line.strip()
				# print("found a category: "+cur_category)
			elif(line.strip() in self.categories and cur_category is not None):
				cur_category = line.strip()
			elif(line.strip() in self.player_element and cur_category is not None):
				cur_category=None
			elif(line.strip() not in self.categories and cur_category is not None ):
				initial_list = [self.Team_Name,self.Uploaded_Date,self.format,cur_category]
				cur_element = line.split('\t')[0].strip()
				if(cur_category=='Shot Attempt - Half Court' and cur_element=='Short Shot Clock <4 Seconds'):
					special_list = [last_element,cur_element]
					cur_element = '.'.join(special_list)
				if(cur_element == self.Team_Name):
					cur_element = 'Overall'
				initial_list.append(cur_element)
				# print(initial_list)
				rest_list = [x.strip('\t') for x in line.split('\t')[1:]]
				# print("rest_list")
				# print(rest_list)
				initial_list.extend(rest_list)
				# print("full_list")
				# print(initial_list)
				list_of_lists.append(initial_list)
				last_element = cur_element
		 
		headers = list_of_lists.pop(0)
		df = pd.DataFrame(list_of_lists, columns=headers)
		# print(df)
		return df

		

	def player_average_generator(self,file):
	   
		self.file = file
		self.Team_Name= file.split('_')[-2]
		self.opened_file = open(self.file,"r")
		if(file.split('_')[-1]=='Defensive'):
			# print("found Defensive")
			self.format = 'Defensive'
			self.categories = team_defensive_categories
			self.player_element = player_element
		elif(file.split('_')[-1]=='Offensive'):
			# print("found Offensive")
			self.format = "Offensive"
			self.categories = team_offensive_categories
			self.player_element = player_element
		phase1_list = []
		for line in self.opened_file:
			if(tab.search(line) is None):
				# print("No tab is found!")
				if(line.strip() in self.categories or line.strip() in self.player_element):
					# print("found a category")
					phase1_list.append(line)
			else:
				phase1_list.append(line)
		
		# print(phase1_list)
		cur_element = None
		initial_list = []
		full_list = []
		last_element = None
		cur_element = None
		list_of_lists = [Player_First_Row]
		category = 'Play Types'
		for line in phase1_list:
			if(line.strip() not in self.player_element and cur_element==None):
				continue
			elif(line.strip() in self.player_element and cur_element==None):
				cur_element = line.strip()
				# print("found a category: "+cur_element)
			elif(line.strip() in self.player_element and cur_element is not None):
				cur_element = line.strip()
			elif(line.strip() in self.categories and cur_element is not None):
				cur_element=None
			elif(line.strip() not in self.player_element and cur_element is not None ):
				if(hashtag.search(line) is None or unidentified.search(line) is not None):
					continue
				else:
					player_name = re.sub(r'\#[0-9][0-9]? ','',line.split('\t')[0].strip())
					player_name_list = player_name.split(' ')
					if(len(player_name_list)>2):
						del player_name_list[-1]
					player_name = ' '.join(player_name_list)

					if(player_name=='Neil O\'Donnell'):
						print('find donnel!')
						player_name ='Neil Odonnell'
					initial_list = [self.Team_Name,player_name,self.Uploaded_Date,category,self.format,cur_element]
					# print(initial_list)
					rest_list = [x.strip('\t') for x in line.split('\t')[1:]]
					# print("rest_list")
					# print(rest_list)
					initial_list.extend(rest_list)
					# print("full_list")
					# print(initial_list)
					list_of_lists.append(initial_list)
		 
		headers = list_of_lists.pop(0)
		df = pd.DataFrame(list_of_lists, columns=headers)
		# print(df)
		return df




			
if __name__ == "__main__":
	os.chdir('/home/chenjie/Desktop/ScarletHawksAnalysis/codes_and_raw_files/Updates/2.17 package/Team_Player_Average/')
	afc = Average_File_Converter('2019-2-12')
	team_dfs = []
	player_dfs = []
	for file in glob.glob("*"):
		# print(file)
		team = afc.team_average_generator(file)
		team_dfs.append(team)
	 	player = afc.player_average_generator(file)
	 	player_dfs.append(player)
	team_result = pd.concat(team_dfs)
	player_result = pd.concat(player_dfs)
	team_result.to_csv("team_average_results.csv",index=None)
	player_result.to_csv("player_average_results.csv",index=None)






