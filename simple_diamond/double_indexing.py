import itertools
import sketching
#import minimizer_test
import sort_merge_join
#import smith_waterman
import datetime



def double_indexing_iterator(query_database, protein_database, reduced_query_database, reduced_protein_database, shapes, sketching_method):
    query_database_seed_hits = {}    
    
    for query in reduced_query_database:
        query_database_seed_hits[query] = {}
        
    for seed_shape_count in range(len(shapes)):       
        protein_list = []
        protein_list_name = []
        shape_length = len(shapes[seed_shape_count])
        first_time = datetime.datetime.now()

        for protein in reduced_protein_database:
            protein_list.append(sketching.find_minimizers(reduced_protein_database[protein], shape_length, 30))
            protein_list_name.append(protein)
        last_time = datetime.datetime.now()
        time = last_time - first_time
        print("Seed structure complete in " + str(time))
        
        for query in reduced_query_database:
            for individual_frame_count in range(len(reduced_query_database[query])):
                first_time = datetime.datetime.now()
                query_dictionary = sketching.find_minimizers(reduced_query_database[query][individual_frame_count], shape_length, 30)
                for protein_list_count in range(len(protein_list)):                    
                    for query_key in query_dictionary:
                        if query_key in protein_list[protein_list_count]:
                            if protein_list_name[protein_list_count] in query_database_seed_hits[query]:
                                if individual_frame_count in query_database_seed_hits[query][protein_list_name[protein_list_count]]:
                                    query_database_seed_hits[query][protein_list_name[protein_list_count]][individual_frame_count] += protein_list[protein_list_count][query_key]
                                    for positions in protein_list[protein_list_count][query_key]:
                                        query_database_seed_hits[query][protein_list_name[protein_list_count]][individual_frame_count].append(positions)
                                else:
                                    query_database_seed_hits[query][protein_list_name[protein_list_count]][individual_frame_count] = []
                                    for positions in protein_list[protein_list_count][query_key]:
                                        query_database_seed_hits[query][protein_list_name[protein_list_count]][individual_frame_count].append(positions)
                            else:
                                query_database_seed_hits[query][protein_list_name[protein_list_count]] = {}
                                query_database_seed_hits[query][protein_list_name[protein_list_count]][individual_frame_count] = []
                                for positions in protein_list[protein_list_count][query_key]:
                                    query_database_seed_hits[query][protein_list_name[protein_list_count]][individual_frame_count].append(positions)          
                last_time = datetime.datetime.now()
                time = last_time - first_time
                print("1 iter complete in " + str(time))
    print(query_database_seed_hits)
    """        
                #merged_dict = sort_merge_join.sort_merge_join_dicts(query_dictionary, , shape)

                
                for protein_dictionary_count in range(len(protein_list)):
                   # if protein_list[protein_dictionary_count] == 
                   print("Hi")
    """

                     
        
        
        
    """
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
            first_time = datetime.datetime.now()
            merged_dict = sort_merge_join.sort_merge_join_dicts(minimizer_sequences, protein_list[0], shape)
            last_time = datetime.datetime.now()
            print(last_time - first_time)
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
    """


