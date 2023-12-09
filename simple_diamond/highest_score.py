"""
Keep only the sequences with highest score (including tie) from fasta
"""

import pandas as pd

def filter_highest_scores(input_path, output_path):
    df = pd.read_csv(input_path, sep="\s+", header=None)
    
    df.columns = ['DNA_number', 'Protein_name', 'Score'] + [f'Col_{i}' for i in range(3, df.shape[1])]
    
    # Group by the DNA_number and filter to keep only the rows with the highest score
    def keep_highest_scores(group):
        highest_score = group['Score'].max()
        return group[group['Score'] == highest_score]

    # Apply the function to keep rows with the highest scores
    df_filtered = df.groupby('DNA_number', group_keys=False).apply(keep_highest_scores)
    
    df_filtered.to_csv(output_path, sep='\t', index=False)

filter_highest_scores('/home/cgf2312/Desktop/CGS/CGS_project/Computational_Genomics_Final_Project/matches_diamond.tsv','/home/cgf2312/Desktop/CGS/CGS_project/Computational_Genomics_Final_Project/matches_diamond_highest.tsv' )
