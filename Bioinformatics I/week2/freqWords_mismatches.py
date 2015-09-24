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

def PatternToNumber(pattern):
	if len(pattern) == 0:
		return 0
	symbol = pattern[-1]
	prefix = pattern[:-1]
	return 4 * PatternToNumber(prefix) + SymbolToNumber(symbol)

def SymbolToNumber(symbol):
	if symbol == 'A':
		return 0
	elif symbol == 'C':
		return 1
	elif symbol == 'G':
		return 2
	elif symbol == 'T':
		return 3

def ApproximatePatternCount(t,p,d):
	k = len(p)
	app = []
	for i in range(len(t)-k+1):
		temp = t[i:i+k]
		hD = hammingDistance(p,temp)
		if hD <= d:
			app.append(i)

	return len(app)

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

# FrequentWordsWithMismatches(Text, k, d)
#         FrequentPatterns : an empty set
#         for i : 0 to 4k - 1
#             Close(i) : 0
#             FrequencyArray : 0
#         for i : 0 to len(Text) - k
#             Neighborhood : Neighbors(Text(i, k), d)
#             for each Pattern from Neighborhood
#                 index : PatternToNumber(Pattern)
#                 Close(index) : 1
#         for i :0 to 4k - 1
#             if Close(i) = 1
#                 Pattern : NumberToPattern(i, k)
#                 FrequencyArray(i) : ApproximatePatternCount(Text, Pattern, d)
#         maxCount : maximal value in FrequencyArray
#         for i :0 to 4k - 1
#             if FrequencyArray(i) = maxCount
#                 Pattern : NumberToPattern(i, k)
#                 add Pattern to the set FrequentPatterns
#        return FrequentPatterns 

def FrequentWordsWithMismatches(Text, k, d):
	FP = set()
	Neighborhoods = []
	NeighborhoodsArray = []
	for i in range(len(Text)-k+1):
		Neighborhoods.append(Neighbors(Text[i:i+k],d))
		NeighborhoodsArray.extend(Neighbors(Text[i:i+k],d))

	#NeighborhoodsArray = list(set(NeighborhoodsArray))
	
	dictNeighbors = Counter(NeighborhoodsArray)

	maxCount = max(dictNeighbors.values())

	for i, v in dictNeighbors.items():
		if v == maxCount:
			FP.add(i)

	# FrequencyArray = [0]*(4**k)
	# Close = [0]*(4**k)
	# for i in range(len(Text)-k+1):
	# 	Neighborhood = Neighbors(Text[i:i+k],d)
	# 	print i
	# 	print Neighborhood
	# 	for pattern in Neighborhood:
	# 		index = PatternToNumber(pattern)
	# 		Close[index]=1
	# 	for i in range(4**k):
	# 		if Close[i] == 1:
	# 			Pattern = NumberToPattern(i,k)
	# 			FrequencyArray[i] = ApproximatePatternCount(Text,Pattern,d)
	# 	maxCount = max(FrequencyArray)
	# 	for i in range(4**k):
	# 		if FrequencyArray[i]==maxCount:
	# 			Pattern = NumberToPattern(i,k)
	# 			FP.append(Pattern)
	return FP


Text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
k = 4
d = 1

lines = sys.stdin.read().splitlines() # read in the input from STDIN
Text = lines[0]
k = int(lines[1].split(' ')[0])
d = int(lines[1].split(' ')[1])


FrequencyPatterns = FrequentWordsWithMismatches(Text, k, d)
for i in FrequencyPatterns:
	print i,
