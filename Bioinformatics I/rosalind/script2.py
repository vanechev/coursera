import string as str
file = open("rosalind_rna.txt", 'r')

for line in file:
	line = str.replace(line,"T","U")
	print line