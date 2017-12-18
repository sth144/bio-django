from __future__ import division
import numpy as np
import re as re


# hammingDistance() returns the hamming distance between two input strings

def hammingDistance(seqA, seqB):

	# Initialize result to 0
	hamming = 0

	# find all one character strings in sequences A and B
	charsA, charsB = re.findall('.', seqA), re.findall('.', seqB)

	# Store length of shorter sequence
	checkLen = min(len(charsA), len(charsB))

	# Iterate from 0 to checkLen
	for i in range (0, checkLen):

		# If characters at index in sequences A and B are equal
		if charsA[i] != charsB[i]:
			hamming += 1

	# If one string is longer than checkLen, these statements will increase result by the disparity
	hamming += (len(charsA) - checkLen)
	hamming += (len(charsB) - checkLen)

	# return the hamming distance
	return hamming