# DistanceBetweenPatternAndStrings(Pattern, Dna)
#     k <- |Pattern|
#     distance <- 0
#     for each string Text in Dna
#         HammingDistance <- 00
#         for each k-mer Pattern' in Text
#             if HammingDistance > HammingDistance(Pattern, Pattern')
#                 HammingDistance <- HammingDistance(Pattern, Pattern')
#         distance <-  distance + HammingDistance
#     return distance
# Sample Input:
# AAA
# TTACCTTAAC GATATCTGTC ACGGCGTTCG CCCTAAAGAG CGTCAGAGGT
# Sample Output:
# 5
from itertools import product
import sys
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

def DistanceBetweenPatternAndStrings(Pattern, Dna):
	k = len(Pattern)
	distance = 0
	for text in Dna:
		kmers = []
		HammingDistance = k
		for j in range(len(text)-k+1):
			kmer = text[j:j+k]
			if HammingDistance > hammingDistance(kmer,Pattern):
				HammingDistance = hammingDistance(kmer,Pattern)
		distance+=HammingDistance
	return distance

def NumberToPattern(index,k):
	if k==1:
		return NumberToSymbol(index)
	prefixIndex = index//4
	r = index%4
	symbol = NumberToSymbol(r)
	PrefixPattern = NumberToPattern(prefixIndex, k-1)
	return PrefixPattern+symbol

def NumberToSymbol(number):
	if number == 0:
		return 'A'
	elif number == 1:
		return 'C'
	elif number == 2:
		return 'G'
	elif number == 3:
		return 'T'

# MedianString(Dna, k)
#     distance <- inf
#     for i <-0 to 4k -1
#         Pattern <- NumberToPattern(i, k)
#         if distance > DistanceBetweenPatternAndStrings(Pattern, Dna)
#             distance <- DistanceBetweenPatternAndStrings(Pattern, Dna)
#             Median <- Pattern
#     return Median
def MedianString(Dna,k):
	distance = 100000000
	Median = []
	kmers = list(product('ACGT',repeat=k))
	for Pattern in kmers:
		#Pattern = NumberToPattern(i,k)
		if distance > DistanceBetweenPatternAndStrings(Pattern,Dna):
			distance = DistanceBetweenPatternAndStrings(Pattern,Dna)
			Median = Pattern
			print Median
	return Median

#Pattern = 'AAA'
#Dna = 'AAATTGACGCAT GACGACCACGTT CGTCAGCGCCTG GCTGAGCACCGG AGTTCGGGACAG'.split(' ')
lines = sys.stdin.read().splitlines() # read in the input from STDIN
k = 0
Dna = []
for i,line in enumerate(lines):
	if i == 0:
		k = int(line[0])
		i = 1
	else:
		Dna.append(line)
print MedianString(Dna,k)













