from __future__ import division
import numpy as np
import re as re

from .codonTable import codonTable


# translate() function translates a DNA or RNA coding sequence and returns the peptide sequence

def translate(seq):

	# Handle both DNA and RNA
	sequence = seq.replace('U', 'T').upper()

	# use regular expressions to parse codons from sequence
	codons = re.findall('...', sequence)		
	res = []

	# Iterate through the codons
	for codon in codons:
		res.append(codonTable[codon])
	result = ''.join(res)

	return result
