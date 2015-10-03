# CODE CHALLENGE: Implement GIBBSSAMPLER.
#      Input: Integers k, t, and N, followed by a collection of strings Dna.
#      Output: The strings BestMotifs resulting from running GIBBSSAMPLER(Dna, k, t, N) with
#      20 random starts. Remember to use pseudocounts!

# Note: The next lesson features a detailed example of GIBBSSAMPLER, so you may wish to return to this problem later.

# Visit the code-graded challenge!
# Sample Input:      

#      8 5 100
#      CGCCCCTCTCGGGGGTGTTCAGTAACCGGCCA
#      GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG
#      TAGTACCGAGACCGAAAGAAGTATACAGGCGT
#      TAGATCAAGTTTCAGGTGCACGTCGGTGAACC
#      AATCCACCAGCTCCACGTGCAATGTTGGCCTA
# Sample Output:

#      TCTCGGGG
#      CCAAGGTG
#      TACAGGCG
#      TTCAGGTG
#      TCCACGTG

 # GIBBSSAMPLER(Dna, k, t, N)
 #        randomly select k-mers Motifs = (Motif1,..., Motift) in each string
 #            from Dna
 #        BestMotifs <- Motifs
 #        for j <- 1 to N
 #            i <- Random(t)
 #            Profile <- profile matrix constructed from all strings in Motifs
 #                       except for Motifi
 #            Motifi <- Profile-randomly generated k-mer in the i-th sequence
 #            if Score(Motifs) < Score(BestMotifs)
 #                BestMotifs <- Motifs
 #        return BestMotifs

import sys
from random import randint

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

def kmerToIndices(kmer):
	ind = []
	for e in kmer:
		if e == 'A':
			ind.append(0)
		elif e == 'C':
			ind.append(1)
		elif e == 'G':
			ind.append(2)
		elif e == 'T':
			ind.append(3)
		else:
			print "error"
			return 0
	return ind

def getProbabiltyProfileKmer(p,kmer):
	kmersIndices = kmerToIndices(kmer)
	prob = 1.0
	for i in range(len(kmersIndices)):
		prob *= p[i][kmersIndices[i]]
	return prob

def profileInit(p,k):
	for i in range(4):
		p.append([0.0]*k)
	return Profile

def getProbabilityProfileStrand(Strand,p):
	allProbs = []
	prob = 0.0
	pos = 0
	mostProbkmer = Strand[0:k]
	for i in range(len(Strand)-k+1):
		kmer = Strand[i:i+k]
		r = getProbabiltyProfileKmer(map(list,map(None,*p)),kmer)
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

def Profile(Mo):
	Pro = []
	profileInit(Pro,k)
	count = [[0 for col in range(len(Pro[0]))] for row in range(len(Pro))]
	indMo = MatrixToIndices(Mo)
	MotifsSc = map(list,map(None,*indMo))
	for i,row in enumerate(MotifsSc):
		for el in row:
			count[el][i] += 1.0
	for i,row in enumerate(count):
		for j,el in enumerate(row):
			count[i][j] += 1.0
	for i,row in enumerate(count):
		for j,el in enumerate(row):
			Pro[i][j] = count[i][j]/(len(Mo)+len(Pro))
	return Pro

def mode(values):
    return max(set(values), key=values.count)

def Score(MotifMatrix):
	if len(MotifMatrix) == 0:
		return k*t
	MotifIndices = MatrixToIndices(MotifMatrix)
	temp = map(list,map(None,*MotifIndices))
	unmatches = 0
	for el in temp:
		m = mode(el)
		unmatches += len(el) - len([e for e in el if e == m])
	return unmatches

def getMotifs(p,Dna):
	Motifs = []
	#add best kmer to motif list
	for strand in Dna:
		Motifs.append(getProbabilityProfileStrand(strand,p))
	return Motifs


def randomizedMotifSearch(Dna,k,t):
	random.seed()
	BestMotifs = []
	Motifs1 = []
	profile = []
	#generate first kmers from Dna randomly
	for strand in Dna:
		randi = random.randint(0,len(strand)-k)
		BestMotifs.append(strand[randi:randi+k])
	
	Motifs1 = BestMotifs
	while True:
		profile = Profile(Motifs1)
		Motifs1 = getMotifs(profile,Dna)
		#print Score(Motifs1), Score(BestMotifs)
		if Score(Motifs1) < Score(BestMotifs):
			BestMotifs = Motifs1
		else:
			return BestMotifs


def gibbsSampler(Dna,k,t,N):
	motifs = []
	#generate first kmers from Dna randomly
	for strand in Dna:
		randi = randint(0,len(strand)-k)
		motifs.append(strand[randi:randi+k])
	best_motifs = motifs
	best_score = Score(motifs)

	#from 1 to N
	for i in xrange(N):
		r = randint(0,t-1)
		profile = Profile([motif for index,motif in enumerate(motifs) if index != r])
		motifs = [getProbabilityProfileStrand(Dna[index],profile) if index == r else motif for index,motif in enumerate(motifs)]
		current_score = Score(motifs)
		if current_score < best_score:
			best_motifs = motifs
			best_score = current_score
	return best_motifs,best_score



lines = sys.stdin.read().splitlines()
k = int(lines[0].split(' ')[0])
t = int(lines[0].split(' ')[1])
N = int(lines[0].split(' ')[2])
Dna = []
Dna = lines[1:]

best = []
best_score = k*t
for repeat in xrange(20):
	print >> sys.stderr,"Iteration: %d\r"%(repeat),
	current_motifs,current_score = gibbsSampler(Dna,k,t,N)
	if current_score < best_score:
		best = current_motifs
		best_score = current_score
print
for el in best:
	print el






