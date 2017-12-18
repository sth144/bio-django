from __future__ import division
import numpy as np


# baseDistribution() function definition

def baseDistribution(seq):

    # Measure sequence length and initialize result variables to 0
    length = len(seq)
    a, t, c, g = 0, 0, 0, 0         # result variables

    # Iterate through the sequence, counting each result variable
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

    # Compile results into a list
    result = [a, t, c, g]

    # Return the results
    return result
