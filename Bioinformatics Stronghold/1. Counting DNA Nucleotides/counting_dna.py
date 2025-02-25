from collections import Counter

def count_nucleotides_from_file(filename):
    with open(filename, 'r') as file:
        dna_string = file.read().strip()
    counts = Counter(dna_string)
    print(counts['A'], counts['C'], counts['G'], counts['T'])

# Nome do arquivo fornecido pelo Rosalind
filename = "Bioinformatics Stronghold/1. Counting DNA Nucleotides/rosalind_dna.txt"
count_nucleotides_from_file(filename)