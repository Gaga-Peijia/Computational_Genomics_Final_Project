import hashlib


def find_uniformers(sequence, gap):
    """
    Create a sorted uniform sketch dictionary for a given sequence and gap value.

    :param sequence sequence (str): The input sequence of protein.
    :param gap_value (str): The value to represent gaps in the sketch.

    :return: A dictionary representing the sorted uniform sketch of the sequence.
    """
    
    sketch_dict = {}
    for i in range(0, len(sequence), gap):
        seed = sequence[i:i + gap]

        if seed not in sketch_dict:
            sketch_dict[seed] = {i}
        else:
            sketch_dict[seed].add(i)
    return sketch_dict  

def find_minhash(dna_sequence, seed_length, number_of_hashes):
    """
    Perform minhash sketching on the 5 smallest hash value sequences of size n in a given DNA sequence.

    Parameters:
    - dna_sequence (str): The input DNA sequence to be sketched.
    - n (int): The size of the sequences for minhashing.

    Returns:
    - dict: A dictionary with keys as seeds and values as another dictionary of seed starting positions and hash values.
    """

    num_hashes = number_of_hashes
    sketch_dict = {}

    for i in range(len(dna_sequence) - seed_length + 1):
        seed = dna_sequence[i:i + seed_length]

        # Calculate hash values
        hash_values = [int(hashlib.sha256(seed.encode('utf-8') + str(hash_num).encode('utf-8')).hexdigest(), 16)
                       for hash_num in range(num_hashes)]

        # Find the 5 smallest hash values
        smallest_hashes = sorted(enumerate(hash_values), key=lambda x: x[1])[:5]
        for idx, hash_value in smallest_hashes:
            if seed not in sketch_dict:
                sketch_dict[seed] = {i}
            else:
                sketch_dict[seed].add(i)

    return sketch_dict


def find_minimizers(sequence, k, w):
    """
    Find unique minimizers in a given sequence based on minimum hash value.
    Store the results in a dictionary where each key is a unique k-mer and the value is a set of positions.

    :param sequence: The input sequence (string).
    :param k: The size of k-mer.
    :param w: The window size.
    :return: A dictionary with k-mers as keys and sets of positions as values.
    """
    if len(sequence) < k or len(sequence) < w or w < k:
        raise ValueError("Invalid sequence, k, or w values.")

    # Function to generate a hash value for a k-mer
    def hash_kmer(kmer):
        return int(hashlib.md5(kmer.encode()).hexdigest(), 16)

    # Function to generate k-mers from a sequence
    def generate_kmers(seq, k):
        for i in range(len(seq) - k + 1):
            yield seq[i:i+k], i

    # Initialize the dictionary to store unique minimizers
    minimizers_dict = {}

    # Slide the window across the sequence
    for i in range(len(sequence) - w + 1):
        window = sequence[i:i+w]
        min_kmer, min_pos = min(generate_kmers(window, k), key=lambda x: hash_kmer(x[0]))

        # Add the minimizer position to the set in the dictionary
        if min_kmer not in minimizers_dict:
            minimizers_dict[min_kmer] = {min_pos + i}
        else:
            minimizers_dict[min_kmer].add(min_pos + i)

    return dict(sorted(minimizers_dict.items()))
