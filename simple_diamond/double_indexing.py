import itertools
import sketching
import sort_merge_join
import datetime
import blosum as bl
import full_smithwaterman

BLOSUM62 = bl.BLOSUM(62)

def best_match(dict, querydatabase, protein_database,seed_length):
    with open("alignment_results.txt", "w") as file:
        #initialize the local variable
        query_seq = ""
        query_len = 0
        best_reading_frame_score = 0
        best_reading_frame = 0
        starting_position_of_reference = 0
        edge = 0
        reading_frame_list = []
        protein_sequence_length = 0
        for item in dict:
            #item is the name of the query
            for protein_name in dict[item]:
                protein_seq = protein_database[protein_name]
                protein_sequence_length = len(protein_seq)
                for reading_frame in dict[item][protein_name]:
                    #reset the variable every time we traverse each reading frame
                    query_seq = querydatabase[item][reading_frame]
                    query_len = len(query_seq)
                    best_reading_frame_score = 0
                    best_reading_frame = 0
                    starting_position_of_reference = 0
                    edge = 0
                    #reginal smithwarterman
                    #need to convert set to list and sort it 
                    reading_frame_list = list(dict[item][protein_name][reading_frame])
                    reading_frame_list.sort()
                    for index in reading_frame_list:
                        if index>=edge:  # it should be >= since edge can be 0
                            start = max(0, index - query_len)
                            end = min(protein_sequence_length, index + seed_length + query_len)
                            edge = end  #extending the edge
                            sequence_snippet = protein_seq[start:end]
                            aligning_sequence, query_align, protein_align, score = full_smithwaterman.SMalignment(query_seq, sequence_snippet, BLOSUM62)
                            if score>best_reading_frame_score:
                                best_reading_frame_score = score
                                starting_position_of_reference = start
                                if best_reading_frame!=reading_frame:
                                    best_reading_frame = reading_frame
                #after each iteration
                file.write(f"{item}\t{protein_name}\t{best_reading_frame_score}\t{starting_position_of_reference}\t{best_reading_frame}\n")    
                    #return aligning_sequence, align_seq1, align_seq2, align_score
                    




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
    print(query_database_seed_hits)
    best_match(query_database_seed_hits, query_database, protein_database, len(max(shapes, key=len)))