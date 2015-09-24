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

Pattern = 'TGCAT'
d = 2

print len(Neighbors(Pattern,d))
