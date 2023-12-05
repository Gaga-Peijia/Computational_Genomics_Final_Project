def filter_fasta_by_length(input_file, output_file, min_length):
    """
    Filters sequences in a FASTA file that are at least a certain length.

    :param input_file: Path to the input FASTA file.
    :param output_file: Path to the output FASTA file.
    :param min_length: Minimum length of sequences to be included in the output.
    """
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        sequence = ''
        header = ''
        for line in infile:
            if line.startswith('>'):
                if len(sequence) >= min_length:
                    outfile.write(header + '\n' + sequence + '\n')
                header = line.strip()
                sequence = ''
            else:
                sequence += line.strip()
        # Check the last sequence in the file
        if len(sequence) >= min_length:
            outfile.write(header + '\n' + sequence + '\n')

if __name__ == "__main__":
    input_path = input("Enter the path of the input FASTA file: ")
    output_path = input("Enter the path of the output FASTA file: ")
    min_len = int(input("Enter the minimum length for sequences: "))

    filter_fasta_by_length(input_path, output_path, min_len)
