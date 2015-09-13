
from ComputingFrequencies import ComputingFrequencies
from number2pattern import NumberToPattern

def FasterFrequentWords(Text , k):
	FP=[]
	Farray = ComputingFrequencies(Text,k)
	maxCount = max(Farray)
	for i in range(4**k):
		if FrequencyArray[i] == maxCount:
			Pattern = NumberToPattern(i,k)
			FP.append(Pattern)

	return FP



# for f in FasterFrequentWords(Text,k):
# 	print f,