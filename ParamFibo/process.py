from __future__ import division
import numpy as np
import re as re

def population(n, k):
	n = int(n)
	k = int(k)
	if n < 2:
		return n
	else:
		return (
			population(n-1, k) +
			population(n-2, k) * k
		)