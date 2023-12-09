"""
Generate the accuracy scores comparing the output of blast and that of diamond
"""

# Function to read data from a text file and store it in a set
def read_data(file_path):
    data = set()
    with open(file_path, 'r') as infile:
        for line_number, line in enumerate(infile, start=1):
            parts = line.strip().split()  # Split the line into parts
            if len(parts) < 2:  # Check if the line has at least two parts
                print(f"Skipping line {line_number}: not enough parts. Line content: {line}")
                continue  # Skip this line

            sample_number = parts[0].strip('>')  # Remove '>' if present
            try:
                protein_name = parts[1].split('|')[1]  # Get the protein name
                data.add((sample_number, protein_name))
            except IndexError:
                print(f"Skipping line {line_number}: protein name split error. Line content: {line}")
    return data

algorithm_output_path = '/home/cgf2312/Desktop/CGS/CGS_project/blastx_output_highest_ecoli_30_30.txt'
blast_output_path = '/home/cgf2312/Desktop/CGS/CGS_project/Computational_Genomics_Final_Project/simple_diamond/minimizer_alignment_results.txt'


algorithm_data = read_data(algorithm_output_path)
blast_data = read_data(blast_output_path)

matches = algorithm_data & blast_data  # Intersection of both sets gives the matches

total_blast_lines = len(blast_data)
matches_count = len(matches)
score_percentage = (matches_count / total_blast_lines) * 100 if total_blast_lines > 0 else 0

print(f"Number of Matches: {matches_count}")
print(f"Matching Score: {score_percentage:.2f}%")
