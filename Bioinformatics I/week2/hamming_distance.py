# Hamming Distance Problem: Compute the Hamming distance between two strings.
#      Input: Two strings of equal length.
#      Output: The Hamming distance between these strings.
import sys
def hammingDistance(p,q):
	if len(p) == len(q):
		c = 0
		for i in range(len(p)):
			if p[i] != q[i]:
				c+=1
	return c

p = 'CTACAGCAATACGATCATATGCGGATCCGCAGTGGCCGGTAGACACACGT'
q = 'CTACCCCGCTGCTCAATGACCGGGACTAAAGAGGCGAAGATTATGGTGTG'
# lines = sys.stdin.read().splitlines() # read in the input from STDIN
# p = lines[0]
# q = lines[1]

print hammingDistance(p,q)
