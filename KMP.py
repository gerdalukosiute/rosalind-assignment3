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

def compute_failure_array(s):
    n = len(s)
    failure_array = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = failure_array[j - 1]
        if s[i] == s[j]:
            j += 1
        failure_array[i] = j
    return failure_array

def main(fasta_input):
    sequence = read_fasta(fasta_input)
    failure_array = compute_failure_array(sequence)
    result = ' '.join(map(str, failure_array))
    print(result)

if __name__ == "__main__":
    fasta_input = """#paste input sequence here, increase terminal scrollback settings to 2000 on VSC before using"""
    main(fasta_input)