import Core
from Core import *


file_loc = '/home/chenjie/Desktop/ScarletHawksAnalysis/codes_and_raw_files/1.15 Package/Game_Raw/'
output_dir = '/home/chenjie/Desktop/ScarletHawksAnalysis/codes_and_raw_files/1.15 Package/Game_CSVs/'

Benedictine_lineup = ['Kenny Bogus','Eric Grygo','Bryan Jacobsze','Jaquan Phipps','Kyle Graebner']

IIT_lineup = ['Jake Digiorgio','Milos Dugalic','Max Hisatake','Anthony Mosley','Ahmad Muhammad']

IIT_against_Dominican_Lineup = ['Jake Digiorgio','Milos Dugalic','Parker Joncus','Anthony Mosley','Ahmad Muhammad']

IIT_against_MSOE_Lineup = ['Jake Digiorgio','Milos Dugalic','Parker Joncus','Anthony Mosley','Ahmad Muhammad']

IIT_against_Lakeland_Lineup = ['Jake Digiorgio','Max Hisatake','Parker Joncus','Anthony Mosley','Ahmad Muhammad']

IIT_against_Concordia_Wis_Lineup = ['Jake Digiorgio','Max Hisatake','Parker Joncus','Anthony Mosley','Ahmad Muhammad']

IIT_against_Wis_Lutheran = ['Jake Digiorgio','Max Hisatake','Parker Joncus','Anthony Mosley','Ahmad Muhammad']

Aurora_lineup = ['Jarek Hotwagner','Bailey Vance','Ty Carlson','Matt Dunn','Brandon James']

Dominican_lineup = ['Jackson Smith','Derek Steck','Braquan Echols','Dennis Handy','Andrew Wojcik']

MSOE_lineup =['Jake Gebert','Travis Ballard','Anthony Bartman','Jason Palesse','Matthew Kirmse']

Lakeland_lineup = ["Eric Nygaard","Shakur Jinad","Carlos Campos","Pat Mcdonald","Zach Hasenstein"]

Concordia_Wis_Lineup = ['George Olalekan','Andrew Fratzke','Jake Jurss','Jordan Johnson','Josh Hau']

Wis_Lutheran_Lineup = ['Matty Farner','Collin Kennedy','Colin Biesterfeld','Caleb Goldstein','Andrew Bruggink']

# game_1 = DataExtractor(Game_ID=1,home_team='Benedictine (IL) Eagles',home_first_lineup=Benedictine_lineup,
# 	away_team='Illinois Tech Scarlet Hawks',away_first_lineup=IIT_lineup,game_file_loc=file_loc,output_loc=output_dir)
# game_1.generate_data(game_name='Benedictine')
# game_1.outputs()


# game_2 = DataExtractor(Game_ID=2,home_team='Illinois Tech Scarlet Hawks',home_first_lineup=IIT_lineup,
# 	away_team='Aurora University',away_first_lineup=Aurora_lineup,game_file_loc=file_loc,output_loc=output_dir)
# game_2.generate_data(game_name='Aurora')
# game_2.outputs()


# game_3 = DataExtractor(Game_ID=3,home_team='Illinois Tech Scarlet Hawks',home_first_lineup=IIT_against_Dominican_Lineup,
# 	away_team='Dominican (IL) Stars',away_first_lineup=Dominican_lineup,game_file_loc=file_loc,output_loc=output_dir)
# game_3.generate_data(game_name='Dominican')
# game_3.outputs()


# game_4 = DataExtractor(Game_ID=4,home_team='Milwaukee School of Engineering',home_first_lineup=MSOE_lineup,
# 	away_team='Illinois Tech Scarlet Hawks',away_first_lineup=IIT_against_MSOE_Lineup,game_file_loc=file_loc,output_loc=output_dir)
# game_4.generate_data(game_name='MSOE')
# game_4.outputs()


# game_5 = DataExtractor(Game_ID=5,home_team='Illinois Tech Scarlet Hawks',home_first_lineup=IIT_against_Lakeland_Lineup,
# 	away_team='Lakeland (WI) Muskies',away_first_lineup=Lakeland_lineup,game_file_loc=file_loc,output_loc=output_dir)
# game_5.generate_data(game_name='Lakeland')
# game_5.outputs()


# game_6 = DataExtractor(Game_ID=6,home_team='Concordia (WI) Falcons',home_first_lineup=Concordia_Wis_Lineup,
# 	away_team='Illinois Tech Scarlet Hawks',away_first_lineup=IIT_against_Concordia_Wis_Lineup,game_file_loc=file_loc,output_loc=output_dir)
# game_6.generate_data(game_name='Concordia_Wis')
# game_6.outputs()


# game_7 = DataExtractor(Game_ID=7,home_team='Wisconsin Lutheran Warriors',home_first_lineup=Wis_Lutheran_Lineup,
# 	away_team='Illinois Tech Scarlet Hawks',away_first_lineup=IIT_against_Wis_Lutheran,game_file_loc=file_loc,output_loc=output_dir)
# game_7.generate_data(game_name='Lutheran_Wis')
# game_7.outputs()


game_8 = DataExtractor(Game_ID=8,home_team='Lakeland (WI) Muskies',home_first_lineup=Lakeland_lineup,
	away_team='Illinois Tech Scarlet Hawks',away_first_lineup=IIT_against_Lakeland_Lineup,game_file_loc=file_loc,output_loc=output_dir)
game_8.generate_data(game_name='Lakeland')
game_8.outputs()