from __future__ import division
import numpy as np

def keywithmaxval(d):
     """ a) create a list of the dict's keys and values;
         b) return the key with the max value"""
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

def consensusSequence(check, against):
    tuples = []
    checklist = list(check)
    againstlist = list(against)
    tuples.append(checklist)
    tuples.append(againstlist)
    array = np.array(tuples)
    return array
