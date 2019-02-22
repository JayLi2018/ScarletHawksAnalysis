import Core
from Core import *


file_loc = '/home/chenjie/Desktop/ScarletHawksAnalysis/codes_and_raw_files/All_Games_Raw/'
output_dir = '/home/chenjie/Desktop/ScarletHawksAnalysis/codes_and_raw_files/All_Games_Raw/'

Benedictine_lineup = ['Kenny Bogus','Eric Grygo','Bryan Jacobsze','Michael Johnson','Kyle Graebner']

IIT_lineup = ['Jake Digiorgio','Otis Reale','Milos Dugalic','Calvin Schmitz','Parker Joncus']

IIT_against_Marian = ['Jake Digiorgio','Parker Joncus','Anthony Mosley','Max Hisatake','Ahmad Muhammad']

IIT_against_Concordia_CHI_Lineup = ['Jake Digiorgio','Parker Joncus','Anthony Mosley','Max Hisatake','Ahmad Muhammad']

IIT_against_Edgewood = ['Jake Digiorgio','Parker Joncus','Max Hisatake','Ahmad Muhammad','Otis Reale']

IIT_against_Dominican_Lineup = ['Jake Digiorgio','Milos Dugalic','Parker Joncus','Anthony Mosley','Ahmad Muhammad']

IIT_against_MSOE_Lineup = ['Jake Digiorgio','Max Hisatake','Parker Joncus','Otis Reale','Ahmad Muhammad']

IIT_against_Lakeland_Lineup = ['Jake Digiorgio','Max Hisatake','Parker Joncus','Anthony Mosley','Ahmad Muhammad']

IIT_against_Concordia_Wis_Lineup = ['Jake Digiorgio','Max Hisatake','Parker Joncus','Anthony Mosley','Ahmad Muhammad']

IIT_against_Wis_Lutheran = ['Jake Digiorgio','Max Hisatake','Parker Joncus','Anthony Mosley','Ahmad Muhammad']

IIT_against_Rockford = ['Jake Digiorgio','Parker Joncus','Max Hisatake','Calvin Schmitz','Otis Reale']

Aurora_lineup = ['Jarek Hotwagner','Bailey Vance','Ty Carlson','Matt Dunn','Brandon James']

Dominican_lineup = ['Jackson Smith','Derek Steck','Braquan Echols','Dennis Handy','Andrew Wojcik']

MSOE_lineup =['Jake Gebert','Travis Ballard','Gabe Wear','Jason Palesse','Matthew Kirmse']

Lakeland_lineup = ["Eric Nygaard","Shakur Jinad","Carlos Campos","Pat Mcdonald","Zach Hasenstein"]

Concordia_Wis_Lineup = ['George Olalekan','Andrew Fratzke','Jake Jurss','Jordan Johnson','Josh Hau']

Wis_Lutheran_Lineup = ['Matty Farner','Collin Kennedy','Colin Biesterfeld','Caleb Goldstein','Andrew Bruggink']

Rocford_Lineup = ['Tony Diemer','Kevin Diemer','Jeremiah Stewart','Brandon Emerick','Kivontay Sha']

Marian_Lineup = ['Scott Paulus','Tristan Van','Tyrese Pinson','Tavaris Mccullough','Trentin Fouse']

Concordia_CHI_Lineup = ['Hassan Basbous','Landen Gladney','Mitch Pelissier','Neil Odonnell','Jalen Meeks']

Edgewood_Lineup = ['Ben Seefeld','Emil Radisevic','Mcclain Steffens','Sy Staver','Jake Negus']

Rockford_Lineup = ['Tony Diemer','Kevin Diemer','Jeremiah Stewart','Brandon Emerick','Kivontay Shaw']

IIT_against_Dominican_2 = ['Calvin Schmitz','Otis Reale','Jake Digiorgio','Max Hisatake','Parker Joncus']

Dominican_2_lineup = ['Jackson Smith','Isaac Moore','Connor Dartt','Sean Ek','Dennis Handy']

Edgewood_2_Lineup = ['Ben Seefeld','Emil Radisevic','Mcclain Steffens','Sy Staver','Jake Negus']

IIT_against_Edgewood_2 = ['Calvin Schmitz','Otis Reale','Jake Digiorgio','Max Hisatake','Parker Joncus']

IIT_against_Aurora_2 = ['Calvin Schmitz','Otis Reale','Jake Digiorgio','Max Hisatake','Parker Joncus']

Aurora_lineup_2 = ['Demetrius Pointer','Max Vickers','Brandon James','Marquis Howard','Ty Carlson']

Concordia_Wis_Lineup_2 = ['Andrew Fratzke','Josh Hau','Jared Jurss','Jake Jurss','Jordan Johnson']

IIT_against_Concordia_Wis_Lineup_2 = ['Milos Dugalic','Parker Joncus','Max Hisatake','Otis Reale','Calvin Schmitz']

Wis_Lutheran_Lineup_2 = ['Matty Farner','Collin Kennedy','Colin Biesterfeld','Caleb Goldstein','Bruggink Andrew']

IIT_against_Lutheran_2 = ['Calvin Schmitz','Otis Reale','Jake Digiorgio','Max Hisatake','Parker Joncus']

Rockford_Lineup_2 = ['Tony Diemer','Kevin Diemer','Brandon Emerick','Will Adams','Kivontay Shaw']

