"""
Extract sequences from E.coli strain k12 from uniprot database
"""

def extract_ecoli_k12_data(fasta_file, output_file):
    with open(fasta_file, 'r') as file:
        lines = file.readlines()

    ecoli_k12_data = []
    capture = False

    for line in lines:
        if line.startswith('>'):
            if 'Escherichia coli (strain K12)' in line: 
                capture = True
                ecoli_k12_data.append(line)
            else:
                capture = False
        elif capture:
            ecoli_k12_data.append(line)

    with open(output_file, 'w') as file:
        file.writelines(ecoli_k12_data)

fasta_file = 'uniprot_sprot.fasta'
output_file = 'uniprot_sprot_ecoli_k12.fasta'
extract_ecoli_k12_data(fasta_file, output_file)
