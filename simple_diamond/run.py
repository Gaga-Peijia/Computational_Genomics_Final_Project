import subprocess
import os
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
python_file=os.path.join(CURR_DIR,'diamond_main.py')
query_file=os.path.join(CURR_DIR,'test_DNA_query.fasta')
protein_database_file=os.path.join(CURR_DIR,'test_protein_database.fasta')

# python diamond_main.py --query test_DNA_query.fasta --protein_database test_protein_database.fasta --extension full_sw --save_path results
subprocess.run(["python", python_file, "--query", query_file, "--protein_database", protein_database_file,
                 "--extension", "full_sw", "--save_path", "results.txt"])