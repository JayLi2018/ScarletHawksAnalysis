import os
import glob
import re

os.chdir('/home/chenjie/Desktop/ScarletHawksAnalysis/codes_and_raw_files/1.26 Package/Games_CSVs/')


home_lineup_file = open('lineups.csv','a+')
n=1

for file in glob.glob('*_lineups.csv'):
	if(n==1):
		for line in open(file,'r+'):
			home_lineup_file.write(line)
			n+=1
	else:	
		f = open(file,'r+')
		n+=1
		f.next() # skip the header
		for line in f:
			 home_lineup_file.write(line)
		f.close() # not really needed

home_lineup_file.close()


away_player_file = open('player_games.csv','a+')

n=1

for file in glob.glob('*_players.csv'):
	if(n==1):
		for line in open(file,'r+'):
			away_player_file.write(line)
			n+=1
	else:	
		f = open(file,'r+')
		n+=1
		f.next() # skip the header
		for line in f:
			 away_player_file.write(line)
		f.close() # not really needed

away_player_file.close()


tracker_file = open('game_trackers.csv','a+')

n=1

for file in glob.glob('*_tracker.csv'):
	if(n==1):
		for line in open(file,'r+'):
			tracker_file.write(line)
			n+=1
	else:	
		f = open(file,'r+')
		n+=1
		f.next() # skip the header
		for line in f:
			 tracker_file.write(line)
		f.close() # not really needed

tracker_file.close()


