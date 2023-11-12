import sys

input_seq = sys.argv[1]
outputFile = sys.argv[2]


first = True
seq_from_input = ""
start_codon = "ATG"
stop_codon = ["TAA", "TAG", "TGA"]

def find_sequences(genome,dist):
    sequences = []
    start = 0
    
    while start<len(genome):
        if genome[start:start+3] == start_codon:
            for stop in range (start, len(genome),3):
                if genome[stop:stop+3] in stop_codon and (stop+3-start)>dist:
                    sequences.append(genome[start:stop+3])
                    break
        start+=1
    return sequences
        

with open(input_seq, encoding="utf-8") as myFile:
    input_seq = myFile.readlines()


for lines in input_seq:
    if first ==True:
        first = False
    else:
        line = lines.strip()
        seq_from_input+=line
#print(seq_from_input)       
result = find_sequences(seq_from_input,50)

#print(result)
        
count = 1
with open(outputFile, 'w') as out_fh:
    for seq in result:
        out_fh.write("seq"+str(count)+"\n")
        out_fh.write(seq+"\n")

import sys

input_seq = sys.argv[1]
outputFile = sys.argv[2]


first = True
seq_from_input = ""
start_codon = "ATG"
stop_codon = ["TAA", "TAG", "TGA"]

def find_sequences(genome,dist):
    sequences = []
    start = 0
    
    while start<len(genome):
        if genome[start:start+3] == start_codon:
            for stop in range (start, len(genome),3):
                if genome[stop:stop+3] in stop_codon and (stop+3-start)>dist:
                    sequences.append(genome[start:stop+3])
                    break
        start+=1
    return sequences
        

with open(input_seq, encoding="utf-8") as myFile:
    input_seq = myFile.readlines()


for lines in input_seq:
    if first ==True:
        first = False
    else:
        line = lines.strip()
        seq_from_input+=line
#print(seq_from_input)       
result = find_sequences(seq_from_input,50)

#print(result)
        
count = 1
with open(outputFile, 'w') as out_fh:
    for seq in result:
        out_fh.write("seq"+str(count)+"\n")
        out_fh.write(seq+"\n")
        count+=1
