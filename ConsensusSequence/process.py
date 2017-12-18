from __future__ import division
import numpy as np


# keywithmaxval() returns the key in a dict with the highest corresponding value

def keywithmaxval(d):

    # Store keys and values in ORDERED lists
    v = list(d.values())
    k = list(d.keys())

    # Return the key whos corresponding value is highest
    return k[v.index(max(v))]


# consensusSequence() returns the consensus sequence over two sequence strings

def consensusSequence(inputSeqs):

    # Iterate through sequence, capitalize and split on commas
    for char in inputSeqs:
        if char != ',':
            char = char.upper()
    seqs = inputSeqs.split(',')

    # Measure length of first sequence
    length = len(seqs[0])

    # Store sequences in a numpy array
    array = np.array(seqs)

    # Initialize consensus to an empty list
    consensus = []

    # Iterate from from 0 to length
    for i in range(0, length):
        a, t, c, g = 0, 0, 0, 0

        # Iterate over all lists in array, tallying sequence data
        for vector in array:
            if vector[i] == None:
                pass
            elif vector[i] == 'A':
                a += 1
            elif vector[i] == 'T':
                t += 1
            elif vector[i] == 'C':
                c += 1
            else:
                g += 1

        # Define a local dict structure to store key:values for each index
        x = {
            'A': a, 'T': t,
            'C': c, 'G': g
        }

        # Consensus value is the key with max value in local dict
        consensus.append(keywithmaxval(x))

    # Convert consensus list into a consensus string
    consensus = ''.join(consensus)

    # Return consensus string
    return consensus
