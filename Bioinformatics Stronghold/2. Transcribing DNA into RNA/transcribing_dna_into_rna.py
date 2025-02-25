def transcribing_dna_into_rna_from_file(input_filename, output_filename):
    # read
    with open(input_filename, 'r') as file:
        dna_string = file.read().strip()
    rna_string = dna_string.replace('T', 'U')

    # write
    with open(output_filename, 'w') as file:
        file.write(rna_string)

input_filename = 'Bioinformatics Stronghold/2. Transcribing DNA into RNA/rosalind_rna.txt'
output_filename = 'Bioinformatics Stronghold/2. Transcribing DNA into RNA/rna_output.txt'

transcribing_dna_into_rna_from_file(input_filename, output_filename)