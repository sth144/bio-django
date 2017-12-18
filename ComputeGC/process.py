# computeGC() function returns GC base pair proportion as a decimal

def computeGC(seq):

	# Initialize count to 0
	n = 0

	# Iterate throug the sequence
	for char in seq:
		if char == 'G':
			n += 1
		elif char == 'C':
			n += 1
		else:
			pass

	# Convert numbers to floats, carry out division, and return result
	return str(float(n) / float(len(seq)))
