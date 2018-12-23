import re
import os
from Classes import Team,Player,Lineup,Lineup_Stats,Score_Tracker
import File_Processor
from File_Processor import FileProcessor
from Rosters import Team_Lists
from copy import deepcopy
import pandas as pd

# this is the lineup stats generator

# list of regexes:
first_half = re.compile(r'1 Half')
second_half = re.compile(r'2 Half')
over_time = re.compile(r'3 Half')
off_reb = re.compile(r'([A-Z]+ {0,1}?[A-Z]+)\.?\,([A-Z]+) offensive rebound')
def_reb = re.compile(r'([A-Z]+ {0,1}?[A-Z]+)\.?\,([A-Z]+) defensive rebound')
shot_attempt = re.compile(r'([A-Z]+ {0,1}?[A-Z]+)\.?\,([A-Z]+) .* (jump shot|layup)')
two_made = re.compile(r'([A-Z]+ {0,1}?[A-Z]+)\.?\,([A-Z]+) made (jump shot|layup)')
two_missed = re.compile(r'([A-Z]+ {0,1}?[A-Z]+)\.?\,([A-Z]+) missed (jump shot|layup)')
three_made = re.compile(r'([A-Z]+ {0,1}?[A-Z]+)\.?\,([A-Z]+) made 3-pt\.')
three_miss = re.compile(r'([A-Z]+ {0,1}?[A-Z]+)\.?\,([A-Z]+) missed 3-pt\.')
freethrow_made = re.compile(r'([A-Z]+ {0,1}?[A-Z]+)\.?\,([A-Z]+) made free throw')
freethrow_miss =re.compile(r'([A-Z]+ {0,1}?[A-Z]+)\.?\,([A-Z]+) missed free throw') 
assist = re.compile(r'Assist by ([A-Z]+ {0,1}?[A-Z]+)\.?\,([A-Z]+)')
steal = re.compile(r'Steal by ([A-Z]+ {0,1}?[A-Z]+)\.?\,([A-Z]+)')
player_movement_out = re.compile(r'([A-Z]+ {0,1}?[A-Z]+)\.?\,([A-Z]+) goes to the bench')
player_movement_in = re.compile(r'([A-Z]+ {0,1}?[A-Z]+)\.?\,([A-Z]+) enters the game')
timer = re.compile(r'([0-9][0-9])\:([0-5][0-9])')


