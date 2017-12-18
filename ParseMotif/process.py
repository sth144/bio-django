from __future__ import division
import numpy as np
import re as re


# parseMotif() function parses sequence and returns indices of occurrence for 
# 	input motif 

def parseMotif(motif, seq):

	# Stringify inputs from DOM HTML input
	motif, seq = str(motif), str(seq)

	# Initialize result to an empty list
	result = []

	# Iterate through each frame among those where motif occurss
	for frame in re.finditer(motif, seq):
		# Append the indices of occurrence to result
		result.append([frame.start(), frame.end()])

	return result