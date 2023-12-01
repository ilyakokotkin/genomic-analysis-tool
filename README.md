
# Comparative Genomic Analysis Tool

## Overview
This tool compares genomic sequences from different organisms to identify similarities and differences. It includes sequence alignment, conservation analysis, and evolutionary relationship insights.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/ilyakokotkin/genomic-analysis-tool.git
   ```
2. Navigate to the project directory:
   ```
   cd comparative-genomics-tool
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
Run `main.py` to execute the tool:
```
python main.py
```
Ensure you have the genomic data files in FASTA format in the project directory.

## Files Description
- `data_reader.py`: Reads and parses genomic data.
- `sequence_alignment.py`: Aligns sequences using basic pairwise alignment.
- `conservation_analysis.py`: Analyzes conservation in aligned sequences.
- `visualization.py`: Visualizes the alignment and conservation data.
- `main.py`: Main script to run the tool.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
