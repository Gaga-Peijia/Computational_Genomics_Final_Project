# Intro and abstract of the repository

## Intro and abstract of the repository
Aligning sequencing reads against a protein reference database is a major computational bottleneck in metagenomics and other data-intensive evolutionary project. In this report, we developed a version of "Simple-DIAMOND" based upon "DIAMOND" and "PALADIN" in order to speed up the sequencing read protein alignment process while preserving the high accuracy crucial for gene identification and functional analysis. Our goal was to create a faster alternative to the more traditional Blastx method. 

## key factors
* Oppen Reading Frame (ORF) filter
* Smith-Waterman algorithm with Blosum62 as the penalty function
* Regional and full mith-Waterman
* double indexing
* sketching methods

## how to build up and run the software
### generating simulated samples
Our methodology for testing and validating the program in its development phase includes the generation of simulated random queries derived from a genomic database. We create a total of 10,000 queries, with each query consisting of a random selection of 150 nucleotides from the database. This extensive random sampling is crucial for ensuring the robustness and accuracy of our software.

Used command line in **root directory**:

**python random_samples.py**

### preprocessing
Our original data is from Uniprot sprot, which has sequences of a lot of species. But since prokaryotes rarely have intronic regions, we aim only at the E. coli sequneces. Therefore, we extract only the sequences for E. coli from Uniprot database by 'extract_ecoli_sequences.py'.

While working with our version of algorithm, to accelerate processing, we tried aimming only at strain k12 of E. coli, via extracting only the sequences for E. coli of strain k12 from Uniprot database by 'extract_ecoli_k12.py'.
Also, the minimizer of our version of algorithm has window that can due with sequences that with length at least 30, we used 'fasta_filter.py' to extract E. coli sequences with length of at least 30.

Used command line in **Computational_Genomics_Final_Project**
**/simple_diamond/:**

**python extract_ecoli_sequences.py**

Usage: Preprocessing protein database. Extract only the sequences for E. coli from Uniprot database.

**python extract_ecoli_k12.py**

Usage: Preprocessing protein database. Extract only the sequences for E. coli of strain k12 from Uniprot database.

**python fasta_filter.py**

Usage:  Preprocessing protein database. Filters sequences in a FASTA file that are at least a certain length. 

**python orf_filter.py**

We use 'orf_filter.py' to preprocess the dna reads before inputing it to run blast, diamond or our version of simple diamond. The input is random_samples.fasta, and the filtered file is called orffilter_output_threshold.fasta. Fasta files filtered by different threshold has a little impact on the speed of the alignment algorithms.

### Commands to run the scripts:

cd into simple_diamond

To execute the full_sw alignment, run the following command:
python diamond_main.py --query <DNA FASTA> --protein_database <Protein Database Fasta> --extension full_sw --save_path results
I recommend that you don't run this command as it's a terribly inefficient execution of Smith-Waterman that queries each protein. I would use only 1 or 2 sequences for the DNA query. The protein database can be ../data/uniprot_sprot_cleaned_30.fasta

To execute the regional_sw alignment with minimizers, run the following command:
python diamond_main.py --query ../data/random_samples.fasta --protein_database ../data/uniprot_sprot_cleaned_30.fasta --extension regional_sw --sketching minimizer --save_path results

To execute the regional_sw alignment with minhash, run the following command:
python diamond_main.py --query ../data/random_samples.fasta --protein_database ../data/uniprot_sprot_cleaned_30.fasta --extension regional_sw --sketching minhash --save_path results

To execute the regional_sw alignment with uniformers, run the following command:
python diamond_main.py --query ../data/random_samples.fasta --protein_database ../data/uniprot_sprot_cleaned_30.fasta --extension regional_sw --sketching uniform --save_path results



### scoring 
We firstly preprocess the output txt file from blast or diamond by the 'highest_score.py' to remove lines that do not have the highest score, And then we use 'score_blast_diamond.py' or 'score_our_blast.py' to generate the accuracy scores which can compare the qualify of output.

**python highest_score.py**

Usage: Preprocessing the output of blast or diamond before comparing it with the output of our version. Keep only the sequences with highest score (including tie) from fasta file.

**python score_blast_diamond.py**

Usage: Generate the accuracy scores comparing the output of blast and that of diamond

**python score_our_blast.py**

Usage: Generate the accuracy scores comparing the output of our version of simple diamond and that of diamond
