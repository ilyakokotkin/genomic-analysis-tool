from data_reader import read_genomic_data
from sequence_alignment import align_sequences
from conservation_analysis import analyze_conservation
from visualization import plot_alignment

# Example file paths
file_path1 = 'sequence1.fasta'
file_path2 = 'sequence2.fasta'

# Read and parse data
seq1 = read_genomic_data(file_path1)
seq2 = read_genomic_data(file_path2)

# Perform sequence alignment
alignment = align_sequences(seq1, seq2)

# Analyze conservation
conservation_rate = analyze_conservation(alignment[0], alignment[1])
print(f"Conservation Rate: {conservation_rate}")

# Visualize the results
plot_alignment(alignment[0], alignment[1])
