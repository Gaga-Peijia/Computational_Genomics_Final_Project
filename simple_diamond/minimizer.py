import hashlib
def find_unique_minimizers_with_min_hash(sequence, k, w, shape, query):
    """
    Find unique minimizers in a given sequence based on minimum hash value.

    :param sequence: The input sequence (string).
    :param k: The size of k-mer.
    :param w: The window size.
    :return: A list of tuples (minimizer, position).
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

    # Initialize the list to store unique minimizers
    minimizers = []
    seen_minimizers = set()

    # Slide the window across the sequence
    for i in range(len(sequence) - w + 1):
        window = sequence[i:i+w]
        min_kmer, min_pos = min(generate_kmers(window, k), key=lambda x: hash_kmer(x[0]))
        # Check if the minimizer has already been seen
        if min_kmer not in seen_minimizers:
            if query: 
                minimizers.append((min_kmer, min_pos + i))  # Adjust position relative to the entire sequence
            else:
                seq_temp = ""
                for i in range(len(shape)):
                    if shape[i]=="0":
                        seq_temp+="-"
                    else:
                        seq_temp+=min_kmer[i]
                minimizers.append((seq_temp, min_pos + i))  # Adjust position relative to the entire sequence
            seen_minimizers.add(min_kmer)

    return minimizers


sequence = "ACGTGCAATGC"
k = 3  # k-mer size
w = 5  # window size
unique_minimizers = find_unique_minimizers_with_min_hash(sequence, k, w, "101", False)
print(unique_minimizers)