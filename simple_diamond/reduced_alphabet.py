def reduce_sequence(sequence):
    # Define the mapping of amino acids to the reduced alphabet
    reduced_alphabet = {
        'K': '1', 'R': '1', 'E': '1', 'D': '1', 'Q': '1', 'N': '1',  # [KREDQN]
        'C': '2',                                                   # [C]
        'G': '3',                                                   # [G]
        'H': '4',                                                   # [H]
        'I': '5', 'L': '5', 'V': '5',                               # [ILV]
        'M': '6',                                                   # [M]
        'F': '7',                                                   # [F]
        'Y': '8',                                                   # [Y]
        'W': '9',                                                   # [W]
        'P': '0',                                                   # [P]
        'S': 'A', 'T': 'A', 'A': 'A'                                # [STA]
    }

    # Translate the sequence to the reduced alphabet
    reduced_sequence = ''.join(reduced_alphabet.get(aa, '*') for aa in sequence)
    return reduced_sequence

# Example usage
"""
original_sequence = "MSTNPKPQRKCCSCCLGRGECRASVG*KCSTSSLCSKCGCACGTG"
reduced_sequence = reduce_sequence(original_sequence)
print("Original:", original_sequence)
print("Reduced:", reduced_sequence)
"""