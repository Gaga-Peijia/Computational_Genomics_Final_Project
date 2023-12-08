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
    gap_cost=5
    
    # Initialize the scoring matrix
    m, n = len(seq1), len(seq2)
    score_matrix = np.zeros((m + 1, n + 1), dtype=int)
    
    # Track the maximum score
    max_score = 0
    max_pos = (0, 0)

    # Fill in the scoring matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match = score_matrix[i-1, j-1] + SingleBaseCompare(seq1,seq2,i-1,j-1, penalty_matrix)
            delete = score_matrix[i-1, j] - gap_cost
            insert = score_matrix[i, j-1] - gap_cost
            score = max(0, match, delete, insert)
            score_matrix[i, j] = score
            
            if score > max_score:
                max_score = score
                max_pos = (i, j)

    # Traceback to get the aligned sequences
    align1, align2 = "", ""
    aligning = ""
    i, j = max_pos
    while score_matrix[i, j] > 0:
        score = score_matrix[i, j]
        diag = score_matrix[i-1, j-1]
        up = score_matrix[i, j-1]
        left = score_matrix[i-1, j]
        
        if score == diag + SingleBaseCompare(seq1,seq2,i-1,j-1, penalty_matrix):
            if seq1[i-1]==seq2[j-1]:
                aligning+="|"
            else:
                aligning+=" "
                
            align1 += seq1[i-1]
            align2 += seq2[j-1]
            i -= 1
            j -= 1
        elif score == left - gap_cost:
            align1 += seq1[i-1]
            align2 += '-'
            aligning+=" "
            i -= 1
        elif score == up - gap_cost:
            align1 += '-'
            align2 += seq2[j-1]
            aligning+=" "
            j -= 1
    align_score = 0
    blosum_score = 0
    gapcount_seq1 = 0
    gapcount_seq2 = 0
    for k in range(0, len(align1)):
        if align1[k]!='-' and align2[k]!='-':
            if align1[k]== align2[k]:
                align_score += 1
            scoring = SingleBaseCompare(align1,align2,k,k, penalty_matrix)
            blosum_score += scoring
            if k-1>=0 and align1[k-1]=='-':
                blosum_score-=11+gapcount_seq1
                gapcount_seq1 = 0
            elif k-1>=0 and align2[k-1]=='-':
                blosum_score-=11+gapcount_seq2
                gapcount_seq2 = 0
    align_score = float(align_score)/len(align1)
    
    return aligning, align1, align2, align_score,blosum_score

#VFADLLRTLSWKLGVHGSLCPGFQCQYERRVCARGGGDTCWCIARR', 'SLLICYVPSHGSESDMVKVYAPASSANMSVGFDVLGAAVTPVDGALLG', 'LCSATYPLMEVRSLTWLKFMPRLPVPIASGLMCSGRRHLLMVHCSE', 'SPSNAPSTGVTAAPSTSNPTLILALEAGATLTMSDSLPEGTQISKD', 'LRAMHHQQVSPPPRAHQTRRSYWHWKPGHKL*PCQTPNFHERVRSRSAK', 'SEQCTINRCHRRPEHIKPDAHIGTGSRGINFNHVRLLTSMRGYVADQQR']
seq1 = "SPSNAPSTGVTAAPSTSNPTLILALEAGATLTMSDSLPEGTQISKD"
seq2 = "MLYKGDTLYLDWLEDGIAELVFDAPGSVNKLDTATVASLGEAIGVLEQQSDLKGLLLRSNKAAFIVGADITEFLSLFLVPEEQLSQWLHFANSVFNRLEDLPVPTIAAVNGYALGGGCECVLATDYRLATPDLRIGLPETKLGIMPGFGGSVRMPRMLGADSALEIIAAGKDVGADQALKIGLVDGVVKAEKLIEGAMAILRQAINGDLDWKAKRQPKLEPLKLSKIEATMSFTIAKGMVAQTAGKHYPAPITAVKTIEAAARFGREEALNLENKSFVPLAHTNEARALVGIFLNDQYVKGKAKKLTKDVETPKQAAVLGAGIMGGGIAYQSAWKGVPVIMKDINDKSLALGMTEAAKLLNKQLERGKIDGLKLAGVISTIHPTLDYAGFERVDVVVEAIVENPKVKKAVLAETEQKVRPDTVLASNTSTIPISELANALERPENFCGMHFFNPVHRMPLVEIIRGEKSSDETIAKVVAWASKMGKTPIVVNDCPGFFVNRVLFPYFAGFSQLLRDGADFRKIDKVMEKQFGWPMGPAYLLDVVGIDTAHHAQAVMAAGFPQRMQKDYRDAIDALFDANRFGQKNGLGFWHYKEDSKGKPKKEEDAAVDDLLAEVSQPKRDFSEEEIIARMMIPMVNEVVRCLEEGIIATPAEADMALVYGLGFPPFHGGAFRWLDTLGSAKYLDMAQQYQHLGPLYEVPEGLRNKARHNEPYYPPVEPARPVGDLKTA"
aligning, align_1, align_2, align_score, blosum_score= SMalignment(seq1, seq2, bl.BLOSUM(62))
print(len(align_1))
print(align_1)
print(aligning)
print(align_2)
print("Alignment Score:", align_score)
print("Alignment Score:", blosum_score)

