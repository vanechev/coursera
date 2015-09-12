import sys

def complementDNA(line):
	temp = ''
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
	return temp

lines = sys.stdin.read().splitlines() # read in the input from STDIN

Text = lines[0]

print complementDNA(Text)