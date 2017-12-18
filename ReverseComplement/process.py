# reverseComplement() function returns the revurse complement of a DNA sequence

def reverseComplement(stringInput):

	# Reverse the input
	string = stringInput[::-1].upper()
	
	# define pairs dict
	pairs = {
		'A':'T', 'T':'A',
		'G':'C', 'C':'G'
	}
	
	# Turn string into list
	_list = list(string)

	# Define a new empty list
	new = []

	# Iterate through the sequence list and append corresponding chars from pairs dict to new list
	for char in _list:
		new.append(pairs[char])

	# Join and return the new list as a string
	return ''.join(new)
