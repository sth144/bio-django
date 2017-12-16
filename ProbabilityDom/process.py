from __future__ import division
import numpy as np
import re as re

def probabilityDom(k, m, n):
	k, m, n = float(k), float(m), float(n)
	pop = k + m + n
	prob = (k / pop) + (m / (2 * pop))
	return prob