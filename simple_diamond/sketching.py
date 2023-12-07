import hashlib

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
