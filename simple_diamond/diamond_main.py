import sys
import argparse
import read_fasta
import full_smithwaterman
import double_indexing
from alignment import *



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
# print(query_dictionary)

if args.extension == "full_sw":
    alignments=find_best_alignment(query_dictionary, protein_database_dictionary)
    with open("alignments.txt", "w") as f:
        for query_name,query_matches in alignments.items():
            for match in query_matches:
                f.write(f"{query_name}\t{match['data_name']}\t{match['score']}\t{match['frame']}\t{match['position']}\n")
            


elif args.extension == "regional_sw":
    sketching_technique = args.sketching
    if sketching_technique == "uniform":
        double_indexing.double_indexing_iterator(query_dictionary, 
                                                 protein_database_dictionary, 
                                                 query_dictionary_reduced, 
                                                 protein_database_dictionary_reduced, 
                                                 ["111101011101111", "111011001100101111", "1111001001010001001111","111100101000010010010111"], sketching_technique)
    elif sketching_technique == "minimizer":
        double_indexing.double_indexing_iterator(query_dictionary, 
                                                 protein_database_dictionary, 
                                                 query_dictionary_reduced, 
                                                 protein_database_dictionary_reduced, 
                                                 ["111101011101111", "111011001100101111", "1111001001010001001111","111100101000010010010111"], sketching_technique)
    elif sketching_technique == "minhash":
        double_indexing.double_indexing_iterator(query_dictionary, 
                                                 protein_database_dictionary, 
                                                 query_dictionary_reduced, 
                                                 protein_database_dictionary_reduced, 
                                                 ["111101011101111", "111011001100101111", "1111001001010001001111","111100101000010010010111"], sketching_technique)


"""
else:
    print("Extension Settings are as follows:\n\tfull_sw: Performs Smith Waterman between queried protein and reference database\n\tRegional_sw: Performs Smith Waterman between queried protein and reference database")
"""
"""
elif args.extension == "seed_extend":
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



    

