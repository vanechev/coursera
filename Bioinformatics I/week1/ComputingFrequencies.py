# ComputingFrequencies(Text , k)
from pattern_2_number import PatternToNumber

def ComputingFrequencies(Text , k):
	FrequencyArray = [0]*((4**k))
	for i in range(len(Text)-k+1):
		Pattern = Text[i:i+k]
		j = PatternToNumber(Pattern)
		FrequencyArray[j] = FrequencyArray[j]+1
	return FrequencyArray

#arr = ComputingFrequencies('ACGCGGCTCTGAAA',5)

# for i in arr:
# 	print i,
