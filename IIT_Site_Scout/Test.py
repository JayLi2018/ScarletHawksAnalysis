import Core
from Core import *


file_loc = '/home/chenjie/Desktop/PBP_NEW/IIT_Site_Scout/Games/'

game_name = 'Benedictine'

Benedictine_lineup = ['Kenny Bogus','Eric Grygo','Bryan Jacobsze','Jaquan Phipps','Kyle Graebner']

IIT_lineup = ['Jake Digiorgio','Milos Dugalic','Max Hisatake','Anthony Mosley','Ahmad Muhammad']


game_extractor = DataExtractor(home_team='Benedictine',home_first_lineup=Benedictine_lineup,away_team='IllinoisTech',away_first_lineup=IIT_lineup,game_file_loc=file_loc,output_loc=file_loc)
game_extractor.generate_data(game_name='Benedictine')
game_extractor.outputs()


# test_process = FileProcessor('/home/chenjie/Desktop/PBP_NEW/IIT_Site_Scout/Games/Benedictine')
# test_process.process_and_output()
