def reverseComplement(stringInput):
	string = stringInput[::-1].upper()
	pairs = {
		'A':'T', 'T':'A',
		'G':'C', 'C':'G'
	}
	_list = list(string)
	new = []
	for char in _list:
		new.append(pairs[char])
	return ''.join(new)
