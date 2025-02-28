# Tabela de códons de RNA para aminoácidos
codon_table = {
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "UAU": "Y", "UAC": "Y", "UAA": "STOP", "UAG": "STOP",
    "UGU": "C", "UGC": "C", "UGA": "STOP", "UGG": "W",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}

def translate_rna_to_protein(rna):
    protein = ""
    # Percorre a string de RNA de 3 em 3 nucleotídeos
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]

        if codon in codon_table:
            amino_acid = codon_table[codon]
            if amino_acid == "STOP":
                break
            protein += amino_acid

    return protein

def read_file(filename):
    with open(filename, "r") as file:
        rna = file.read().strip()

    return translate_rna_to_protein(rna)

rna_sequence = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
filename = "Bioinformatics Stronghold/8. Translating RNA into Protein/rosalind_prot.txt"

# MAMAPRTEINSTRING sample output
# print(translate_rna_to_protein(rna_sequence))

print(read_file(filename))

