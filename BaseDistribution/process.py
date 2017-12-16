from __future__ import division
import numpy as np

def baseDistribution(seq):

    length = len(seq)
    a, t, c, g = 0, 0, 0, 0

    for i in range(0, length):
        if seq[i] == 'A':
            a += 1
        elif seq[i] == 'T' or seq[i] == 'U':
            t += 1
        elif seq[i] == 'C':
            c += 1
        elif seq[i] =='G':
            g += 1
        else:
            pass
    result = [a, t, c, g]
    return result
