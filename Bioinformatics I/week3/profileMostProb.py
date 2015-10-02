# Profile-most Probable k-mer Problem: Find a Profile-most probable k-mer in a string.
#      Input: A string Text, an integer k, and a 4 x k matrix Profile.
#      Output: A Profile-most probable k-mer in Text.

#      Sample Input:
#      ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT
#      5
#      0.2 0.2 0.3 0.2 0.3
#      0.4 0.3 0.1 0.5 0.1
#      0.3 0.3 0.5 0.2 0.4
#      0.1 0.2 0.1 0.1 0.2

# Sample Output:
#      CCGAG
# A=0,C=1,G=2,T=3
import sys
import decimal
def kmerToIndices(kmer):
	ind = []
	for e in kmer:
		if e == 'A':
			ind.append(0)
		elif e == 'C':
			ind.append(1)
		elif e == 'G':
			ind.append(2)
		else:
			ind.append(3)
	return ind

def getProbabiltyProfileKmer(Profile,kmer):
	kmersIndices = kmerToIndices(kmer)
	prob = 1.0
	for i in range(len(kmersIndices)):
		prob *= Profile[i][kmersIndices[i]]
	return prob

def getProbabilityProfileStrand(Strand,Profile):
	allProbs = []
	prob = 0.0
	pos = 0
	mostProbkmer = ''
	for i in range(len(Text)-k+1):
		kmer = Text[i:i+k]
		r = getProbabiltyProfileKmer(map(list,map(None,*Profile)),kmer)
		if prob < r:
			pos = i
			prob = r
			mostProbkmer = kmer

	return mostProbkmer

lines = sys.stdin.read().splitlines()
Text = lines[0]
k = int(lines[1])
Profile = []
for line in lines[2:]:
	Profile.append( [float(i) for i in line.split(' ')])

print getProbabilityProfileStrand(Text,Profile)