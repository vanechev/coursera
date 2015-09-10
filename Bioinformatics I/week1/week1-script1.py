import sys

def PatternCount(Text,Pattern):
	count = 0
	for i in range(len(Text)-len(Pattern)+1):
		if Text[i:i+len(Pattern)] == Pattern:
			count+=1
	return count

lines = sys.stdin.read().splitlines() # read in the input from STDIN
# lines=["a","b"]
# lines[0]="GCGCG"
# lines[1]="GCG"

Text = lines[0]
Pattern = lines[1]
print PatternCount(Text,Pattern)