#EXERCISE BREAK: Give all values of Skewi (GAGCCACCGCGATA) for i ranging from 0 to 14.
import sys

# def Skew(Genome,f,t):
# 	sk = [0]*(t+1)
# 	for i in range(f,t+1):
# 		sk[i]=Skewi(i,Genome)
# 	return sk
import time
start_time = time.time()

Genome = 'CATTCCAGTACTTCATGATGGCGTGAAGA'
# lines = sys.stdin.read().splitlines() # read in the input from STDIN
# Genome = lines[0]
skew_values = {'A': 0, 'C': -1, 'T': 0, 'G': 1}
skew = [0]
for base in Genome:
    skew.append(skew_values[base] + skew[-1])

maximum = max(skew)
indices = [i for i, x in enumerate(skew) if x == maximum]
for i in indices:
	print i,

print
print("--- %s seconds ---" % (time.time() - start_time))