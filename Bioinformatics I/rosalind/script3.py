file = open("rosalind_revc.txt", 'r')
temp = ''
for line in file:
	print line
	line = line[::-1]
	for letter in line:
		if letter == 'A':
			temp+='T'
		elif letter == 'T':
			temp+='A'
		if letter == 'G':
			temp+='C'
		if letter == 'C':
			temp+='G'

print temp
