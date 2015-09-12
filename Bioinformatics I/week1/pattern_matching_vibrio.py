# Solve the Pattern Matching Problem.
# Input: Two strings, Pattern and Genome.
# Output: A collection of space-separated integers specifying all starting positions where Pattern appears
# as a substring of Genome.
import sys

def Pattern_Matching_Indices(pattern,text):
	a = []
	for i in xrange(len(text)-len(pattern)+1):
		if text[i:i+len(pattern)] == pattern:
			a.append(i)
	return a
lines = sys.stdin.read().splitlines()
pattern = 'CTTGATCAT'
text = lines[0]

#pattern = 'ATAT'
#text = 'GATATATGCATATACTT'

idx = Pattern_Matching_Indices(pattern,text)
for i in idx:
	print i,