import reduced_alphabet
import create_six_reading_frames

def read_fasta_for_DNA (query_sequences):
    query_dictionary = {}
    query_dictionary_reduced = {}
    key = ""
    seq = ""
    making_seq = False
    for line in query_sequences:
        if line[0]  == '>' and seq=="":
            # meaning this is the name of the sequence
            #name of the key
            key = line.strip()
        elif line[0]  == '>' and seq!="":
            #now we end the seq
            query_sequences = create_six_reading_frames.generate_protein_sequences(seq)
            reduced_sequences = [reduced_alphabet.reduce_sequence(seq) for seq in query_sequences]
            query_dictionary[key] = query_sequences
            query_dictionary_reduced[key] = reduced_sequences
            key = line.strip()
            #reset the seq to ""
            seq = ""
        else:
            seq+= line.strip()
    # Gets last item from fasta

    query_sequences = create_six_reading_frames.generate_protein_sequences(seq)
    reduced_sequences = [reduced_alphabet.reduce_sequence(seq) for seq in query_sequences]
    query_dictionary[key] = query_sequences
    query_dictionary_reduced[key] = reduced_sequences
    key = line.strip()
    return query_dictionary, query_dictionary_reduced

def read_fasta_for_proteins(protein_database_sequences):
    protein_database_dictionary = {}
    protein_database_dictionary_reduced = {}
    key = ""
    seq = ""
    for line in protein_database_sequences:
        if line[0]  == '>' and seq=="":
            # meaning this is the name of the sequence
            #name of the key
            key = line.strip()
        elif line[0]  == '>' and seq!="":
            #now we end the seq
            protein_database_dictionary[key] = seq
            reduced_sequence = reduced_alphabet.reduce_sequence(seq)
            protein_database_dictionary_reduced[key] = reduced_sequence
            key = line.strip()
            #reset the seq to ""
            seq = ""
        else:
            seq+= line.strip()
    # Gets last item from fasta
    protein_database_dictionary[key] = seq
    reduced_sequence = reduced_alphabet.reduce_sequence(seq)
    protein_database_dictionary_reduced[key] = reduced_sequence
    key = line.strip()
    #reset the seq to ""
    seq = ""
    return protein_database_dictionary, protein_database_dictionary_reduced