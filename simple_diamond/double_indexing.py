import itertools
import minimizer_test
import sort_merge_join

def merge_indices(query_index, reference_index):
    # Merge the two indices and yield matching pairs
    for query, ref in itertools.product(query_index, reference_index):
        if query[0] == ref[0]:  # If the encoded seeds match
            yield query, ref


def double_indexing_iterator(query_database, protein_database):
    protein_list = []
    
    for protein in protein_database:
        protein_list.append(minimizer_test.find_unique_minimizers_with_min_hash_dict(protein_database[protein], 15, 30))
    
    for query in query_database:
        max_score = 0
        best_frame = 0
        for individual_frame in query_database[query]:
            minimizer_sequences = minimizer_test.find_unique_minimizers_with_min_hash_dict(individual_frame, 15, 30)
            merged_dict = sort_merge_join.sort_merge_join_dicts(minimizer_sequences, protein_list[0], "111110111111111")

        
    
    return 1, 2



