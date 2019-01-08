import re


player_number = re.compile(r'\#[0-9][0-9]? ([A-Z][a-z]+ [A-Z][a-z]+)')
percentage = re.compile(r'([1]?[0-9][0-9]\.?[0-9])\%')


# line = '#42 Jonathan Turner III	5	3.4	1.18	0.35	2	0.2	0.2	1	0.2	0	0	0.6	0.2	0.4'
line1 = '53.8%'


print(float(percentage.search(line1).group(1)))
# print(player_number.search(line).group(1)) 