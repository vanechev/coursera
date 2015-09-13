import sys
from ComputingFrequencies import ComputingFrequencies
from pattern_2_number import PatternToNumber
from number2pattern import NumberToPattern

def BetterClumpFinding(Genome, k, t, L):
    FP = []
    Clump = [0]*(4**k)
    Text = Genome[0:L]
    Farray = ComputingFrequencies(Text,k)
    for i in range(4**k):
        if Farray[i] >= t:
            print i
            Clump[i] = 1
    for i in range(1,len(Genome)-L+1):
        FirstPattern = Genome[i-1:i+k-1]
        index = PatternToNumber(FirstPattern)
        #print index
        Farray[index] = Farray[index]-1
        LastPattern = Genome[i+L-k:i+L]
        #print FirstPattern,LastPattern
        index = PatternToNumber(LastPattern)
        Farray[index] = Farray[index]+1
        if Farray[index] >= t:
            Clump[index]= 1
    for i in range(4**k):
        if Clump[i] == 1:
            Pattern = NumberToPattern(i,k)
            FP.append(Pattern)
    return FP


lines = sys.stdin.read().splitlines() # read in the input from STDIN

Genome = lines[0]
line = lines[1].split()
k = int(line[0])
L = int(line[1])
t = int(line[2])
# Genome = 'CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'
# k = 5
# L = 50
# t = 4

f = set(BetterClumpFinding(Genome,k,t,L))
print len(f)
