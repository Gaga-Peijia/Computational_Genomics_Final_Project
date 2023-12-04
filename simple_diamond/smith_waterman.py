from Bio.Align import substitution_matrices

def calculate_seed_score(seq1, seq2, start_pos1, start_pos2, seed_length):
    blosum62 = substitution_matrices.load("BLOSUM62")
    score = 0
    for i in range(seed_length):
        pair = (seq1[start_pos1 + i], seq2[start_pos2 + i])
        score += blosum62.get(pair, blosum62.get(tuple(reversed(pair)), 0))
    return score

def extend_seed_bilaterally(seq1, seq2, start_pos1, start_pos2, seed_length=3, threshold=-5):
    blosum62 = substitution_matrices.load("BLOSUM62")
    gap_penalty = -1

    # Calculate initial score of the seed
    initial_score = calculate_seed_score(seq1, seq2, start_pos1, start_pos2, seed_length)
    alignment1, alignment2 = seq1[start_pos1:start_pos1 + seed_length], seq2[start_pos2:start_pos2 + seed_length]
    score = initial_score
    max_score = score
    extension = 1
    # Extend bilaterally from the ends of the seed
    while True:
        # Extend left
        if (start_pos1 - extension<0 or start_pos2 - extension<0) and (start_pos1 + seed_length-1 + extension >= len(seq1)or start_pos2 + seed_length-1 + extension >= len(seq2)):
            break
        if start_pos1 - extension >= 0 and start_pos2 - extension >= 0:
            left1, left2 = seq1[start_pos1 - extension], seq2[start_pos2 - extension]
            score += blosum62.get((left1, left2), blosum62.get((left2, left1), gap_penalty))
            #if score < threshold:
            #    break
            alignment1 = left1 + alignment1
            alignment2 = left2 + alignment2
            #max_score = max(max_score, score)

        # Extend right
        if start_pos1 + seed_length-1 + extension < len(seq1) and start_pos2 + seed_length-1 + extension < len(seq2):
            right1, right2 = seq1[start_pos1 + seed_length-1 + extension], seq2[start_pos2 + seed_length-1 + extension]
            score += blosum62.get((right1, right2), blosum62.get((right2, right1), gap_penalty))
            #if score < threshold:
            #    break
            alignment1 += right1
            alignment2 += right2
            #max_score = max(max_score, score)
        if score < threshold:
            break
        max_score = max(max_score, score)
        extension+=1

    return alignment1, alignment2, max_score

# Example usage
"""
query_seq = "PALADIN"
ref_seq = "PALIDIN"
seed_start_pos1 = 4  # Example start position of the seed in query_seq
seed_start_pos2 = 4  # Example start position of the seed in ref_seq
alignment = extend_seed_bilaterally(query_seq, ref_seq, seed_start_pos1, seed_start_pos2)
print("Extended Alignment:\n", alignment[0], "\n", alignment[1], "\nScore:", alignment[2])
"""
