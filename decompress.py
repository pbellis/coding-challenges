compressed = "0[abc]"

def isDigit(c):
	delta = ord(c) - ord('0')
	if delta > -1 and delta < 10:
		return True
	else:
		return False

def decompress(compressed, start):
	power10 = 1
	number = 0
	
	outer = "";
	
	i = start
	while i < len(compressed) and compressed[i] != ']':
		if compressed[i] == '[':
			inner, i = decompress(compressed, i + 1)
			mul = number if power10 > 1 else 1
			number, power10 = 0, 1
			outer += inner * mul
		elif isDigit(compressed[i]):
			number += power10 * int(compressed[i])
			power10 *= 10;
		else:
			outer += compressed[i];
		i += 1
	
	return outer, i
		
print(decompress(compressed, 0))