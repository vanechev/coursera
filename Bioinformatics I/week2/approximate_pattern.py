# Approximate Pattern Matching Problem: Find all approximate occurrences of a pattern in a string.
#      Input: Strings Pattern and Text along with an integer d.
#      Output: All starting positions where Pattern appears as a substring of Text with at most d mismatches.

import sys
def hammingDistance(p,q):
	if len(p) == len(q):
		c = 0
		for i in range(len(p)):
			if p[i] != q[i]:
				c+=1
	return c

def ApproximatePatternCount(t,p,d):
	k = len(p)
	app = []
	for i in range(len(t)-k+1):
		temp = q[i:i+k]
		hD = hammingDistance(p,temp)
		if hD <= d:
			app.append(i)

	return len(app)

p = 'AA'
q = 'TACGCATTACAAAGCACA'
h = 1
# lines = sys.stdin.read().splitlines() # read in the input from STDIN
# p = lines[0]
# q = lines[1]
# h = int(lines[2])

print ApproximatePatternCount(q,p,h)

