import minimizer_test
import sort_merge_join
import smith_waterman



def double_indexing_naive_iterator(query_database, protein_database, reduced_query_database, reduced_protein_database, shapes):
    hash_table_
    

def double_indexing_iterator(query_database, protein_database, reduced_query_database, reduced_protein_database, shape):
    protein_list = []
    protein_list_name = []
    shape_length = len(shape)

    
    for protein in reduced_protein_database:
        print(protein)
        protein_list.append(minimizer_test.find_unique_minimizers_with_min_hash_dict(reduced_protein_database[protein], shape_length, 27))
        protein_list_name.append(protein)
        
    a = []
    b = []
    for query in reduced_query_database:
        max_score = 0
        best_frame = 0
        frame_count = 0
        for individual_frame in reduced_query_database[query]:
            minimizer_sequences = minimizer_test.find_unique_minimizers_with_min_hash_dict(individual_frame, shape_length, 27)
            merged_dict = sort_merge_join.sort_merge_join_dicts(minimizer_sequences, protein_list[0], shape)
            
            for seed, positions in merged_dict.items():
                for query_seed_pos in positions[0]:
                    for reference_seed_pos in positions[1]:
                        alignment = smith_waterman.extend_seed_bilaterally(query_database[query][frame_count], protein_database[protein_list_name[0]], query_seed_pos, reference_seed_pos, shape_length)
                        print(alignment[2])
                        if alignment[2] > max_score:
                            max_score = alignment[2]
                            best_frame = frame_count
            frame_count +=1
        a.append(max_score)
        b.append(best_frame)    
    print(a)
    print(b)
    return 1, 2




