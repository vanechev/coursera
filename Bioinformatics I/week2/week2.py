#EXERCISE BREAK: Give all values of Skewi (GAGCCACCGCGATA) for i ranging from 0 to 14.
import sys
def Skewi(i,Genome):
	countG = 0
	countC = 0
	Genome = Genome[:i]
	for k in range(len(Genome)):
		if Genome[k]=='G':
			countG+=1
		if Genome[k]=='C':
			countC+=1
	return countG-countC

def Skew(Genome):
	sk = [0]*(len(Genome)+1)
	for i in range(len(Genome)+1):
		sk[i]=Skewi(i,Genome)
	return sk

# def Skew(Genome,f,t):
# 	sk = [0]*(t+1)
# 	for i in range(f,t+1):
# 		sk[i]=Skewi(i,Genome)
# 	return sk
import time
start_time = time.time()

#Genome = 'TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'
lines = sys.stdin.read().splitlines() # read in the input from STDIN
Genome = lines[0]
skew_values = {'A': 0, 'C': -1, 'T': 0, 'G': 1}
skew = [0]
for base in Genome:
    skew.append(skew_values[base] + skew[-1])

minimum = min(skew)
indices = [i for i, x in enumerate(skew) if x == minimum]
for i in indices:
	print i,

print
print("--- %s seconds ---" % (time.time() - start_time))