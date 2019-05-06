import re
import os


uppercase_name = re.compile(r'([A-Z]+)\,([A-Z]+)')
uppercase_name_suffix = re.compile(r'([A-Z]+) JR\.?\,([A-Z]+)')
player_movement_out = re.compile(r'([A-Z]+ {0,1}?[A-Z]+)\.?\,([A-Z]+) goes to the bench')


timer = re.compile(r'([0-9][0-9])\:([0-5][0-9])')
player_out = re.compile(r'([A-Z]+ {0,1}?[A-Z]+)\,([A-Z]+) goes to the bench')
player_in = re.compile(r'([A-Z]+ {0,1}?[A-Z]+)\,([A-Z]+) enters the game')
half = re.compile(r'Half [0-9]')

line1 = ' MOSLEY,ANTHONY goes to the bench'


# print(uppercase_name.search(line).groups())
# print(uppercase_name_suffix.search(line1).groups())
# print(player_movement_out.search(line1).group(1).split(' ')[0])


# print(uppercase_name.search(line).group(0).split(',')[1].capitalize() + ' ' +uppercase_name.search(line).group().split(',')[0].capitalize())

# print(uppercase_name_suffix.search(line1).group(2).capitalize() + ' ' +uppercase_name_suffix.search(line1).group(1).capitalize())


def get_time(line):  # change time to float format so that it's easier to compare between times
	timer = re.compile(r'([0-9][0-9])\:([0-5][0-9])')
	match = timer.search(line)
	if match:
		return (float(match.group(1)) + float(match.group(2))/60)

def get_movement(line):

	sub_in_match = player_in.search(line)
	sub_out_match = player_out.search(line)

	if(sub_in_match):
		return 1
	elif(sub_out_match):
		return 0


class FileProcessor:

	def __init__(self,file_dir):
		self.file_dir = file_dir # input file directory here



	def process_file(self):
		
		self.raw_file = open(self.file_dir,'r')
		self.raw_file_list = []

		cur_list = []
		lists = []
		self.sub_buffer = []

		self.first_list = []  # list of lists


		# self.processed_file = open(self.file_dir+'_processed',"a+")
		self.processed_file = []

		cur_time = 20.0
		
		first_list = []
		cur_list = first_list
		lists.append(first_list)

		for line in self.raw_file:
			if(timer.search(line)==None):
				continue
			elif(get_time(line)<=cur_time):
				cur_list.append(line)
				cur_time = get_time(line)
			else:
				new_list = []
				cur_list = new_list
				cur_time = get_time(line)
				new_list.append(line)
				lists.append(new_list)

		for list in lists:  # this part is used for sorting "sub in" and "sub out"
			sorted_sublist = []
			n=0
			for line in list:
				# print("now processing line" + str(n))
				if(half.search(line) is not None):
					sorted_sublist.append(line)
				if((player_in.search(line) is None) and (player_out.search(line) is None)):
					if(len(self.sub_buffer)>=1):
						self.sub_buffer.sort(key = get_movement, reverse = True)
						# print("length of buffer beofre sorting: "+str(len(self.sub_buffer)))
						# print(self.sub_buffer)
						for m in self.sub_buffer:
							sorted_sublist.append(m)
						del self.sub_buffer[:]
						sorted_sublist.append(line)
						n +=1
					else:
						sorted_sublist.append(line)
						n +=1
				else:
					self.sub_buffer.append(line)
					n +=1
			self.processed_file.append(sorted_sublist)  

		print('processed_file has '+str(len(self.processed_file))+' sub sorted list')	
		return self.processed_file	
		
	def process_and_output(self):

		self.raw_file = open(self.file_dir,'r')
		self.raw_file_list = []

		cur_list = []
		lists = []
		self.sub_buffer = []

		self.first_list = []  # list of lists

		cur_time = 20.0
		output_file = open(self.file_dir+'_processed',"a+")

		first_list = []
		cur_list = first_list
		lists.append(first_list)

		for line in self.raw_file:
			if(timer.search(line)==None):
				continue
			elif(get_time(line)<=cur_time):
				cur_list.append(line)
				cur_time = get_time(line)
			else:
				new_list = []
				cur_list = new_list
				cur_time = get_time(line)
				new_list.append(line)
				lists.append(new_list)
		
		for list in lists:  # this part is used for sorting "sub in" and "sub out"
			sorted_sublist = []
			n=0
			for line in list:
				# print("now processing line" + str(n))
				if(half.search(line) is not None):
					output_file.write("%s" % line)
				if((player_in.search(line) is None) and (player_out.search(line) is None)):
					if(len(self.sub_buffer)>=1):
						self.sub_buffer.sort(key = get_movement, reverse = True)
						# print("length of buffer beofre sorting: "+str(len(self.sub_buffer)))
						# print(self.sub_buffer)
						for m in self.sub_buffer:
							output_file.write("%s" % m)
						del self.sub_buffer[:]
						output_file.write("%s" % line)
						n +=1
					else:
						output_file.write("%s" % line)
						n +=1
				else:
					self.sub_buffer.append(line)
					n +=1 


# if __name__ == '__main__':
# 	processor = FileProcessor('/home/chenjie/Desktop/PBP_NEW/IIT_Site_Scout/Trine')
# 	processor.process_file()



	

	