IIT_against_Rockford_2 = ['Jake Bruns','Otis Reale','Jake Digiorgio','Max Hisatake','Parker Joncus']


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


# game_8 = DataExtractor(Game_ID=8,home_team='Lakeland (WI) Muskies',home_first_lineup=Lakeland_lineup,
# 	away_team='Illinois Tech Scarlet Hawks',away_first_lineup=IIT_against_Lakeland_Lineup,game_file_loc=file_loc,output_loc=output_dir)
# game_8.generate_data(game_name='Lakeland')
# game_8.outputs()

# game_9 = DataExtractor(Game_ID=9,home_team='Illinois Tech Scarlet Hawks',home_first_lineup=IIT_against_Marian,
# 	away_team='Marian University (WI) Sabres',away_first_lineup=Marian_Lineup,game_file_loc=file_loc,output_loc=output_dir)
# game_9.generate_data(game_name='Marian')
# game_9.outputs()

# game_10 = DataExtractor(Game_ID=10,home_team='Concordia (Chicago) Cougars',home_first_lineup=Concordia_CHI_Lineup,
# 	away_team='Illinois Tech Scarlet Hawks',away_first_lineup=IIT_against_Concordia_CHI_Lineup,game_file_loc=file_loc,output_loc=output_dir)
# game_10.generate_data(game_name='Concordia_Chicago')
# game_10.outputs()

game_11 = DataExtractor(Game_ID=11,home_team='Illinois Tech Scarlet Hawks',home_first_lineup=IIT_against_MSOE_Lineup,
	away_team='Milwaukee School of Engineering',away_first_lineup=MSOE_lineup,game_file_loc=file_loc,output_loc=output_dir)
game_11.generate_data(game_name='MSOE_2')
game_11.outputs()


# game_12 = DataExtractor(Game_ID=12,home_team='Edgewood College (WI) Eagles',home_first_lineup=Edgewood_Lineup,
# 	away_team='Illinois Tech Scarlet Hawks',away_first_lineup=IIT_against_Edgewood,game_file_loc=file_loc,output_loc=output_dir)
# game_12.generate_data(game_name='Edgewood')
# game_12.outputs()


# game_13 = DataExtractor(Game_ID=13,home_team='Illinois Tech Scarlet Hawks',home_first_lineup=IIT_lineup,
# 	away_team='Benedictine (IL) Eagles',away_first_lineup=Benedictine_lineup,game_file_loc=file_loc,output_loc=output_dir)
# game_13.generate_data(game_name='Benedictine')
# game_13.outputs()


# game_14 = DataExtractor(Game_ID=14,home_team='Rockford Regents',home_first_lineup=Rockford_Lineup,
# 	away_team='Illinois Tech Scarlet Hawks',away_first_lineup=IIT_against_Rockford,game_file_loc=file_loc,output_loc=output_dir)
# game_14.generate_data(game_name='Rockford_1')
# game_14.outputs()

# game_15 = DataExtractor(Game_ID=15,home_team='Dominican (IL) Stars',home_first_lineup=Dominican_2_lineup,
# 	away_team='Illinois Tech Scarlet Hawks',away_first_lineup=IIT_against_Dominican_2,game_file_loc=file_loc,output_loc=output_dir)
# game_15.generate_data(game_name='Dominican_2')
# game_15.outputs()

# game_16 = DataExtractor(Game_ID=16,home_team='Illinois Tech Scarlet Hawks',home_first_lineup=IIT_against_Edgewood_2,
# 	away_team='Edgewood College (WI) Eagles', away_first_lineup=Edgewood_2_Lineup,game_file_loc=file_loc,output_loc=output_dir)
# game_16.generate_data(game_name='Edgewood_2')
# game_16.outputs()

# game_17 = DataExtractor(Game_ID=17,home_team='Aurora University',home_first_lineup=Aurora_lineup_2,
# 	away_team='Illinois Tech Scarlet Hawks',away_first_lineup=IIT_against_Aurora_2,game_file_loc=file_loc,output_loc=output_dir)
# game_17.generate_data(game_name='Aurora_2')
# game_17.outputs()

# game_18 = DataExtractor(Game_ID=18,home_team='Illinois Tech Scarlet Hawks',home_first_lineup=IIT_against_Concordia_Wis_Lineup_2,
# 	away_team='Concordia (WI) Falcons',away_first_lineup=Concordia_Wis_Lineup_2,game_file_loc=file_loc,output_loc=output_dir)
# game_18.generate_data(game_name='Concordia_Wis_2')
# game_18.outputs()

# game_19 = DataExtractor(Game_ID=19,home_team='Illinois Tech Scarlet Hawks',home_first_lineup=IIT_against_Lutheran_2,
# 	away_team='Wisconsin Lutheran Warriors',away_first_lineup=Wis_Lutheran_Lineup_2,game_file_loc=file_loc,output_loc=output_dir)
# game_19.generate_data(game_name='Lutheran_Wis_2')
# game_19.outputs()

# game_20 = DataExtractor(Game_ID=20,home_team='Illinois Tech Scarlet Hawks',home_first_lineup=IIT_against_Rockford_2,
# 	away_team='Rockford Regents',away_first_lineup=Rockford_Lineup_2,game_file_loc=file_loc,output_loc=output_dir)
# game_20.generate_data(game_name='Rockford_2')
# game_20.outputs()


