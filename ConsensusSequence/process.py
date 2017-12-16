from __future__ import division
import numpy as np


def keywithmaxval(d):

     """ a) create a list of the dict's keys and values;
         b) return the key with the max value"""

     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]


def consensusSequence(inputSeqs):

    for char in inputSeqs:
        if char != ',':
            char = char.upper()

    seqs = inputSeqs.split(',')
    length = len(seqs[0])
    array = np.array(seqs)

    consensus = []
    for i in range(0, length):
        a, t, c, g = 0, 0, 0, 0
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
        x = {
            'A': a, 'T': t,
            'C': c, 'G': g
        }
        consensus.append(keywithmaxval(x))

    consensus = ''.join(consensus)
    return consensus
