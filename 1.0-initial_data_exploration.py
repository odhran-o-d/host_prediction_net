
#%%
from Bio import SeqIO
import pandas as pd

#%%
records = list(SeqIO.parse("data/raw/protein_sequences.fasta", "fasta"))
record_metadata = pd.read_csv("data/raw/protein_sequences.csv")

if len(records) == len(record_metadata):
    print('test_pass')
# %%
print(records[0]) 
print(record_metadata.iloc[0])
# %%
print(records[0].description) 
print(record_metadata.iloc[0].Protein)
# %%
Bio.AlignIO.parse()