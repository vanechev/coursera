# Frequent Words with Mismatches Problem: Find the most frequent k-mers with mismatches in a string.
#      Input: A string Text as well as integers k and d. (You may assume k <= 12 and d <= 3.)
#      Output: All most frequent k-mers with up to d mismatches in Text.
# generate all 4k k-mers Pattern
# compute ApproximatePatternCount(Text, Pattern, d) for each k-mer Pattern
# output k-mers with the maximum number of approximate occurrences
import sys
import collections
import itertools
from collections import Counter

def hammingDistance(p,q):
	if len(p) == len(q):
		c = 0
		for i in range(len(p)):
			if p[i] != q[i]:
				c+=1
	return c

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

# Neighbors(Pattern, d)
#         if d = 0
#             return {Pattern}
#         if |Pattern| = 1 
#             return {A, C, G, T}
#         Neighborhood : an empty set
#         SuffixNeighbors : Neighbors(Suffix(Pattern), d)
#         for each string Text from SuffixNeighbors
#             if HammingDistance(Suffix(Pattern), Text) < d
#                 for each nucleotide x
#                     add x + Text to Neighborhood
#             else
#                 add FirstSymbol(Pattern) + Text to Neighborhood
#         return Neighborhood

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

def FrequentWordsWithMismatches(Text, k, d):
	FP = set()
	NeighborhoodsArray = []
	for i in range(len(Text)-k+1):
		NeighborhoodsArray.extend(Neighbors(Text[i:i+k],d))
		NeighborhoodsArray.extend(Neighbors(complementDNA(Text[i:i+k]),d))
	
	dictNeighbors = Counter(NeighborhoodsArray)
	maxCount = max(dictNeighbors.values())

	for i, v in dictNeighbors.items():
		if v == maxCount:
			FP.add(i)

	return FP


Text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
k = 4
d = 1

# lines = sys.stdin.read().splitlines() # read in the input from STDIN
# Text = lines[0]
# k = int(lines[1].split(' ')[0])
# d = int(lines[1].split(' ')[1])


FrequencyPatterns = FrequentWordsWithMismatches(Text, k, d)
for i in FrequencyPatterns:
	print i,
