from __future__ import division
import numpy as np
import re as re

from .codonTable import codonTable

def translate(seq):
	sequence = seq.replace('U', 'T').upper()
	codons = re.findall('...', sequence)		# use regular expressions to parse codons from sequence
	res = []
	for codon in codons:
		res.append(codonTable[codon])
	result = ''.join(res)
	return result
