def generate_strings(input_seq):
    lines = input_seq.strip().split('\n')
    alphabet = lines[0].split()
    n = int(lines[1])

    results = ['']
    for _ in range(n):
        new_results = []
        for result in results:
            for symbol in alphabet:
                new_results.append(result + symbol)
        results = new_results
    return results

def main(input_seq):
    strings = generate_strings(input_seq)
    for string in strings:
        print(string)

if __name__ == "__main__":
    input_seq = """#paste input data here"""
    main(input_seq)