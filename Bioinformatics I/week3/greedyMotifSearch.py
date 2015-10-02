# CODE CHALLENGE: Implement GREEDYMOTIFSEARCH.
#     Input: Integers k and t, followed by a collection of strings Dna.
#     Output: A collection of strings BestMotifs resulting from applying GREEDYMOTIFSEARCH(Dna,k,t).
#     If at any step you find more than one Profile-most probable k-mer in a given string, use the
#     one occurring first.

#     Sample Input:
#      3 5
#      GGCGTTCAGGCA
#      AAGAATCAGTCA
#      CAAGGAGTTCGC
#      CACGTCAATCAC
#      CAATAATATTCG

# Sample Output:
#      CAG
#      CAG
#      CAA
#      CAA
#      CAA

# GREEDYMOTIFSEARCH(Dna, k, t)
#         BestMotifs <- motif matrix formed by first k-mers in each string
#                       from Dna
#         for each k-mer Motif in the first string from Dna
#             Motif1 <- Motif
#             for i = 2 to t
#                 form Profile from motifs Motif1, ..., Motifi - 1
#                 Motifi <- Profile-most probable k-mer in the i-th string
#                           in Dna
#             Motifs <- (Motif1, ..., Motift)
#             if Score(Motifs) < Score(BestMotifs)
#                 BestMotifs <- Motifs
#         return BestMotifs
# A=0,C=1,G=2,T=3
import sys
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

def profileInit(Profile,k):
	for i in range(4):
		Profile.append([0.0]*k)
	return Profile

def getProbabilityProfileStrand(Strand,Profile):
	allProbs = []
	prob = 0.0
	pos = 0
	mostProbkmer = Strand[0:k]
	for i in range(len(Strand)-k+1):
		kmer = Strand[i:i+k]
		r = getProbabiltyProfileKmer(map(list,map(None,*Profile)),kmer)
		#print r
		if prob < r:
			pos = i
			prob = r
			mostProbkmer = kmer
	return mostProbkmer

def MatrixToIndices(Mo):
	Res = []
	for m in Mo:
		Res.append(kmerToIndices(m))
	return Res

def getProfile(Mo,Pro):
	indMo = MatrixToIndices(Mo)
	if len(indMo) > 1:
		MotifsSc = map(list,map(None,*indMo))
	else:
		MotifsSc = list(zip(*indMo))
	for i,row in enumerate(MotifsSc):
		for el in row:
			#print Pro[el]
			Pro[el][i] += (1.0/len(Mo))
	return Pro

def mode(values):
    return max(set(values), key=values.count)

def Score(MotifMatrix):
	MotifIndices = MatrixToIndices(MotifMatrix)
	temp = map(list,map(None,*MotifIndices))
	unmatches = 0
	for el in temp:
		m = mode(el)
		unmatches += len(el) - len([e for e in el if e == m])
	return unmatches


def greddyMotifSeach(Dna,k,t):
	
	BestMotifs = []
	#generate first kmers from Dna
	for strand in Dna:
		BestMotifs.append(strand[:k])
	Motif = []
	#generate all kmers of first strand in Dna
	for i in range(len(Dna[0])-k+1):
		Motif.append(Dna[0][i:i+k])

	#iterate over all kmers of first strand
	for kmer in Motif:
		Motif1 = []
		#add first Motif of first strand
		Motif1.append(kmer)
		for i in range(1,t):
			Profile = []
			profileInit(Profile,k)
			Profile = getProfile(Motif1,Profile)
			#add best Strand to motif list
			Motif1.append(getProbabilityProfileStrand(Dna[i],Profile))
		#check best score
		#ifScore(Motifs) < Score(BestMotifs) BestMotifs <- Motifs outputBestMotifs
		if Score(Motif1) < Score(BestMotifs):
			BestMotifs = Motif1
	return BestMotifs

lines = sys.stdin.read().splitlines()
k = int(lines[0].split(' ')[0])
t = int(lines[0].split(' ')[1])
Dna = []
Dna = lines[1:]

for e in greddyMotifSeach(Dna,k,t):
	print e,







