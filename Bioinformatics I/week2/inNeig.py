ImmediateNeighbors(Pattern)
        Neighborhood ← the set consisting of single string Pattern
        for i = 1 to |Pattern|
            symbol ← i-th nucleotide of Pattern
            for each nucleotide x different from symbol
                Neighbor ← Pattern with the i-th nucleotide substituted by x
                add Neighbor to Neighborhood
        return Neighborhood

def inmediateNeighbors(Pattern):
	Neighborhood = 
	for i in range(len(Pattern))
	symbol = Pattern[i]
	for s