from smith_waterman import *
from read_fasta import *
import os


def find_best_alignment(DNA_query,protein_database):
    '''
        DNA_query: dictionary of DNA query sequences
        protein_database: dictionary of protein database sequences
        return the name of the best match protein database, and the alignment
    '''
    max_score = -100000
    max_score_name = ""
    max_score_alignment = []
    for data_name,data_protein in protein_database.items():
        for query_name,query_protein in DNA_query.items():
            for query in query_protein:
                alignment = extend_seed_bilaterally(query, data_protein,4,4)
                score=alignment[2]
                if score>max_score:
                    max_score=score
                    max_score_name=data_name
                    max_score_alignment=alignment
                
    return max_score_name,max_score_alignment
#example usage
if __name__=='__main__':
    CURR_DIR = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(CURR_DIR,'test_DNA_query.fasta')) as protein_database:
        DNA_query = protein_database.readlines()
    with open(os.path.join(CURR_DIR,'test_protein_database.fasta')) as protein_database:
        protein_database = protein_database.readlines()
    DNA_query,_ = read_fasta_for_DNA(DNA_query)
    protein_database,_ = read_fasta_for_proteins(protein_database)
    # print("DNA query:",DNA_query)
    max_score_name,alignment = find_best_alignment(DNA_query,protein_database)
    print("best match protein database name:",max_score_name)
    print("database alignment:",alignment[1])
    print("query alignment:",alignment[0])
    print("score:",alignment[2])
