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

def reverse_complement(sequence):
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement_dict[base] for base in reversed(sequence))

def find_reverse_palindromes(sequence):
    results = []
    for i in range(len(sequence)):
        for length in range(4, 13):
            if i + length <= len(sequence):
                substring = sequence[i:i + length]
                rev_comp = reverse_complement(substring)
                if substring == rev_comp:
                    results.append((i + 1, length))
    return results

def main(fasta_input):
    sequence = read_fasta(fasta_input)
    palindrome_positions = find_reverse_palindromes(sequence)
    for pos in palindrome_positions:
        print(" ".join(map(str, pos)))

if __name__ == "__main__":
    fasta_input = """#input fasta sequence here"""
    main(fasta_input)