def hamming_distance(filename):
    count = 0
    with open(filename, 'r') as file:
        s = file.readline().strip() #lê a primeira linha do arquivo e remove os espaços em branco
        t = file.readline().strip() #lê a segunda linha do arquivo e remove os espaços em branco
        
    for i in range(len(s)): # Percorre cada posição da string
        if s[i] != t[i]: # Compara se os caracteres são diferentes
            count += 1
    return count

filename = "Bioinformatics Stronghold/6. Counting Point Mutations/rosalind_hamm.txt"

print(hamming_distance(filename))