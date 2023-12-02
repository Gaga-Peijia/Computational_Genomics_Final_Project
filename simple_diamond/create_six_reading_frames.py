def translate_codon(codon):
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
    return codon_table.get(codon, 'X')  # 'X' for unknown or invalid codons

def generate_protein_sequences(dna_sequence):
    """Generate protein sequences from the six reading frames of a DNA sequence."""
    protein_sequences = []

    # Forward frames
    for frame in range(3):
        protein_sequence = ''
        for i in range(frame, len(dna_sequence)-2, 3):
            codon = dna_sequence[i:i+3]
            amino_acid = translate_codon(codon)
            protein_sequence += amino_acid
        protein_sequences.append(protein_sequence)

    # Reverse frames
    reverse_complement = dna_sequence[::-1].translate(str.maketrans('ACGT', 'TGCA'))
    for frame in range(3):
        protein_sequence = ''
        for i in range(frame, len(reverse_complement)-2, 3):
            codon = reverse_complement[i:i+3]
            amino_acid = translate_codon(codon)
            protein_sequence += amino_acid
        protein_sequences.append(protein_sequence)

    return protein_sequences

# Example DNA sequence
example_dna_sequence = "ATGGTCTACATAGCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGTGGGCACCTGGAGCCACCGCGCCTTCGACCCCGCCCGGAGCCCTCCCTCCTCCAGCCCTCCTCCACCTCCGCCTCCCTCCTCCAGCCCTCCTCCACCTCCGCCTCCCTCCTCCAGCCCTCCTCCACCTCCGCCTCCCTCCTCCGCCCACCCAGCCTCCAGCCCTCCACCCACCTCCAGCCCTCCAGCCCTCCAGCCCTCCAGCCCTCCAGCCTCCACCCACCTCCAGCCCTCCAGCCCTCCAGCCCTCCAGCCTCCAGCCCTCCAGCCCTCCAGCCCTCCAGCCTCCAGCCCTCCAGCCTCCAGCCCTCCAGCCTCCAGCCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCC"
print(generate_protein_sequences(example_dna_sequence))