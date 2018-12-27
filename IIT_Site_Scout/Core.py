import re
import os
from Classes import Team,Player,Lineup,Lineup_Stats,Score_Tracker
import File_Processor
from File_Processor import FileProcessor
from Rosters import Team_Lists
import pandas as pd

# this is the lineup stats generator

# list of regexes:
first_half = re.compile(r'1 Half')
second_half = re.compile(r'2 Half')
over_time = re.compile(r'3 Half')
off_reb = re.compile(r'([A-Z]+ {0,1}?[A-Z]+)\.?\,([A-Z]+\'{0,1}?[A-Z]+) offensive rebound')
def_reb = re.compile(r'([A-Z]+ {0,1}?[A-Z]+)\.?\,([A-Z]+\'{0,1}?[A-Z]+) defensive rebound')
shot_attempt = re.compile(r'([A-Z]+ {0,1}?[A-Z]+)\.?\,([A-Z]+\'{0,1}?[A-Z]+) .* (jump shot|layup|dunk)')
two_made = re.compile(r'([A-Z]+ {0,1}?[A-Z]+)\.?\,([A-Z]+\'{0,1}?[A-Z]+) made (jump shot|layup|dunk)')
two_missed = re.compile(r'([A-Z]+ {0,1}?[A-Z]+)\.?\,([A-Z]+\'{0,1}?[A-Z]+) missed (jump shot|layup|dunk)')
three_made = re.compile(r'([A-Z]+ {0,1}?[A-Z]+)\.?\,([A-Z]+\'{0,1}?[A-Z]+) made 3-pt\.')
three_miss = re.compile(r'([A-Z]+ {0,1}?[A-Z]+)\.?\,([A-Z]+\'{0,1}?[A-Z]+) missed 3-pt\.')
freethrow_made = re.compile(r'([A-Z]+ {0,1}?[A-Z]+)\.?\,([A-Z]+\'{0,1}?[A-Z]+) made free throw')
freethrow_miss =re.compile(r'([A-Z]+ {0,1}?[A-Z]+)\.?\,([A-Z]+\'{0,1}?[A-Z]+) missed free throw') 
assist = re.compile(r'Assist by ([A-Z]+ {0,1}?[A-Z]+)\.?\,([A-Z]+\'{0,1}?[A-Z]+)')
turnover = re.compile(r'Turnover by ([A-Z]+ {0,1}?[A-Z]+)\.?\,([A-Z]+\'{0,1}?[A-Z]+)')
steal = re.compile(r'Steal by ([A-Z]+ {0,1}?[A-Z]+)\.?\,([A-Z]+\'{0,1}?[A-Z]+)')
block = re.compile(r'Block by ([A-Z]+ {0,1}?[A-Z]+)\.?\,([A-Z]+\'{0,1}?[A-Z]+)')
foul = re.compile(r'Foul by ([A-Z]+ {0,1}?[A-Z]+)\.?\,([A-Z]+\'{0,1}?[A-Z]+)')
player_movement_out = re.compile(r'([A-Z]+ {0,1}?[A-Z]+)\.?\,([A-Z]+\'{0,1}?[A-Z]+) goes to the bench')
player_movement_in = re.compile(r'([A-Z]+ {0,1}?[A-Z]+)\.?\,([A-Z]+\'{0,1}?[A-Z]+) enters the game')
timer = re.compile(r'([0-9][0-9])\:([0-5][0-9])')