class DataExtractor(object):


	def __init__(self,game_file_loc=None,output_loc=None,
		home_team=None,away_team=None,
		home_first_lineup = None,away_first_lineup = None,
		home_second_lineup = None, away_second_lineup = None,
		home_ot_lineup = None, away_ot_lineup = None,
		**kwargs):
		
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
		self.home_team_rosters=[]
		self.away_team_rosters=[]
		self.home_score=0
		self.away_score=0
		
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
		
		game_file = self.game_file_loc+game_name

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
		# home_lineup_stats_dicts = []
		# for n in self.home_team_obj.lineup_stats:
		# 	df = pd.DataFrame(n.stats,index=[0])
		# 	home_lineup_stats_dicts.append(df)
		# home_lineup_stats_df = pd.concat(home_lineup_stats_dicts)
		# home_lineup_stats_df.to_csv('test_home_df.csv',index=None)

		# away_lineup_stats_dicts = []
		# for n in self.away_team_obj.lineup_stats:
		# 	df = pd.DataFrame(n.stats,index=[0])
		# 	away_lineup_stats_dicts.append(df)
		# away_lineup_stats_df = pd.concat(away_lineup_stats_dicts)
		# away_lineup_stats_df.to_csv('test_away_df.csv',index=None)
		
		tracker_df = pd.DataFrame(self.score_track.tracker)
		print(tracker_df)

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
			home_lineup_info = Lineup_Stats(session_num)
			home_lineup_info.stats['From'] = cur_time
			home_lineup_info.stats['session_number'] = session_num					
			for player_name in home_session_start_lineup:
				p = Player(Team_Name=self.home_team,Player_Name=player_name)
				home_lineup.players.append(p)
			self.home_team_obj.lineups.append(deepcopy(home_lineup))
			
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
			away_lineup_info = Lineup_Stats(session_num)
			away_lineup_info.stats['From'] = cur_time
			away_lineup_info.stats['session_number'] = session_num		
			for player_name in away_session_start_lineup:
				p = Player(Team_Name=self.away_team,Player_Name=player_name)
				away_lineup.players.append(p)
			self.away_team_obj.lineups.append(deepcopy(away_lineup))
			
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
						# print(player)
						if(player in self.home_team_rosters):					
							for n in self.home_team_rosters:
								if(n == player):
									player_in = Player(Team_Name=self.home_team,Player_Name=n)
									home_sub_in_buffer.append(player_in) # sub_in_buffer contains player objects
									# print("Time: "+str(self.get_time(line)) + " " + player + " in! sub_in buffer size "+str(len(iit_sub_in_buffer)))

						elif(player in self.away_team_rosters):					
							for n in self.away_team_rosters:
								if(n == player):
									player_in = Player(Team_Name=self.away_team,Player_Name=n)
									away_sub_in_buffer.append(player_in) # sub_in_buffer contains player objects
									# print("Time: "+str(self.get_time(line)) + " " + player + " in! sub_in buffer size "+str(len(iit_sub_in_buffer)))


				if(player_movement_out.search(line) is not None or player_movement_out.search(line) is not None):
					if(player_movement_out.search(line) is not None):
						player = player_movement_out.search(line).group(2).capitalize() + ' ' +player_movement_out.search(line).group(0).split(',')[0].split(' ')[0].capitalize()  # convert all uppercase name to normal format name
						# print(player)
						if(player in self.home_team_rosters):					
							for n in self.home_team_rosters:
								if(n == player):
									player_out = Player(Team_Name=self.home_team,Player_Name=n)
									home_sub_out_buffer.append(player_out) # sub_out_buffer contains player objects
									# print("Time: "+str(self.get_time(line)) + " " + player + " in! sub_out buffer size "+str(len(iit_sub_out_buffer)))

						elif(player in self.away_team_rosters):					
							for n in self.away_team_rosters:
								if(n == player):
									player_out = Player(Team_Name=self.away_team,Player_Name=n)
									away_sub_out_buffer.append(player_out) # sub_out_buffer contains player objects
									# print("Time: "+str(self.get_time(line)) + " " + player + " in! sub_out buffer size "+str(len(iit_sub_out_buffer)))


					if(bool(len(home_sub_out_buffer)>=1 and len(home_sub_in_buffer)>=1)==True or bool(len(away_sub_out_buffer)>=1 and len(away_sub_in_buffer)>=1)==True):
						if(len(home_sub_out_buffer)>=1 and len(home_sub_in_buffer)>=1):							
							# print("Substitution on ther court! ")
							out_player_name = home_sub_out_buffer[-1].player_stats['Player_Name']
							# print(out_player_name+" goes to the bench")
							# print("Before pop, the size of the sub_out_buffer is "+str(len(iit_sub_out_buffer)))
							home_sub_out_buffer.pop()
							# print("sub_out_buffer pops,now the size of the sub_out_buffer is "+str(len(iit_sub_out_buffer)))
							for n in cur_home_lineup.players:
								if(n.player_stats['Player_Name'] == out_player_name):
									cur_home_lineup.players.remove(n)
									# print("deleted a player! now we have " +str(len(cur_lineup))+" players!")
								else:
									continue
							home_new_lineup = Lineup(session_num)

							for p in cur_home_lineup.players:     # now it's supposed to have 4 players in the lineup
								new_player = Player(Team_Name=self.home_team,Player_Name=p.player_stats['Player_Name']) # create 4 new players with same names since it is a 
																		# new lineup
								home_new_lineup.players.append(new_player)

							home_new_lineup.players.append(home_sub_in_buffer[-1]) # add the sub_in player
							cur_home_lineup = home_new_lineup  # just need to copy, and even though it is a sudo_lineup, it still need to be assigned
							# print("Substitution timing : "+str(self.get_time(line)))
							# print("Current lineup is ")
							# print("\n")
							# print(str(self.get_time(line))+"home cur_lineup: ")
							# for n in cur_home_lineup.players:
							# 	print(n.player_stats['Player_Name'])
							# print("\n")


							# print("Before pop, the size of the sub_in_buffer is "+str(len(iit_sub_in_buffer)))
							home_sub_in_buffer.pop()
							# print("sub_out_buffer pops,now the size of the sub_in_buffer is "+str(len(iit_sub_in_buffer)))

							if(len(home_sub_in_buffer)==0):
								# print("First half ! still Substitution going on!")
								print(str(self.get_time(line))+"Home Team New Lineup:")
								for n in cur_home_lineup.players:
									print(n.player_stats['Player_Name'])
								print('\n')
								self.home_team_obj.lineups.append(deepcopy(cur_home_lineup))

								cur_home_lineup_info.stats['To'] = cur_time
								cur_home_lineup_info.stats['Min'] = cur_home_lineup_info.stats['From'] - cur_home_lineup_info.stats['To'] 
								home_new_lineup_info = Lineup_Stats(session_num)
								home_player_list = []
								for player in cur_home_lineup.players:
									home_player_list.append(player.player_stats['Player_Name'])
								home_player_list.sort()
								home_new_lineup_info.stats['Lineup_Players']= ','.join(home_player_list)

								cur_home_lineup_info = home_new_lineup_info
								home_new_lineup_info.stats['session_number'] = session_num		
								home_new_lineup_info.stats['From'] = cur_time
								self.home_team_obj.lineup_stats.append(home_new_lineup_info)


						if(len(away_sub_out_buffer)>=1 and len(away_sub_in_buffer)>=1):							
							# print("Substitution on ther court! ")
							out_player_name = away_sub_out_buffer[-1].player_stats['Player_Name']
							# print(out_player_name+" goes to the bench")
							# print("Before pop, the size of the sub_out_buffer is "+str(len(iit_sub_out_buffer)))
							away_sub_out_buffer.pop()
							# print("sub_out_buffer pops,now the size of the sub_out_buffer is "+str(len(iit_sub_out_buffer)))
							for n in cur_away_lineup.players:
								if(n.player_stats['Player_Name'] == out_player_name):
									cur_away_lineup.players.remove(n)
									# print("deleted a player! now we have " +str(len(cur_lineup))+" players!")
								else:
									continue
							away_new_lineup = Lineup(session_num)

							for p in cur_away_lineup.players:     # now it's supposed to have 4 players in the lineup
								new_player = Player(Team_Name=self.away_team,Player_Name=p.player_stats['Player_Name']) # create 4 new players with same names since it is a 
																		# new lineup
								away_new_lineup.players.append(new_player)

							away_new_lineup.players.append(away_sub_in_buffer[-1]) # add the sub_in player
							cur_away_lineup = away_new_lineup # just need to copy, and even though it is a sudo_lineup, it still need to be assigned
							# print("Substitution timing : "+str(self.get_time(line)))
							# print("Current lineup is ")
							# print("\n")
							# print(str(self.get_time(line))+"away cur_lineup: ")
							# for n in cur_away_lineup.players:
							# 	print(n.player_stats['Player_Name'])
							# print("\n")


							# print("Before pop, the size of the sub_in_buffer is "+str(len(iit_sub_in_buffer)))
							away_sub_in_buffer.pop()
							# print("sub_out_buffer pops,now the size of the sub_in_buffer is "+str(len(iit_sub_in_buffer)))

							if(len(away_sub_in_buffer)==0):
								# print("First half ! still Substitution going on!")
								print(str(self.get_time(line))+"Away Team New Lineup:")
								for n in cur_away_lineup.players:
									print(n.player_stats['Player_Name'])
								print('\n')
								self.away_team_obj.lineups.append(deepcopy(cur_away_lineup))
								cur_away_lineup_info.stats['To'] = cur_time
								cur_away_lineup_info.stats['Min'] = cur_away_lineup_info.stats['From'] - cur_away_lineup_info.stats['To'] 
								away_new_lineup_info = Lineup_Stats(session_num)
								away_player_list = []
								for player in cur_away_lineup.players:
									away_player_list.append(player.player_stats['Player_Name'])
								away_player_list.sort()
								away_new_lineup_info.stats['Lineup_Players']= ','.join(away_player_list)
								cur_away_lineup_info = away_new_lineup_info
								away_new_lineup_info.stats['From'] = cur_time
								away_new_lineup_info.stats['session_number'] = session_num		
								self.away_team_obj.lineup_stats.append(away_new_lineup_info)

				# ---------------------------------Offensive Rebound -----------------------------------------------------#


				if(off_reb.search(line) is not None):      # Offensive Reb
					print('found a off reb!')
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
						# print('Found an Opponent stat!!!!')
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
						# print('Found an Opponent stat!!!!')
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
						# print('Found an Opponent stat!!!!')
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
						# print('Found an Opponent stat!!!!')
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
								self.score_track.tracker['Score_Dif'].append(cur_score_dif)
								self.score_track.tracker['Time'].append(self.get_time(line))
								player_scored = p.player_stats['Player_Name']
								break 

						if(home_found == False):
							# print('Found an Opponent stat!!!!')
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
								self.score_track.tracker['Score_Dif'].append(cur_score_dif)
								self.score_track.tracker['Time'].append(self.get_time(line))
								player_scored = p.player_stats['Player_Name']
								break 

						if(away_found == False):
							# print('Found an Opponent stat!!!!')
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
							# print('Found an Opponent stat!!!!')
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
							# print('Found an Opponent stat!!!!')
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
								self.score_track.tracker['Score_Dif'].append(cur_score_dif)
								self.score_track.tracker['Time'].append(self.get_time(line))
								player_scored = p.player_stats['Player_Name']
								break 

						if(home_found == False):
							# print('Found an Opponent stat!!!!')
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
								self.score_track.tracker['Score_Dif'].append(cur_score_dif)
								self.score_track.tracker['Time'].append(self.get_time(line))
								player_scored = p.player_stats['Player_Name']
								break 

						if(away_found == False):
							# print('Found an Opponent stat!!!!')
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
							# print('Found an Opponent stat!!!!')
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
							# print('Found an Opponent stat!!!!')
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
							self.score_track.tracker['Score_Dif'].append(cur_score_dif)
							self.score_track.tracker['Time'].append(self.get_time(line))
							break 

					if(home_found == False):
						# print('Found an Opponent stat!!!!')
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
							self.score_track.tracker['Score_Dif'].append(cur_score_dif)
							self.score_track.tracker['Time'].append(self.get_time(line))
							break 

					if(away_found == False):
						# print('Found an Opponent stat!!!!')
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
						# print('Found an Opponent stat!!!!')
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
						# print('Found an Opponent stat!!!!')
						cur_away_lineup_info.stats['Oppo_FTA']+=1
						cur_away_lineup_info.stats['Oppo_FTm']+=1

				# ----------------------------------Asist ---------------------------------------------------------------------------------------#

				if(assist.search(line) is not None):
					assist_name = assist.search(line).group(2).capitalize() + ' ' +assist.search(line).group(1).split(',')[0].split(' ')[0].capitalize()  # convert all uppercase name to normal format name
					home_found = False
					away_found = False
					if(player_scored in self.home_team_rosters):
						# print("found home assist! by "+assist_name)
						for p in cur_home_lineup.players:
							# print("searching!!!!")
							if(p.player_stats['Player_Name'] == assist_name):
								# print("Found assist by home player!" + p.player_stats['Player_Name'] +'at '+str(self.get_time(line)))
								home_found = True
								p.player_stats['Ast']+=1
								p.pass_to(player_scored)
								cur_home_lineup_info.stats['Ast']+=1
								break
					if(home_found == False):
						# print('Found an Opponent stat!!!!')
						cur_home_lineup_info.stats['Oppo_Ast']+=1
					
					if(player_scored in self.away_team_rosters):
						# print("found away assist!by "+assist_name)
						for p in cur_away_lineup.players:
							# print("searching!!!!")
							if(p.player_stats['Player_Name'] == assist_name):
								# print("Found assist by home player!" + p.player_stats['Player_Name'] + 'at '+str(self.get_time(line)) )
								away_found = True
								p.player_stats['Ast']+=1
								p.pass_to(player_scored)
								cur_away_lineup_info.stats['Ast']+=1
								break
					if(away_found == False):
						# print('Found an Opponent stat!!!!')
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
						# print('Found an Opponent stat!!!!')
						cur_home_lineup_info.stats['Oppo_Stl']+=1

					for p in cur_away_lineup.players:
						if(p.player_stats['Player_Name'] == name_fga):
							p.player_stats['Stl']+=1
							away_found = True
							cur_away_lineup_info.stats['Stl']+=1
							break 
					if(away_found == False):
						# print('Found an Opponent stat!!!!')
						cur_away_lineup_info.stats['Oppo_Stl']+=1
			
			for lineup_info in self.home_team_obj.lineup_stats:
				if(lineup_info.stats['Min']==None):
					lineup_info.stats['Min']=lineup_info.stats['From']

			for lineup_info in self.away_team_obj.lineup_stats:
				if(lineup_info.stats['Min']==None):
					lineup_info.stats['Min']=lineup_info.stats['From']


