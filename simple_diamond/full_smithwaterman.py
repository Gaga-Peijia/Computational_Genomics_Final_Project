import re
import numpy as np
from collections import Counter
from math import ceil
from math import floor
import blosum as bl
#need to do:pip install blosum

# compare single base
def SingleBaseCompare(seq1,seq2,i,j, matrix):
    return matrix.get(seq1[i], {}).get(seq2[j], None)
    
def SMalignment(seq1, seq2, penalty_matrix):
    m = len(seq1)
    n = len(seq2)
    
    g = -3
    matrix = []
    for i in range(0, m):
        tmp = []
        for j in range(0, n):
            tmp.append(0)
        matrix.append(tmp)
    for sii in range(0, m):
        matrix[sii][0] = sii*g
    for sjj in range(0, n):
        matrix[0][sjj] = sjj*g
    for siii in range(1, m):
        for sjjj in range(1, n):
            matrix[siii][sjjj] = max(matrix[siii-1][sjjj] + g, matrix[siii - 1][sjjj - 1] + SingleBaseCompare(seq1,seq2,siii, sjjj,penalty_matrix), matrix[siii][sjjj-1] + g)
    sequ1 = [seq1[m-1]]
    sequ2 = [seq2[n-1]]
    align_line = []
    while m > 1 and n > 1:
        if max(matrix[m-1][n-2], matrix[m-2][n-2], matrix[m-2][n-1]) == matrix[m-2][n-2]:
            m -= 1
            n -= 1
            sequ1.append(seq1[m-1])
            sequ2.append(seq2[n-1])
            if seq1[m-1]==seq2[n-1]:
                align_line.append('|')
            else:
                align_line.append(' ')
        elif max(matrix[m-1][n-2], matrix[m-2][n-2], matrix[m-2][n-1]) == matrix[m-1][n-2]:
            n -= 1
            align_line.append(' ')
            sequ1.append('-')
            sequ2.append(seq2[n-1])
        else:
            m -= 1
            sequ1.append(seq1[m-1])
            sequ2.append('-')
            align_line.append(' ')
    sequ1.reverse()
    sequ2.reverse()
    align_line.reverse()
    align_seq1 = ''.join(sequ1)
    align_seq2 = ''.join(sequ2)
    align_lining = ''.join(align_line)
    align_score = 0.
    for k in range(0, len(align_seq1)):
        if align_seq1[k] == align_seq2[k]:
            align_score += 1
    align_score = float(align_score)/len(align_seq1)
    return align_lining, align_seq1, align_seq2, align_score
"""
# Get the BLOSUM62 matrix
BLOSUM62 = bl.BLOSUM(62)
# Example usage
seq1 = "DEAAADEAAA"
seq2 = "DWAADEAAA"
aligning, align_1, align_2, alignment_score = SMalignment(seq1, seq2, BLOSUM62)
print(align_1)
print(aligning)
print(align_2)
print("Alignment Score:", alignment_score)
"""