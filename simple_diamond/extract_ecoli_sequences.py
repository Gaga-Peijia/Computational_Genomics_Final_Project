# This Python script will parse a FASTA file and extract only the sequences for E. coli

def extract_ecoli_sequences(input_file_path, output_file_path):
    # Open the input file and the output file
    with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
        # Initialize a variable to keep track of whether to write the current sequence
        write_sequence = False
        
        # Read through each line in the file
        for line in infile:
            # If the line starts with ">", it's a description line
            if line.startswith('>'):
                # Check if "Escherichia coli" is in the description line
                if 'Escherichia coli' in line:
                    write_sequence = True
                    # Write the description line to the output file
                    outfile.write(line)
                else:
                    write_sequence = False
            # If we're currently within an E. coli sequence, write the line
            elif write_sequence:
                outfile.write(line)


input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

extract_ecoli_sequences(input_file_path, output_file_path)
