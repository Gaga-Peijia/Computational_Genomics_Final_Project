"""
Generate the accuracy scores comparing the output of blast and that of diamond
"""

# Function to read data from a BLAST output file and store it in a set
def read_data(file_path):
    data = set()
    with open(file_path, 'r') as infile:
        for line in infile:
            parts = line.strip().split()  # Split the line into parts
            if len(parts) < 2:  # Check if the line has at least two parts
                print(f"Skipping line: not enough parts. Line content: {line}")
                continue  # Skip this line

            sample_number = parts[0]
            protein_name = parts[1]
            data.add((sample_number, protein_name))  # Add the tuple to the set
    return data

blast_output_path = '/home/cgf2312/Desktop/CGS/CGS_project/Computational_Genomics_Final_Project/matches_diamond_highest.tsv'
diamond_output_path = '/home/cgf2312/Desktop/CGS/CGS_project/blastx_output_highest_ecoli_30_30.txt'

blast_data1 = read_data(blast_output_path)
blast_data2 = read_data(diamond_output_path)

matches = blast_data1 & blast_data2  # Intersection of both sets gives the matches

total_lines_in_second_blast = len(blast_data2)
matches_count = len(matches)
score_percentage = (matches_count / total_lines_in_second_blast) * 100 if total_lines_in_second_blast > 0 else 0

print(f"Number of Matches: {matches_count}")
print(f"Matching Score: {score_percentage:.2f}%")
