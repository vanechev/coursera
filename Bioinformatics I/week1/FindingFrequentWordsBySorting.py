
from pattern_2_number import PatternToNumber
from number2pattern import NumberToPattern

def FindingFrequentWordsBySorting(Text , k):
    FP = []
    Index = [0]*(len(Text)-k+1)
    Count = [0]*(len(Text)-k+1)
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Index[i] = PatternToNumber(Pattern)
        Count[i] = 1
    SortedIndex = sorted(Index)
    for i in range(len(Text)-k+1):
        if SortedIndex[i] == SortedIndex[i-1]:
            Count[i] = Count[i-1]+1
    maxCount = max(Count)
    for i in range(len(Text)-k+1):
        if Count[i] == maxCount:
            Pattern = NumberToPattern(SortedIndex[i],k)
            FP.append(Pattern)
    return FP

# Text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
# k = 4

# for f in FindingFrequentWordsBySorting(Text , k):
#     print f,

