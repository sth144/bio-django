def computeGC(seq):
	n = 0
	for char in seq:
		if char == 'G':
			n += 1
		elif char == 'C':
			n += 1
		else:
			pass
	return str(float(n) / float(len(seq)))
