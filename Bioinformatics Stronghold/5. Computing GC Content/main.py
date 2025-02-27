def parse_fasta(filename):
    sequences = {}
    with open(filename, 'r') as file:
        current_label = None
        for line in file:
            line = line.strip()
            if line.startswith(">"):  # Identificador de sequência
                current_label = line[1:]  # Remove o '>'
                sequences[current_label] = ""  # Inicia a sequência no dicionário
            else:
                sequences[current_label] += line  # Adiciona à sequência existente
    return sequences

def gc_content(dna):
    return (dna.count('G') + dna.count('C')) / len(dna) * 100

def highest_gc_content(filename):
    sequences = parse_fasta(filename)  # Lê o arquivo e retorna um dicionário de sequências
    max_label, max_gc = None, 0

    for label, dna in sequences.items():
        gc = gc_content(dna)
        if gc > max_gc:
            max_label, max_gc = label, gc  # Atualiza se encontrar uma sequência com GC maior

    return max_label, round(max_gc, 6)

# Nome do arquivo FASTA
fasta_file = "Bioinformatics Stronghold/5. Computing GC Content/rosalind_gc.txt"

# Executando a função e imprimindo o resultado
label, gc = highest_gc_content(fasta_file)
print(label)
print(gc)