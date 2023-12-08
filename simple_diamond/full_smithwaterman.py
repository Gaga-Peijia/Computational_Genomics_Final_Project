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
    g = -5
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
            try:
                matrix[siii][sjjj] = max(matrix[siii-1][sjjj] + g, matrix[siii - 1][sjjj - 1] + SingleBaseCompare(seq1,seq2,siii, sjjj,penalty_matrix), matrix[siii][sjjj-1] + g)
            except:
                print(siii, sjjj)
                print(seq1, seq2)
                # print(matrix)
                exit()
    sequ1 = [seq1[m-1]]
    sequ2 = [seq2[n-1]]
    while m > 1 and n > 1:
        if max(matrix[m-1][n-2], matrix[m-2][n-2], matrix[m-2][n-1]) == matrix[m-2][n-2]:
            m -= 1
            n -= 1
            sequ1.append(seq1[m-1])
            sequ2.append(seq2[n-1])
        elif max(matrix[m-1][n-2], matrix[m-2][n-2], matrix[m-2][n-1]) == matrix[m-1][n-2]:
            n -= 1
            sequ1.append('-')
            sequ2.append(seq2[n-1])
        else:
            m -= 1
            sequ1.append(seq1[m-1])
            sequ2.append('-')
    sequ1.reverse()
    sequ2.reverse()
    align_seq1 = ''.join(sequ1)
    align_seq2 = ''.join(sequ2)
    align_score = 0.
    gapcount_seq1 = 0
    gapcount_seq2 = 0
    '''
    for k in range(0, len(sequ1)):
        scoring = SingleBaseCompare(sequ1,sequ2,k,k, penalty_matrix)
        align_score += scoring
    '''
    aligning = []
    for k in range(0, len(sequ1)):
        if sequ1[k]!='-' and sequ2[k]!='-':
            if sequ1[k]== sequ2[k]:
                aligning.append('|')
            else:
                aligning.append(' ')
            scoring = SingleBaseCompare(sequ1,sequ2,k,k, penalty_matrix)
            align_score += scoring
            if k-1>=0 and sequ1[k-1]=='-':
                align_score-=11+gapcount_seq1
                gapcount_seq1 = 0
            elif k-1>=0 and sequ2[k-1]=='-':
                align_score-=11+gapcount_seq2
                gapcount_seq2 = 0
        elif sequ1[k]=='-':
            aligning.append(' ')
            gapcount_seq1+=1
        elif sequ2[k]=='-':
            aligning.append(' ')
            gapcount_seq2+=1
        
    aligning_sequence = ''.join(aligning)
    

    align_score = float(align_score)
    
    return aligning_sequence, align_seq1, align_seq2, align_score

if __name__=="__main__":
    seq1 = "PPPSRGSRWRN*KLSSIRNLPK*NMSCMALVCWGSARIASTLR*FAVARK"
    seq2 = "MKKVVTVCPYCASGCKINLVVDNGKIVRAEAAQGKTNQGTLCLKGYYGWDFINDTQILTPRLKTPMIRRQRGGKLEPVSWDEALNYVAERLSAIKEKYGPDAIQTTGSSRGTGNETNYVMQKFARAVIGTNNVDCCARVUHGPSVAGLHQSVGNGAMSNAINEIDNTDLVFVFGYNPADSHPIVANHVINAKRNGAKIIVCDPRKIETARIADMHIALKNGSNIALLNAMGHVIIEENLYDKAFVASRTEGFEEYRKIVEGYTPESVEDITGVSASEIRQAARMYAQAKSAAILWGMGVTQFYQGVETVRSLTSLAMLTGNLGKPHAGVNPVRGQNNVQGACDMGALPDTYPGYQYVKDPANREKFAKAWGVESLPAHTGYRISELPHRAAHGEVRAAYIMGEDPLQTDAELSAVRKAFEDLELVIVQDIFMTKTASAADVILPSTSWGEHEGVFTAADRGFQRFFKAVEPKWDLKTDWQIISEIATRMGYPMHYNNTQEIWDELRHLCPDFYGATYEKMGELGFIQWPCRDTSDADQGTSYLFKEKFDTPNGLAQFFTCDWVAPIDKLTDEYPMVLSTVREVGHYSCRSMTGNCAALAALADEPGYAQINTEDAKRLGIEDEALVWVHSRKGKIITRAQVSDRPNKGAIYMTYQWWIGACNELVTENLSPITKTPEYKYCAVRVEPIADQRAAEQYVIDEYNKLKTRLREAALA"
    aligning, align_1, align_2, alignment_score = SMalignment(seq1, seq2, bl.BLOSUM(62))
    print(align_1)
    print(aligning)
    print(align_2)
    print("Alignment Score:", alignment_score)