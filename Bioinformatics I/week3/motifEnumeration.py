# MOTIFENUMERATION(Dna, k, d)
#         Patterns <- an empty set
#         for each k-mer Pattern in Dna
#             for each k-mer Pattern' differing from Pattern by at most d
#              mismatches
#                 if Pattern' appears in each string from Dna with at most d
#              mismatches
#                     add Pattern' to Patterns
#         remove duplicates from Patterns
#         return Patterns
import sys

def intersection(first, *others):
    return set(first).intersection(*others)

def hammingDistance(p,q):
	if len(p) == len(q):
		c = 0
		for i in range(len(p)):
			if p[i] != q[i]:
				c+=1
	return c

def Neighbors(Pattern,d):
	if d == 0:
		return Pattern
	if len(Pattern) == 1:
		return ['A','C','G','T']
	Neighborhood = []
	SuffixNeighbors = Neighbors(Pattern[1:],d)
	for text in SuffixNeighbors:
		if hammingDistance(Pattern[1:],text) < d:
			for nucleotide in ['A','C','G','T']:
				Neighborhood.append(nucleotide+text)
		else:
			Neighborhood.append(Pattern[0]+text)
	return Neighborhood

def MotifEnumeration(DNA,k,d):
	temp = [0]*len(DNA)
	for i,Pattern in enumerate(DNA):
		prima_neighbors = []
		for j in range(len(Pattern)-k+1):
			prima_pattern = Pattern[j:j+k]
			prima_neighbors.extend(Neighbors(prima_pattern,d))
		temp[i] = prima_neighbors
	
	return intersection(temp[0], *temp)

lines = sys.stdin.read().splitlines() # read in the input from STDIN
i = 0
k = 0
d = 0
DNA = []
for i,line in enumerate(lines):
	if i == 0:
		k = int(line.split(' ')[0])
		d = int(line.split(' ')[1])
		i = 1
	else:
		DNA.append(line)

motif = MotifEnumeration(DNA,k,d)
for m in motif:
	print m,




