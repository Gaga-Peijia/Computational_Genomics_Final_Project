import sys
import argparse
import read_fasta
import full_smithwaterman
#import double_indexing



#read in the fata from protein database and query


parser = argparse.ArgumentParser()
parser.add_argument('--query', type=str, required=True)
parser.add_argument('--protein_database', type=str, required=True)
parser.add_argument('--extension', type=str, required=True)
parser.add_argument('--sketching', type=str, required=False)
parser.add_argument('--save_path',  type=str, required=True)
args = parser.parse_args()


with open(args.query, encoding="utf-8") as myFile:
    query_sequences  = myFile.readlines()
    
with open(args.protein_database, encoding="utf-8") as myFile:
    protein_database_sequences  = myFile.readlines()


query_dictionary, query_dictionary_reduced = read_fasta.read_fasta_for_DNA(query_sequences)
protein_database_dictionary, protein_database_dictionary_reduced = read_fasta.read_fasta_for_proteins(protein_database_sequences)

if args.extension == "full_sw":
    full_smithwaterman.run_full_smithwaterman()

"""
elif args.extension == "regional_sw":
    sketching_technique = args.sketching
    match sketching_technique:
        case "uniform": 
            output_file = double_indexing.double_indexing_naive_iterator()
        case "minimizer":
            output_file = double_indexing.double_indexing_naive_iterator()
        case "minhash":
            output_file = double_indexing.double_indexing_naive_iterator()

else:
    sketching_technique = args.sketching
    match sketching_technique:
        case "uniform": 
            output_file = double_indexing.double_indexing_naive_iterator()
        case "minimizer":
            output_file = double_indexing.double_indexing_naive_iterator()
        case "minhash":
            output_file = double_indexing.double_indexing_naive_iterator()          
        
    output_file = double_indexing
"""

#sorted_query_reduced, sorted_protein_database_reduced = double_indexing.double_indexing_iterator(query_dictionary, protein_database_dictionary, query_dictionary_reduced, protein_database_dictionary_reduced, "111101101101")



    

