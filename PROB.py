import math

def common_log_probability(input_data):
    lines = input_data.strip().split('\n')
    dna_string = lines[0]
    gc_content_values = list(map(float, lines[1].split()))

    result = []

    for gc_content in gc_content_values:
        prob_A = prob_T = (1 - gc_content) / 2
        prob_C = prob_G = gc_content / 2

        probability = 1
        for base in dna_string:
            if base == 'A':
                probability *= prob_A
            elif base == 'T':
                probability *= prob_T
            elif base == 'C':
                probability *= prob_C
            elif base == 'G':
                probability *= prob_G
        log_probability = math.log10(probability)
        result.append(round(log_probability, 3)) 
    return result

def main(input_data):
    result = common_log_probability(input_data)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    input_data = """#paste input here"""
    main(input_data)