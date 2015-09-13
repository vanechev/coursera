#pattern to number 

def PatternToNumber(pattern):
	if len(pattern) == 0:
		return 0
	symbol = pattern[-1]
	prefix = pattern[:-1]
	return 4 * PatternToNumber(prefix) + SymbolToNumber(symbol)

def SymbolToNumber(symbol):
	if symbol == 'A':
		return 0
	elif symbol == 'C':
		return 1
	elif symbol == 'G':
		return 2
	elif symbol == 'T':
		return 3

#print PatternToNumber('ACGAACGTCACGACAA')