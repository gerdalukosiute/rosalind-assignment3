import math

def read_fasta(fasta_input):
    sequences = []
    fasta_sequences = fasta_input.strip().split('>')
    for sequence in fasta_sequences:
        lines = sequence.split('\n')
        header = lines[0]
        seq = ''.join(lines[1:])
        if header.startswith("Rosalind_"):
            sequences.append(seq)
    return sequences[0]

def count_perfect_matchings(rna_string):
    gc_count = rna_string.count('G')
    au_count = rna_string.count('A')
    return math.factorial(gc_count) * math.factorial(au_count)

def main(fasta_input):
    rna_string = read_fasta(fasta_input)
    result = count_perfect_matchings(rna_string)
    print(result)

if __name__ == '__main__':
    fasta_input = """#paste fasta sequence"""
    main(fasta_input)