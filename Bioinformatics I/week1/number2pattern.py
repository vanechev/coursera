#number2pattern



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

#print NumberToPattern(6202,8)