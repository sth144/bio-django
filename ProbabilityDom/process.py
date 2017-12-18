from __future__ import division
import numpy as np
import re as re


# probabilityDom() is a predictive function which takes parameters k, m, and n, which are
#	the proportions of homozygous dominant, heterozygous, and homozygous recessive individuals
# 	in a population. Returns the probability that offspring from a randomly mating pair will
#	have the dominant phenotype

def probabilityDom(k, m, n):

	# Convert and sum input data
	k, m, n = float(k), float(m), float(n)
	pop = k + m + n

	# Calculate and return probability of dominant phenotype
	prob = (k / pop) + (m / (2 * pop))
	return prob