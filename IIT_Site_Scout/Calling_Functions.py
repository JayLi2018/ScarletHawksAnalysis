import Core
from Core import *


file_loc = '/home/chenjie/Desktop/ScarletHawksAnalysis/IIT_Site_Scout/Games_Raw/'
output_dir = '/home/chenjie/Desktop/ScarletHawksAnalysis/IIT_Site_Scout/CSVs/GAME_CSVs/'
game_name = 'Benedictine'

Benedictine_lineup = ['Kenny Bogus','Eric Grygo','Bryan Jacobsze','Jaquan Phipps','Kyle Graebner']

IIT_lineup = ['Jake Digiorgio','Milos Dugalic','Max Hisatake','Anthony Mosley','Ahmad Muhammad']

IIT_against_Dominican_Lineup = ['Jake Digiorgio','Milos Dugalic','Parker Joncus','Anthony Mosley','Ahmad Muhammad']

IIT_against_MSOE_Lineup = ['Jake Digiorgio','Milos Dugalic','Parker Joncus','Anthony Mosley','Ahmad Muhammad']

IIT_against_Lakeland_Lineup = ['Jake Digiorgio','Max Hisatake','Parker Joncus','Anthony Mosley','Ahmad Muhammad']

IIT_against_Concordia_Wis_Lineup = ['Jake Digiorgio','Max Hisatake','Parker Joncus','Anthony Mosley','Ahmad Muhammad']

Aurora_lineup = ['Jarek Hotwagner','Bailey Vance','Ty Carlson','Matt Dunn','Brandon James']

Dominican_lineup = ['Jackson Smith','Derek Steck','Braquan Echols','Dennis Handy','Andrew Wojcik']

MSOE_lineup =['Jake Gebert','Travis Ballard','Anthony Bartman','Jason Palesse','Matthew Kirmse']

Lakeland_lineup = ['Garrett Duffin','Eric Nygaard','Jequan Pegeese','Shakur Jinad','Don Joachim']

Concordia_Wis_Lineup = ['George Olalekan','Andrew Fratzke','Jake Jurss','Jordan Johnson','Josh Hau']


game_1 = DataExtractor(Game_ID=1,home_team='Benedictine (IL) Eagles',home_first_lineup=Benedictine_lineup,
	away_team='Illinois Tech Scarlet Hawks',away_first_lineup=IIT_lineup,game_file_loc=file_loc,output_loc=output_dir)
game_1.generate_data(game_name='Benedictine')
game_1.outputs()


game_2 = DataExtractor(Game_ID=2,home_team='Illinois Tech Scarlet Hawks',home_first_lineup=IIT_lineup,
	away_team='Aurora University',away_first_lineup=Aurora_lineup,game_file_loc=file_loc,output_loc=output_dir)
game_2.generate_data(game_name='Aurora')
game_2.outputs()


game_3 = DataExtractor(Game_ID=3,home_team='Illinois Tech Scarlet Hawks',home_first_lineup=IIT_against_Dominican_Lineup,
	away_team='Dominican (IL) Stars',away_first_lineup=Dominican_lineup,game_file_loc=file_loc,output_loc=output_dir)
game_3.generate_data(game_name='Dominican')
game_3.outputs()


game_4 = DataExtractor(Game_ID=4,home_team='Milwaukee School of Engineering',home_first_lineup=MSOE_lineup,
	away_team='Illinois Tech Scarlet Hawks',away_first_lineup=IIT_against_MSOE_Lineup,game_file_loc=file_loc,output_loc=output_dir)
game_4.generate_data(game_name='MSOE')
game_4.outputs()


game_5 = DataExtractor(Game_ID=5,home_team='Illinois Tech Scarlet Hawks',home_first_lineup=IIT_against_Lakeland_Lineup,
	away_team='Lakeland (WI) Muskies',away_first_lineup=Lakeland_lineup,game_file_loc=file_loc,output_loc=output_dir)
game_5.generate_data(game_name='Lakeland')
game_5.outputs()


game_6 = DataExtractor(Game_ID=6,home_team='Concordia (WI) Falcons',home_first_lineup=Concordia_Wis_Lineup,
	away_team='Illinois Tech Scarlet Hawks',away_first_lineup=IIT_against_Concordia_Wis_Lineup,game_file_loc=file_loc,output_loc=output_dir)
game_6.generate_data(game_name='Concordia_Wis')
game_6.outputs()
