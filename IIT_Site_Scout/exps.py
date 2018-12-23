import re


line = '16:09	Assist by MOSLEY JR.,PARKER made layup	3 - 6	'
line1 = '08:30	 	12 - 17	GRAEBNER,KYLE made free throw  Benedictine (Ill.)'

assist = re.compile(r'Assist by ([A-Z]+ {0,1}?[A-Z]+)\.?\,([A-Z]+)')
two_made = re.compile(r'([A-Z]+ {0,1}?[A-Z]+)\.?\,([A-Z]+) made (jump shot|layup)')
freethrow_made = re.compile(r'([A-Z]+ {0,1}?[A-Z]+)\.?\,([A-Z]+) made free throw')


# print(assist.search(line).groups())
# print(assist.search(line).group(2))
# print(assist.search(line).group(1))


name = two_made.search(line).group(2).capitalize() + ' ' +two_made.search(line).group(0).split(',')[0].split(' ')[0].capitalize()  # convert all uppercase name to normal format name
assist_name = assist.search(line).group(2).capitalize() + ' ' +assist.search(line).group(1).split(',')[0].split(' ')[0].capitalize()  # convert all uppercase name to normal format name
name_fga= freethrow_made.search(line1).group(2).capitalize() + ' ' +freethrow_made.search(line1).group(0).split(',')[0].split(' ')[0].capitalize()  # convert all uppercase name to normal format name





# print(assist_name)

# print(two_made.search(line).groups())
# print(name)

# print(assist_name)

print(name_fga)
print(freethrow_made.search(line1).groups())
