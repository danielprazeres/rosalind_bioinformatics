def reverse_complement(dna_string, output_filename):
    # Dicionário de mapeamento dos pares complementares
    complement_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    # read
    with open(dna_string, 'r') as file:
        dna_string = file.read().strip()

     # Inverter a string (ler de trás para frente)
    reversed_dna = dna_string[::-1]

    # Substituir cada base pelo seu complemento
    complement_dna = ''.join(complement_map[base] for base in reversed_dna)

    # write
    with open(output_filename, 'w') as file:
        file.write(complement_dna)

    return complement_dna

dna_string = 'Bioinformatics Stronghold/3. Complementing a Strand of DNA/rosalind_revc.txt'
output_filename = 'Bioinformatics Stronghold/3. Complementing a Strand of DNA/output.txt'

reverse_complement(dna_string, output_filename)

