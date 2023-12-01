from Bio import pairwise2
from Bio.pairwise2 import format_alignment

def align_sequences(seq1, seq2):
    alignments = pairwise2.align.globalxx(seq1, seq2)
    return alignments[0]  # Return the first alignment as an example
