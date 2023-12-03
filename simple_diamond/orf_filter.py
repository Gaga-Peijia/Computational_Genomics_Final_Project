import sys

def read_fasta(input_file):
    with open(input_file, encoding="utf-8") as myFile:
        input_seq = myFile.readlines()
    return input_seq

def generate_orf_filter(input_file, output_file, threshold):
    seq_name = ""
    current_seq = ""
    output_text = []
    input_seq = read_fasta(input_file)
    
    # now we extract each sequence 
    # first we get the name of the sequence
    #second we deal with the six frame of the corresponding sequence

    for line in input_seq:
        if line[0] == ">":
            seq_name = line.strip()
        else:
            current_seq = line.strip()
            #now we deal with the sequence: 1. we need to get the forward three frames
            #then we need to get the reverse compliment and get the three frames from that 
            if analyze_dna_frames(current_seq, threshold)==False:
                ## if the function return false=> means at least one frame has no stop codon
                ## we will add this sequence to the output file
                output_text.append(seq_name)   
                output_text.append(current_seq)
    with open(output_file, 'w') as out_fh:
        for line in output_text:
            out_fh.write(line+"\n")
            
            
def complement(nucleotide):
    complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return complements.get(nucleotide, '')

def reverse_complement(seq):
    return ''.join(complement(n) for n in reversed(seq))

def truncate_seq(seq,  threshold):
    if not 0 <= threshold <= 1:
        raise ValueError("Threshold must be between 0 and 1")
    truncated_length = int(len(seq) * threshold)
    return seq[:truncated_length]

def analyze_dna_frames(sequence, threshold):
    stop_codon = ["TAA", "TAG", "TGA"]
    stop_count = 0
    forward_seq = truncate_seq(sequence, threshold)
    reverse_sequence = truncate_seq(reverse_complement(sequence), threshold)
    
    # Analyze forward frames
    for frame in range(3):
        for i in range(frame, len(forward_seq), 3):
            codon = forward_seq[i:i+3]
            if codon in stop_codon:
                stop_count+=1
                break
    # Analyze reverse frames
    for frame in range(3):
        for i in range(frame, len(reverse_sequence), 3):
            codon = reverse_sequence[i:i+3]
            if codon in stop_codon:
                stop_count+=1
                break
            
    if stop_count==6:
        return True
    else:
        return False

input_file = sys.argv[1]
output_file = sys.argv[2]
threshold = 0.9
generate_orf_filter(input_file, output_file, threshold=0.5) 