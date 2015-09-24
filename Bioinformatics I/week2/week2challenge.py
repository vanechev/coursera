#week2 real challenge
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

def Skew(Genome):
	skew_values = {'A': 0, 'C': -1, 'T': 0, 'G': 1}
	skew = [0]
	for base in Genome:
		skew.append(skew_values[base] + skew[-1])
	return skew

def BetterClumpFinding(Genome, k, t, L):
    FP = []
    Clump = [0]*(4**k)
    Text = Genome[0:L]
    Farray = ComputingFrequencies(Text,k)
    for i in range(4**k):
        if Farray[i] >= t:
            Clump[i] = 1
    for i in range(1,len(Genome)-L+1):
        FirstPattern = Genome[i-1:i+k-1]
        index = PatternToNumber(FirstPattern)
        #print index
        Farray[index] = Farray[index]-1
        LastPattern = Genome[i+L-k:i+L]
        #print FirstPattern,LastPattern
        index = PatternToNumber(LastPattern)
        Farray[index] = Farray[index]+1
        if Farray[index] >= t:
            Clump[index]= 1
    for i in range(4**k):
        if Clump[i] == 1:
            Pattern = NumberToPattern(i,k)
            FP.append(Pattern)
    return FP

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

Genome = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
L = 500
k = 9
d = 1
lines = sys.stdin.read().splitlines() # read in the input from STDIN
Genome = lines[0]
print Genome

skew = Skew(Genome)
print skew
maximum = max(skew)
minimum = min(skew)
print minimum
indices = [i for i, x in enumerate(skew) if x == minimum]
print indices
Text = Genome[minimum:minimum+L]
FrequencyPatterns = FrequentWordsWithMismatches(Text, k, d)
for i in FrequencyPatterns:
	print i,
