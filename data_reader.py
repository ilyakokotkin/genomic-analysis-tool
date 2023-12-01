from Bio import SeqIO

def read_genomic_data(file_path):
    sequences = SeqIO.parse(file_path, "fasta")
    return {record.id: record.seq for record in sequences}
