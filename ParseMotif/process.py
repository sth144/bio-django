from __future__ import division
import numpy as np
import re as re

def parseMotif(motif, seq):
	motif, seq = str(motif), str(seq)
	result = []
	for frame in re.finditer(motif, seq):
		result.append([frame.start(), frame.end()])
	return result