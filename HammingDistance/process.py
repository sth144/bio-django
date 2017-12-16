from __future__ import division
import numpy as np
import re as re

def hammingDistance(seqA, seqB):
	hamming = 0
	charsA, charsB = re.findall('.', seqA), re.findall('.', seqB)
	checkLen = min(len(charsA), len(charsB))
	for i in range (0, checkLen):
		if charsA[i] != charsB[i]:
			hamming += 1
	hamming += (len(charsA) - checkLen)
	hamming += (len(charsB) - checkLen)
	return hamming