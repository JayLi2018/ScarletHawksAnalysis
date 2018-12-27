import re



tab = re.compile(r'(\t+)')
line = 'Miscellaneous	7.5%	6.2	2.2	0.363	78%	Very Good	0.5	0.4	0.8	45.5%	50%	61.3%	25%	1.3%	22.5%'
line2 = ' Offense Including Passes                            ' 
# print(tab.search(line).groups())
print(line2.strip())