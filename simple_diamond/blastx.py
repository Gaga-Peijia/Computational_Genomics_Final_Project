import sys
import subprocess
import time
from datetime import timedelta

def run_blastx(dna_reads_path, protein_db_path, output_path, time_log_path):
    """
    Run BLASTx to align DNA reads to a protein database and record the execution time.

    Parameters:
    dna_reads_path (str): Path to the DNA reads file.
    protein_db_path (str): Path to the protein database file.
    output_path (str): Path to save the output file.
    time_log_path (str): Path to save the execution time log.
    """
    try:
        start_time = time.monotonic()
        
        # Construct the BLASTx command
        command = [
            'blastx',
            '-query', dna_reads_path,
            '-db', protein_db_path,
            '-out', output_path,
            '-outfmt', '6'  # Change this number for different output formats
        ]

        # Run the BLASTx command
        subprocess.run(command, check=True)
        
        end_time = time.monotonic()
        elapsed_time = timedelta(seconds=end_time - start_time)
        
        # Print and save the execution time
        with open(time_log_path, 'w') as f:
            f.write(f"Time taken to run the script: {elapsed_time}\n")
        
        print(f"BLASTx completed successfully. Output saved to {output_path}")
        print(f"Time taken to run the script: {elapsed_time}")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running BLASTx: {e}")


dna_reads_path = sys.argv[1]
protein_db_path = sys.argv[2]
output_path = sys.argv[3]
time_log_path = sys.argv[4]

run_blastx(dna_reads_path, protein_db_path, output_path, time_log_path)