class DataExtractor(object):


	def __init__(self,Game_ID=None,game_file_loc=None,output_loc=None,
		home_team=None,away_team=None,
		home_first_lineup = None,away_first_lineup = None,
		home_second_lineup = None, away_second_lineup = None,
		home_ot_lineup = None, away_ot_lineup = None,
		**kwargs):
			self.Game_ID = Game_ID
			self.game_file_loc = game_file_loc
			self.output_loc = output_loc
			
			self.home_team = home_team
			self.away_team = away_team
			
			self.home_team_obj = Team(home_team)
			self.away_team_obj = Team(away_team)

			self.home_first_lineup = home_first_lineup
			self.home_second_lineup = self.home_first_lineup
			self.home_ot_lineup = self.home_first_lineup

			self.away_first_lineup = away_first_lineup
			self.away_second_lineup = self.away_first_lineup
			self.away_ot_lineup = self.away_first_lineup

	def get_time(self,line):  # change time to float format so that it's easier to compare between times  
		match = timer.search(line)
		if match:
			return (float(match.group(1)) + float(match.group(2))/60)


	def generate_data(self,game_name):

		self.score_track = Score_Tracker()
		self.score_track.tracker['Game_ID'] = self.Game_ID
		self.home_team_rosters=[]
		self.away_team_rosters=[]
		self.home_score=0
		self.away_score=0
		self.home_lineup_id = 0  #initialize an ID for home lineups
		self.away_lineup_id = 0  #initialize an ID for away lineups
		self.game_name = game_name
		for h in Team_Lists:
			if(h[0]==self.home_team):
				print("found home_team")
				self.home_team_rosters=h[1:]
		for a in Team_Lists:
			if(a[0]==self.away_team):
				print("found away_team")
				self.away_team_rosters=a[1:]	    	
		
		print("home:")
		print(self.home_team_rosters)
		print("away") 
		print(self.away_team_rosters)

		first_half_file = []
		second_half_file = []
		over_time_file = []
		
		game_file = self.game_file_loc+self.game_name

		file = open(game_file,'r')

		processor = FileProcessor(game_file)
		self.sessions_list = processor.process_file()

		if(len(self.sessions_list)==2):
			self.handle_session(session_doc=self.sessions_list[0],session_num=1)
			self.handle_session(session_doc=self.sessions_list[1],session_num=2)
			print("Number of lineups in Home Team: ")
			print(len(self.home_team_obj.lineups))
			print("Number of lineup infos in Home Team: ")
			print(len(self.home_team_obj.lineup_stats))


			print("Number of lineups in Away Team: ")
			print(len(self.away_team_obj.lineups))
			print("Number of lineup infos in Away Team: ")
			print(len(self.away_team_obj.lineup_stats))

		if(len(self.sessions_list)==3):
			self.handle_session(session_doc=self.sessions_list[0],session_num=1)
			self.handle_session(session_doc=self.sessions_list[1],session_num=2)
			self.handle_session(session_doc=self.sessions_list[2],session_num=3)
			print("Number of lineups in Home Team: ")
			print(len(self.home_team_obj.lineups))
			print("Number of lineup infos in Home Team: ")
			print(len(self.home_team_obj.lineup_stats))


			print("Number of lineups in Away Team: ")
			print(len(self.away_team_obj.lineups))
			print("Number of lineup infos in Away Team: ")
			print(len(self.away_team_obj.lineup_stats))

	def outputs(self):
		"""
		lineup_Stats:
		player_stats:
		score_tracker:
		"""
		#---------------------output lineups---------------------------#
		home_lineup_stats_dicts = []
		for n in self.home_team_obj.lineup_stats:
			df = pd.DataFrame(n.stats,index=[0])
			home_lineup_stats_dicts.append(df)
		home_lineup_stats_df = pd.concat(home_lineup_stats_dicts)
		home_lineup_stats_df.to_csv(self.output_loc+self.game_name+'_'+self.home_team+'_home_lineups.csv',index=False)

		away_lineup_stats_dicts = []
		for n in self.away_team_obj.lineup_stats:
			df = pd.DataFrame(n.stats,index=[0])
			away_lineup_stats_dicts.append(df)
		away_lineup_stats_df = pd.concat(away_lineup_stats_dicts)
		away_lineup_stats_df.to_csv(self.output_loc+self.game_name+'_'+self.away_team+'_away_lineups.csv',index=False)

		#---------------------output player stats----------------------#
		home_player_stats_dicts = []
		for n in self.home_team_obj.lineups:
			for m in n.players:
				df = pd.DataFrame(m.player_stats,index=[0])
				home_player_stats_dicts.append(df)
		home_player_stats_df = pd.concat(home_player_stats_dicts)
		home_player_stats_df.to_csv(self.output_loc+self.game_name+'_'+self.home_team+'_home_players.csv',index=False)

		away_player_stats_dicts = []
		for n in self.away_team_obj.lineups:
			for m in n.players:
				df = pd.DataFrame(m.player_stats,index=[0])
				away_player_stats_dicts.append(df)
		away_player_stats_df = pd.concat(away_player_stats_dicts)
		away_player_stats_df.to_csv(self.output_loc+self.game_name+'_'+self.away_team+'_away_players.csv',index=False)

		#----------------------output score tracker---------------------#
		tracker_df = pd.DataFrame(self.score_track.tracker)
		clear_tracker_df = tracker_df.drop_duplicates(subset='Time', keep='last')
		clear_tracker_df.to_csv(self.output_loc+self.game_name+'_tracker.csv',index=False)

	def handle_session(self,session_doc=None,session_num = None,
		home_session_lieup=None, away_session_lineup=None,
		output_loc=None, 
		**kwargs):
	
			self.session_doc = session_doc
			if(session_num==None):
				print("No session number defined in \"handle session\"")
			elif(session_num==1):
				home_session_start_lineup = self.home_first_lineup
				away_session_start_lineup = self.away_first_lineup
			elif(session_num==2):
				home_session_start_lineup = self.home_second_lineup
				away_session_start_lineup = self.away_second_lineup
			elif(session_num==3):
				home_session_start_lineup = self.home_ot_lineup
				away_session_start_lineup = self.away_ot_lineup

			if(session_num!=3):
				cur_time = 20.0
			else:
				cur_time = 5.0

			home_lineup = Lineup(session_num)
			home_lineup_info = Lineup_Stats()
			self.home_lineup_id+=1
			home_lineup_info.stats['Team_Name'] = self.home_team			
			home_lineup_info.stats['Lineup_ID'] = self.home_lineup_id
			home_lineup_info.stats['From'] = cur_time	
			home_lineup_info.stats['Game_ID'] = self.Game_ID
			home_lineup_info.stats['session_number'] = session_num					
			for player_name in home_session_start_lineup:
				p = Player(Team_Name=self.home_team,Player_Name=player_name)
				p.player_stats['Game_ID'] = self.Game_ID
				p.player_stats['Lineup_ID'] = self.home_lineup_id
				home_lineup.players.append(p)
			self.home_team_obj.lineups.append(home_lineup)
			
			home_player_list = []
			for player in home_lineup.players:
				home_player_list.append(player.player_stats['Player_Name'])
			home_player_list.sort()
			home_lineup_info.stats['Lineup_Players']= ','.join(home_player_list)

			self.home_team_obj.lineup_stats.append(home_lineup_info)
			print(self.home_team_obj.Team_Name+" lineups: ")
			print(str(len(self.home_team_obj.lineups)))
			print(self.home_team_obj.Team_Name+" lineups_stats: ")
			print(str(len(self.home_team_obj.lineup_stats)))
			print('Home Players:')
			for player in home_lineup.players:
				print(player.player_stats['Player_Name'])
			print('\n')
			
			away_lineup = Lineup(session_num)
			away_lineup_info = Lineup_Stats()
			self.away_lineup_id+=1
			away_lineup_info.stats['Team_Name'] = self.away_team
			away_lineup_info.stats['Lineup_ID'] = self.away_lineup_id
			away_lineup_info.stats['From'] = cur_time
			away_lineup_info.stats['Game_ID'] = self.Game_ID
			away_lineup_info.stats['session_number'] = session_num		
			for player_name in away_session_start_lineup:
				p = Player(Team_Name=self.away_team,Player_Name=player_name)
				p.player_stats['Lineup_ID'] = self.away_lineup_id
				p.player_stats['Game_ID'] = self.Game_ID
				away_lineup.players.append(p)
			self.away_team_obj.lineups.append(away_lineup)
			
			self.away_team_obj.lineup_stats.append(away_lineup_info)
			away_player_list = []
			for player in away_lineup.players:
				away_player_list.append(player.player_stats['Player_Name'])
			away_player_list.sort()
			away_lineup_info.stats['Lineup_Players']= ','.join(away_player_list)

			print(self.away_team_obj.Team_Name+" lineups: ")
			print(str(len(self.away_team_obj.lineups)))
			print(self.away_team_obj.Team_Name+" lineups_stats: ")
			print(str(len(self.away_team_obj.lineup_stats)))
			print('Away Players:')
			for player in away_lineup.players:
				print(player.player_stats['Player_Name'])
			print('\n')
			
			cur_home_lineup = home_lineup
			cur_away_lineup = away_lineup
			cur_home_lineup_info = home_lineup_info
			cur_away_lineup_info = away_lineup_info
			home_sub_in_buffer = []
			home_sub_out_buffer = []
			away_sub_in_buffer = []
			away_sub_out_buffer = []

			for line in session_doc:
				cur_time = self.get_time(line)

				if(player_movement_in.search(line) is not None or player_movement_out.search(line) is not None):
					if(player_movement_in.search(line) is not None):
						player = player_movement_in.search(line).group(2).capitalize() + ' ' +player_movement_in.search(line).group(0).split(',')[0].split(' ')[0].capitalize()  # convert all uppercase name to normal format name
						if(player in self.home_team_rosters):					
							for n in self.home_team_rosters:
								if(n == player):
									player_in = Player(Team_Name=self.home_team,Player_Name=n)
									player_in.player_stats['Game_ID'] = self.Game_ID
									home_sub_in_buffer.append(player_in) # sub_in_buffer contains player objects

						elif(player in self.away_team_rosters):					
							for n in self.away_team_rosters:
								if(n == player):
									player_in = Player(Team_Name=self.away_team,Player_Name=n)
									player_in.player_stats['Game_ID'] = self.Game_ID
									away_sub_in_buffer.append(player_in) # sub_in_buffer contains player objects


					if(player_movement_out.search(line) is not None):
						player = player_movement_out.search(line).group(2).capitalize() + ' ' +player_movement_out.search(line).group(0).split(',')[0].split(' ')[0].capitalize()  # convert all uppercase name to normal format name
						if(player in self.home_team_rosters):					
							for n in self.home_team_rosters:
								if(n == player):
									player_out = Player(Team_Name=self.home_team,Player_Name=n)
									player_out.player_stats['Game_ID'] = self.Game_ID
									home_sub_out_buffer.append(player_out) # sub_out_buffer contains player objects

						elif(player in self.away_team_rosters):					
							for n in self.away_team_rosters:
								if(n == player):
									player_out = Player(Team_Name=self.away_team,Player_Name=n)
									player_out.player_stats['Game_ID'] = self.Game_ID
									away_sub_out_buffer.append(player_out) # sub_out_buffer contains player objects


					if(bool(len(home_sub_out_buffer)>=1 and len(home_sub_in_buffer)>=1)==True or bool(len(away_sub_out_buffer)>=1 and len(away_sub_in_buffer)>=1)==True):
						if(len(home_sub_out_buffer)>=1 and len(home_sub_in_buffer)>=1):							
							out_player_name = home_sub_out_buffer[-1].player_stats['Player_Name']
							home_sub_out_buffer.pop()

							copied_cur_home_lineup = Lineup(session_num)
							for p in cur_home_lineup.players:
								copied_player = Player(Team_Name=self.home_team,Player_Name=p.player_stats['Player_Name'])
								copied_player.player_stats['Game_ID'] = self.Game_ID

								copied_cur_home_lineup.players.append(copied_player)


							for n in copied_cur_home_lineup.players:
								if(n.player_stats['Player_Name'] == out_player_name):
									copied_cur_home_lineup.players.remove(n)
								else:
									continue

							copied_cur_home_lineup.players.append(home_sub_in_buffer[-1]) # add the sub_in player
							
							cur_home_lineup = copied_cur_home_lineup  # just need to copy, and even though it is a sudo_lineup, it still need to be assigned

							home_sub_in_buffer.pop()


							if(len(home_sub_in_buffer)==0):

								self.home_team_obj.lineups.append(cur_home_lineup)
								
								print(str(self.get_time(line))+"Home Team New Lineup:")
								for n in cur_home_lineup.players:
									print(n.player_stats['Player_Name'])
								print('\n')

								self.home_lineup_id+=1

								for n in cur_home_lineup.players:
									n.player_stats['Lineup_ID'] = self.home_lineup_id

								
								cur_home_lineup_info.stats['To'] = cur_time
								cur_home_lineup_info.stats['Min'] = cur_home_lineup_info.stats['From'] - cur_home_lineup_info.stats['To']
								cur_home_lineup_info.stats['PlusMinus'] = cur_home_lineup_info.stats['Lineup_Score'] - cur_home_lineup_info.stats['Oppo_Score']
								home_new_lineup_info = Lineup_Stats()
								home_new_lineup_info.stats['session_number'] = session_num
								home_player_list = []
								for player in cur_home_lineup.players:
									home_player_list.append(player.player_stats['Player_Name'])
								home_player_list.sort()
								home_new_lineup_info.stats['Lineup_Players']= ','.join(home_player_list)

								cur_home_lineup_info = home_new_lineup_info
								home_new_lineup_info.stats['Team_Name'] = self.home_team
								home_new_lineup_info.stats['Lineup_ID'] = self.home_lineup_id	
								home_new_lineup_info.stats['From'] = cur_time
								home_new_lineup_info.stats['Game_ID'] = self.Game_ID
								self.home_team_obj.lineup_stats.append(home_new_lineup_info)


						if(len(away_sub_out_buffer)>=1 and len(away_sub_in_buffer)>=1):							
							out_player_name = away_sub_out_buffer[-1].player_stats['Player_Name']
							away_sub_out_buffer.pop()

							copied_cur_away_lineup = Lineup(session_num)
							for p in cur_away_lineup.players:
								copied_player = Player(Team_Name=self.away_team,Player_Name=p.player_stats['Player_Name'])
								copied_player.player_stats['Game_ID'] = self.Game_ID
								copied_cur_away_lineup.players.append(copied_player)


							for n in copied_cur_away_lineup.players:
								if(n.player_stats['Player_Name'] == out_player_name):
									copied_cur_away_lineup.players.remove(n)
								else:
									continue

							copied_cur_away_lineup.players.append(away_sub_in_buffer[-1]) # add the sub_in player
							
							cur_away_lineup = copied_cur_away_lineup  # just need to copy, and even though it is a sudo_lineup, it still need to be assigned

							away_sub_in_buffer.pop()

							if(len(away_sub_in_buffer)==0):
								self.away_team_obj.lineups.append(cur_away_lineup)


								print(str(self.get_time(line))+"Away Team New Lineup:")
								for n in cur_away_lineup.players:
									print(n.player_stats['Player_Name'])
								print('\n')

								self.away_lineup_id+=1

								for n in cur_away_lineup.players:
									n.player_stats['Lineup_ID'] = self.away_lineup_id

								cur_away_lineup_info.stats['To'] = cur_time
								cur_away_lineup_info.stats['Min'] = cur_away_lineup_info.stats['From'] - cur_away_lineup_info.stats['To'] 
								cur_away_lineup_info.stats['PlusMinus'] = cur_away_lineup_info.stats['Lineup_Score'] - cur_away_lineup_info.stats['Oppo_Score']
								away_new_lineup_info = Lineup_Stats()
								away_new_lineup_info.stats['session_number'] = session_num
								away_player_list = []
								for player in cur_away_lineup.players:
									away_player_list.append(player.player_stats['Player_Name'])
								away_player_list.sort()
								away_new_lineup_info.stats['Lineup_Players']= ','.join(away_player_list)
								cur_away_lineup_info = away_new_lineup_info
								away_new_lineup_info.stats['Team_Name'] = self.away_team
								away_new_lineup_info.stats['From'] = cur_time
								away_new_lineup_info.stats['Game_ID'] = self.Game_ID
								away_new_lineup_info.stats['Lineup_ID'] = self.away_lineup_id
								self.away_team_obj.lineup_stats.append(away_new_lineup_info)

				# ---------------------------------Offensive Rebound -----------------------------------------------------#


				if(off_reb.search(line) is not None):      # Offensive Reb

					name_off_reb = off_reb.search(line).group(2).capitalize() + ' ' +off_reb.search(line).group(0).split(',')[0].split(' ')[0].capitalize()  # convert all uppercase name to normal format name
					home_found = False
					away_found = False

					for p in cur_home_lineup.players:
						if(p.player_stats['Player_Name'] == name_off_reb):
							p.player_stats['OffReb']+=1
							p.player_stats['TtlReb']+=1
							home_found = True
							cur_home_lineup_info.stats['OffReb']+=1
							cur_home_lineup_info.stats['TtlReb']+=1
							break
					if(home_found ==False):
						cur_home_lineup_info.stats['Oppo_OffReb'] +=1
						cur_home_lineup_info.stats['Oppo_TtlReb'] +=1
					
					for p in cur_away_lineup.players:
						if(p.player_stats['Player_Name'] == name_off_reb):
							p.player_stats['OffReb']+=1
							p.player_stats['TtlReb']+=1
							away_found = True
							cur_away_lineup_info.stats['OffReb']+=1
							cur_away_lineup_info.stats['TtlReb']+=1
							break
					if(away_found ==False):
						cur_away_lineup_info.stats['Oppo_OffReb'] +=1
						cur_away_lineup_info.stats['Oppo_TtlReb'] +=1
				
				# ---------------------------------Defensive Rebound -----------------------------------------------------#

				if(def_reb.search(line) is not None):      # defensive Reb

					name_def_reb = def_reb.search(line).group(2).capitalize() + ' ' +def_reb.search(line).group(0).split(',')[0].split(' ')[0].capitalize()  # convert all uppercase name to normal format name
					home_found = False
					away_found = False

					for p in cur_home_lineup.players:
						if(p.player_stats['Player_Name'] == name_def_reb):
							p.player_stats['DefReb']+=1
							p.player_stats['TtlReb']+=1
							home_found = True
							cur_home_lineup_info.stats['DefReb']+=1
							cur_home_lineup_info.stats['TtlReb']+=1
							break
					if(home_found ==False):
						cur_home_lineup_info.stats['Oppo_DefReb'] +=1
						cur_home_lineup_info.stats['Oppo_TtlReb'] +=1
					
					for p in cur_away_lineup.players:
						if(p.player_stats['Player_Name'] == name_def_reb):
							p.player_stats['DefReb']+=1
							p.player_stats['TtlReb']+=1
							away_found = True
							cur_away_lineup_info.stats['DefReb']+=1
							cur_away_lineup_info.stats['TtlReb']+=1							
							break
					if(away_found ==False):
						cur_away_lineup_info.stats['Oppo_DefReb'] +=1
						cur_away_lineup_info.stats['Oppo_TtlReb'] +=1
				
				# ---------------------------------2 Point FGA---------------------------------------------------------------------#

				if(shot_attempt.search(line) is not None):  # Shot Attempts
					name_fga= shot_attempt.search(line).group(2).capitalize() + ' ' +shot_attempt.search(line).group(0).split(',')[0].split(' ')[0].capitalize()  # convert all uppercase name to normal format name
					home_found = False
					away_found = False
					made_shot_last_line = False  # this is useful for identifying assists

					if(two_made.search(line) is not None):
						for p in cur_home_lineup.players:
							if(p.player_stats['Player_Name'] == name_fga):
								p.player_stats['FGA']+=1
								p.player_stats['FGM']+=1
								p.player_stats['Two_FGA']+=1
								p.player_stats['Two_FGM']+=1
								p.player_stats['Pts']+=2
								home_found = True
								cur_home_lineup_info.stats['FGA']+=1
								cur_home_lineup_info.stats['FGM']+=1
								cur_home_lineup_info.stats['Two_FGA']+=1
								cur_home_lineup_info.stats['Two_FGM']+=1
								cur_home_lineup_info.stats['Lineup_Score']+=2
								self.home_score+=2
								cur_score_dif = self.home_score-self.away_score
								self.score_track.tracker['Session_num'].append(session_num)
								self.score_track.tracker['Score_Dif'].append(cur_score_dif)
								self.score_track.tracker['Time'].append(self.get_time(line))
								player_scored = p.player_stats['Player_Name']
								break 

						if(home_found == False):
							cur_home_lineup_info.stats['Oppo_FGA']+=1
							cur_home_lineup_info.stats['Oppo_FGM']+=1
							cur_home_lineup_info.stats['Oppo_Two_FGA']+=1
							cur_home_lineup_info.stats['Oppo_Two_FGM']+=1
							cur_home_lineup_info.stats['Oppo_Score']+=2

						for p in cur_away_lineup.players:
							if(p.player_stats['Player_Name'] == name_fga):
								p.player_stats['FGA']+=1
								p.player_stats['FGM']+=1
								p.player_stats['Two_FGA']+=1
								p.player_stats['Two_FGM']+=1
								p.player_stats['Pts']+=2
								away_found = True
								cur_away_lineup_info.stats['FGA']+=1
								cur_away_lineup_info.stats['FGM']+=1
								cur_away_lineup_info.stats['Two_FGA']+=1
								cur_away_lineup_info.stats['Two_FGM']+=1
								cur_away_lineup_info.stats['Lineup_Score']+=2
								self.away_score+=2
								cur_score_dif = self.home_score-self.away_score
								self.score_track.tracker['Session_num'].append(session_num)
								self.score_track.tracker['Score_Dif'].append(cur_score_dif)
								self.score_track.tracker['Time'].append(self.get_time(line))
								player_scored = p.player_stats['Player_Name']
								break 

						if(away_found == False):
							cur_away_lineup_info.stats['Oppo_FGA']+=1
							cur_away_lineup_info.stats['Oppo_FGM']+=1
							cur_away_lineup_info.stats['Oppo_Two_FGA']+=1
							cur_away_lineup_info.stats['Oppo_Two_FGM']+=1
							cur_away_lineup_info.stats['Oppo_Score']+=2

					elif(two_missed.search(line) is not None):

						for p in cur_home_lineup.players:
							if(p.player_stats['Player_Name'] == name_fga):
								p.player_stats['FGA']+=1
								p.player_stats['FGm']+=1
								p.player_stats['Two_FGA']+=1
								p.player_stats['Two_FGm']+=1
								home_found=True
								cur_home_lineup_info.stats['FGA']+=1
								cur_home_lineup_info.stats['FGm']+=1
								cur_home_lineup_info.stats['Two_FGA']+=1
								cur_home_lineup_info.stats['Two_FGm']+=1
								break
						if(home_found == False):
							cur_home_lineup_info.stats['Oppo_FGA']+=1
							cur_home_lineup_info.stats['Oppo_FGm']+=1
							cur_home_lineup_info.stats['Oppo_Two_FGm']+=1
							cur_home_lineup_info.stats['Oppo_Two_FGA']+=1

						for p in cur_away_lineup.players:
							if(p.player_stats['Player_Name'] == name_fga):
								p.player_stats['FGA']+=1
								p.player_stats['FGm']+=1
								p.player_stats['Two_FGA']+=1
								p.player_stats['Two_FGm']+=1
								away_found=True
								cur_away_lineup_info.stats['FGA']+=1
								cur_away_lineup_info.stats['FGm']+=1
								cur_away_lineup_info.stats['Two_FGA']+=1
								cur_away_lineup_info.stats['Two_FGm']+=1
								break
						if(away_found == False):
							cur_away_lineup_info.stats['Oppo_FGA']+=1
							cur_away_lineup_info.stats['Oppo_FGm']+=1
							cur_away_lineup_info.stats['Oppo_Two_FGm']+=1
							cur_away_lineup_info.stats['Oppo_Two_FGA']+=1
				
				# --------------------------------------3 Point FGA -------------------------------------------------------------#
					elif(three_made.search(line) is not None):
						name_fga= three_made.search(line).group(2).capitalize() + ' ' +three_made.search(line).group(0).split(',')[0].split(' ')[0].capitalize()  # convert all uppercase name to normal format name
						home_found = False
						away_found = False
						for p in cur_home_lineup.players:
							if(p.player_stats['Player_Name'] == name_fga):
								p.player_stats['FGA']+=1
								p.player_stats['FGM']+=1
								p.player_stats['Three_FGA']+=1
								p.player_stats['Three_FGM']+=1
								p.player_stats['Pts']+=3
								home_found = True
								cur_home_lineup_info.stats['FGA']+=1
								cur_home_lineup_info.stats['FGM']+=1
								cur_home_lineup_info.stats['Three_FGA']+=1
								cur_home_lineup_info.stats['Three_FGM']+=1
								cur_home_lineup_info.stats['Lineup_Score']+=3
								self.home_score+=3
								cur_score_dif = self.home_score-self.away_score
								self.score_track.tracker['Session_num'].append(session_num)
								self.score_track.tracker['Score_Dif'].append(cur_score_dif)
								self.score_track.tracker['Time'].append(self.get_time(line))
								player_scored = p.player_stats['Player_Name']
								break 

						if(home_found == False):
							cur_home_lineup_info.stats['Oppo_FGA']+=1
							cur_home_lineup_info.stats['Oppo_FGM']+=1
							cur_home_lineup_info.stats['Oppo_Three_FGA']+=1
							cur_home_lineup_info.stats['Oppo_Three_FGM']+=1
							cur_home_lineup_info.stats['Oppo_Score']+=3

						for p in cur_away_lineup.players:
							if(p.player_stats['Player_Name'] == name_fga):
								p.player_stats['FGA']+=1
								p.player_stats['FGM']+=1
								p.player_stats['Three_FGA']+=1
								p.player_stats['Three_FGM']+=1
								p.player_stats['Pts']+=3
								away_found = True
								cur_away_lineup_info.stats['FGA']+=1
								cur_away_lineup_info.stats['FGM']+=1
								cur_away_lineup_info.stats['Three_FGA']+=1
								cur_away_lineup_info.stats['Three_FGM']+=1
								cur_away_lineup_info.stats['Lineup_Score']+=3
								self.away_score+=3
								cur_score_dif = self.home_score-self.away_score
								self.score_track.tracker['Session_num'].append(session_num)
								self.score_track.tracker['Score_Dif'].append(cur_score_dif)
								self.score_track.tracker['Time'].append(self.get_time(line))
								player_scored = p.player_stats['Player_Name']
								break 

						if(away_found == False):
							cur_away_lineup_info.stats['Oppo_FGA']+=1
							cur_away_lineup_info.stats['Oppo_FGM']+=1
							cur_away_lineup_info.stats['Oppo_Three_FGA']+=1
							cur_away_lineup_info.stats['Oppo_Three_FGM']+=1
							cur_away_lineup_info.stats['Oppo_Score']+=3

					elif(three_miss.search(line) is not None):
						name_fga= three_miss.search(line).group(2).capitalize() + ' ' +three_miss.search(line).group(0).split(',')[0].split(' ')[0].capitalize()  # convert all uppercase name to normal format name
						home_found = False
						away_found = False
						made_shot_last_line = False  # this is useful for identifying assists
						for p in cur_home_lineup.players:
							if(p.player_stats['Player_Name'] == name_fga):
								p.player_stats['FGA']+=1
								p.player_stats['FGm']+=1
								p.player_stats['Three_FGA']+=1
								p.player_stats['Three_FGm']+=1
								home_found = True
								cur_home_lineup_info.stats['FGA']+=1
								cur_home_lineup_info.stats['FGm']+=1
								cur_home_lineup_info.stats['Three_FGA']+=1
								cur_home_lineup_info.stats['Three_FGm']+=1
								break
						if(home_found == False):
							cur_home_lineup_info.stats['Oppo_FGA']+=1
							cur_home_lineup_info.stats['Oppo_FGm']+=1
							cur_home_lineup_info.stats['Oppo_Three_FGm']+=1
							cur_home_lineup_info.stats['Oppo_Three_FGA']+=1

						for p in cur_away_lineup.players:
							if(p.player_stats['Player_Name'] == name_fga):
								p.player_stats['FGA']+=1
								p.player_stats['FGm']+=1
								p.player_stats['Three_FGA']+=1
								p.player_stats['Three_FGm']+=1
								away_found = True
								cur_away_lineup_info.stats['FGA']+=1
								cur_away_lineup_info.stats['FGm']+=1
								cur_away_lineup_info.stats['Three_FGA']+=1
								cur_away_lineup_info.stats['Three_FGm']+=1
								break
						if(away_found == False):
							cur_away_lineup_info.stats['Oppo_FGA']+=1
							cur_away_lineup_info.stats['Oppo_FGm']+=1
							cur_away_lineup_info.stats['Oppo_Three_FGm']+=1
							cur_away_lineup_info.stats['Oppo_Three_FGA']+=1

				if(freethrow_made.search(line) is not None):
					print('found a freethrow_made!')
					name_fta= freethrow_made.search(line).group(2).capitalize() + ' ' +freethrow_made.search(line).group(0).split(',')[0].split(' ')[0].capitalize()  # convert all uppercase name to normal format name
					home_found = False
					away_found = False
					for p in cur_home_lineup.players:
						if(p.player_stats['Player_Name'] == name_fta):
							print('found a home player who made freethrow!')
							p.player_stats['FTA']+=1
							p.player_stats['FTM']+=1
							p.player_stats['Pts']+=1
							home_found = True
							cur_home_lineup_info.stats['FTA']+=1
							cur_home_lineup_info.stats['FTM']+=1
							cur_home_lineup_info.stats['Lineup_Score']+=1
							self.home_score+=1
							cur_score_dif = self.home_score-self.away_score
							self.score_track.tracker['Session_num'].append(session_num)
							self.score_track.tracker['Score_Dif'].append(cur_score_dif)
							self.score_track.tracker['Time'].append(self.get_time(line))
							break 

					if(home_found == False):
						cur_home_lineup_info.stats['Oppo_FTA']+=1
						cur_home_lineup_info.stats['Oppo_FTM']+=1
						cur_home_lineup_info.stats['Oppo_Score']+=1

					for p in cur_away_lineup.players:
						if(p.player_stats['Player_Name'] == name_fta):
							print('found a away player who made freethrow!')
							p.player_stats['FTA']+=1
							p.player_stats['FTM']+=1
							p.player_stats['Pts']+=1
							away_found = True
							cur_away_lineup_info.stats['FTA']+=1
							cur_away_lineup_info.stats['FTM']+=1
							cur_away_lineup_info.stats['Lineup_Score']+=1
							self.away_score+=1
							cur_score_dif = self.home_score-self.away_score
							self.score_track.tracker['Session_num'].append(session_num)
							self.score_track.tracker['Score_Dif'].append(cur_score_dif)
							self.score_track.tracker['Time'].append(self.get_time(line))
							break 

					if(away_found == False):
						cur_away_lineup_info.stats['Oppo_FTA']+=1
						cur_away_lineup_info.stats['Oppo_FTM']+=1
						cur_away_lineup_info.stats['Oppo_Score']+=1

				if(freethrow_miss.search(line) is not None):
					print('found a freethrow_miss!')
					name_fta= freethrow_miss.search(line).group(2).capitalize() + ' ' +freethrow_miss.search(line).group(0).split(',')[0].split(' ')[0].capitalize()  # convert all uppercase name to normal format name
					home_found = False
					away_found = False
					for p in cur_home_lineup.players:
						if(p.player_stats['Player_Name'] == name_fta):
							print('found a home player who missed freethrow!')
							p.player_stats['FTA']+=1
							p.player_stats['FTm']+=1
							home_found = True
							cur_home_lineup_info.stats['FTA']+=1
							cur_home_lineup_info.stats['FTm']+=1
							break 

					if(home_found == False):
						cur_home_lineup_info.stats['Oppo_FTA']+=1
						cur_home_lineup_info.stats['Oppo_FTm']+=1

					for p in cur_away_lineup.players:
						if(p.player_stats['Player_Name'] == name_fta):
							print('found a away player who missed freethrow!')
							p.player_stats['FTA']+=1
							p.player_stats['FTm']+=1
							away_found = True
							cur_away_lineup_info.stats['FTA']+=1
							cur_away_lineup_info.stats['FTm']+=1
							break 

					if(away_found == False):
						cur_away_lineup_info.stats['Oppo_FTA']+=1
						cur_away_lineup_info.stats['Oppo_FTm']+=1

				# ----------------------------------Asist ---------------------------------------------------------------------------------------#

				if(assist.search(line) is not None):
					assist_name = assist.search(line).group(2).capitalize() + ' ' +assist.search(line).group(1).split(',')[0].split(' ')[0].capitalize()  # convert all uppercase name to normal format name
					home_found = False
					away_found = False
					if(player_scored in self.home_team_rosters):
						for p in cur_home_lineup.players:
							if(p.player_stats['Player_Name'] == assist_name):
								home_found = True
								p.player_stats['Ast']+=1
								p.pass_to(player_scored)
								cur_home_lineup_info.stats['Ast']+=1
								break
					if(home_found == False):
						cur_home_lineup_info.stats['Oppo_Ast']+=1
					
					if(player_scored in self.away_team_rosters):
						for p in cur_away_lineup.players:
							if(p.player_stats['Player_Name'] == assist_name):
								away_found = True
								p.player_stats['Ast']+=1
								p.pass_to(player_scored)
								cur_away_lineup_info.stats['Ast']+=1
								break
					if(away_found == False):
						cur_away_lineup_info.stats['Oppo_Ast']+=1

			   # ------------------------------------Steal-----------------------------------------------------------------------------------------#
		
				if(steal.search(line) is not None):
					steal_name =steal.search(line).group(2).capitalize() + ' ' +steal.search(line).group(1).split(',')[0].split(' ')[0].capitalize()  # convert all uppercase name to normal format name
					home_found = False
					away_found = False
					for p in cur_home_lineup.players:
						if(p.player_stats['Player_Name'] == steal_name):
							p.player_stats['Stl']+=1
							home_found = True
							cur_home_lineup_info.stats['Stl']+=1
							break 
					if(home_found == False):
						cur_home_lineup_info.stats['Oppo_Stl']+=1

					for p in cur_away_lineup.players:
						if(p.player_stats['Player_Name'] == steal_name):
							p.player_stats['Stl']+=1
							away_found = True
							cur_away_lineup_info.stats['Stl']+=1
							break 
					if(away_found == False):
						cur_away_lineup_info.stats['Oppo_Stl']+=1

				if(turnover.search(line) is not None):
					turnover_name =turnover.search(line).group(2).capitalize() + ' ' +turnover.search(line).group(1).split(',')[0].split(' ')[0].capitalize()  # convert all uppercase name to normal format name
					home_found = False
					away_found = False
					for p in cur_home_lineup.players:
						if(p.player_stats['Player_Name'] == turnover_name):
							p.player_stats['Turnover']+=1
							home_found = True
							cur_home_lineup_info.stats['Turnover']+=1
							break 
					if(home_found == False):
						cur_home_lineup_info.stats['Oppo_Turnover']+=1

					for p in cur_away_lineup.players:
						if(p.player_stats['Player_Name'] == turnover_name):
							p.player_stats['Turnover']+=1
							away_found = True
							cur_away_lineup_info.stats['Turnover']+=1
							break 
					if(away_found == False):
						cur_away_lineup_info.stats['Oppo_Turnover']+=1

				if(block.search(line) is not None):
					block_name =block.search(line).group(2).capitalize() + ' ' +block.search(line).group(1).split(',')[0].split(' ')[0].capitalize()  # convert all uppercase name to normal format name
					home_found = False
					away_found = False
					for p in cur_home_lineup.players:
						if(p.player_stats['Player_Name'] == block_name):
							p.player_stats['Block']+=1
							home_found = True
							cur_home_lineup_info.stats['Block']+=1
							break 
					if(home_found == False):
						cur_home_lineup_info.stats['Oppo_Block']+=1

					for p in cur_away_lineup.players:
						if(p.player_stats['Player_Name'] == block_name):
							p.player_stats['Block']+=1
							away_found = True
							cur_away_lineup_info.stats['Block']+=1
							break 
					if(away_found == False):
						cur_away_lineup_info.stats['Oppo_Block']+=1

				if(foul.search(line) is not None):
					foul_name =foul.search(line).group(2).capitalize() + ' ' +foul.search(line).group(1).split(',')[0].split(' ')[0].capitalize()  # convert all uppercase name to normal format name
					home_found = False
					away_found = False
					for p in cur_home_lineup.players:
						if(p.player_stats['Player_Name'] == foul_name):
							p.player_stats['Foul']+=1
							home_found = True
							cur_home_lineup_info.stats['Foul']+=1
							break 
					if(home_found == False):
						cur_home_lineup_info.stats['Oppo_Foul']+=1

					for p in cur_away_lineup.players:
						if(p.player_stats['Player_Name'] == foul_name):
							p.player_stats['Foul']+=1
							away_found = True
							cur_away_lineup_info.stats['Foul']+=1
							break 
					if(away_found == False):
						cur_away_lineup_info.stats['Oppo_Foul']+=1


			
			for lineup_info in self.home_team_obj.lineup_stats:
				if(lineup_info.stats['Min']==None):
					lineup_info.stats['Min']=lineup_info.stats['From']

			for lineup_info in self.away_team_obj.lineup_stats:
				if(lineup_info.stats['Min']==None):
					lineup_info.stats['Min']=lineup_info.stats['From']


