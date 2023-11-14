import random

def random_sample(file,sample_len=150,number_of_samples=10000):
    """
    Randomly sample a FASTA file.
    """
    with open (file, 'r') as f:
        lines=f.readlines()
    #print(len(lines))
    #concate all lines
    seq=''
    for line in lines[1:]:
        seq+=line.strip()
    #print(len(seq))
    # generate 
    random_number=random.sample(range(0, len(seq)-sample_len), number_of_samples)
    random_number.sort()
    #writing to file
    with open('random_samples.fastq', 'w') as f:
        for i in random_number:
            f.write('>sample_'+str(i)+'\n')
            f.write(seq[i:i+sample_len]+'\n')

def codon_to_amino_acid(codon):
    """
    Convert a DNA codon to its corresponding amino acid.
    """
    # Codon table
    codon_table = {
        'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
        'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
        'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
        'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
        'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
        'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*',
        'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W',
        'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }

    # Return the amino acid or a placeholder for unknown codons
    return codon_table.get(codon.upper(), '?')

#convert mer to protein
def kmer_to_protein(kmer_index):
    """
    Convert a DNA kmer index to its corresponding amino acid index.
    """
    protein_dinx={}
    for kmer,idx in kmer_index.items():
        protein=codon_to_amino_acid(kmer)
        if protein in protein_dinx:
            protein_dinx[protein].append(idx)
        protein_dinx[protein]=idx
    return protein_dinx
def reads_to_protein(reads):
    """
    Convert a DNA read to its corresponding amino acid index.
    """
    protein_read=''
    for i in range(len(reads)//3):
        read=reads[i*3:i*3+3]
        protein=codon_to_amino_acid(read)
        protein_read+=protein
    return protein_read
def get_kmers_index(seq, k=3):
    """
    Generate all kmers of length k in a DNA sequence.
    """
    kmers=[]
    for i in range(len(seq)-k+1):
        kmers.append(seq[i:i+k])
    index={}
    for i in range(len(kmers)):
        if kmers[i] in index:
            index[kmers[i]].append(i)
        else:
            index[kmers[i]]=[i]
    return index

def reverse_complement(read):
    """
    Generate the reverse complement of a DNA sequence.
    """
    # Generate the reverse complement
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    reverse_complement = ''.join(complement.get(base, base) for base in reversed(read))
    return reverse_complement
def six_frame(read):
    """
    Generate the six reading frames of a DNA sequence, including the reverse
    complement.
    """
    # Generate the forward frames
    frames = [read[i:] for i in range(3)]
    # Generate the reverse frames
    frames.extend([reverse_complement(read[i:]) for i in range(3)])
    return frames

def read_six_frame_protein_index(read):
    """
    Generate the six reading frames of a DNA sequence, 
    including the reverse then convert to protein index.
    """
    six_frames=six_frame(read)
    # print(six_frames)
    protein_reads=[reads_to_protein(six_frames[i]) for i in range(len(six_frames))]
    # print(protein_reads)
    protein_indexs=[get_kmers_index(protein_reads[i]) for i in range(len(protein_reads))]
    return protein_indexs
