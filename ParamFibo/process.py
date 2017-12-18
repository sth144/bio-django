from __future__ import division
import numpy as np
import re as re


# population() returns the population after n generations with k offspring per generation

def population(n, k):

	# convert parameter strings to numbers
	n = int(n)
	k = int(k)
	
	# Base case
	if n < 2:
		return n

	# Recursive case	
	else:
		# Recursive Fibonacci sequence calculation
		return (
			population(n-1, k) +
			population(n-2, k) * k
		)