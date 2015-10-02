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

Pattern = 'AAA'
Dna = 'TTACCTTAAC GATATCTGTC ACGGCGTTCG CCCTAAAGAG CGTCAGAGGT'.split(' ')
print DistanceBetweenPatternAndStrings(Pattern, Dna)














