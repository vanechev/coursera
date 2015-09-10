a =0
g=0
c=0
t=0
file = open("rosalind_dna.txt", 'r')

for line in file:
	for letter in line:
		if letter == 'A':
			a+=1
		elif letter == 'G':
			g+=1
		elif letter == 'C':
			c+=1
		elif letter == 'T':
			t+=1

print a,c,g,t