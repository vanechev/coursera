import sys

def PatternCount(Text,Pattern):
	count = 0
	for i in xrange(len(Text)-len(Pattern)+1):
		if Text[i:i+len(Pattern)] == Pattern:
			count+=1
	return count


def FrequentWords(Text,k):
	FP = []
	count = range(len(Text)-k+1)
	for i in range(len(Text)-k+1):
		Pattern = Text[i:i+k]
		count[i] = PatternCount(Text,Pattern)
	maxCount = max(count)
	for i in range(len(Text)-k+1):
		if count[i] == maxCount:
			FP.append(Text[i:i+k])
	FP =list(set(FP))
	print maxCount
	return FP

lines = sys.stdin.read().splitlines()
Text = lines[0]
k = int(lines[1])

for f in FrequentWords(Text,k):
	print f,