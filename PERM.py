def generate_permutations(n):
    permutations = [[]]
    for i in range(1, n + 1):
        new_permutations = []
        for perm in permutations:
            for j in range(len(perm) + 1):
                new_permutations.append(perm[:j] + [i] + perm[j:])
        permutations = new_permutations
    return permutations

def main(n): 
    permutations = generate_permutations(n)
    print(len(permutations))
    for perm in permutations:
        print(" ".join(map(str, perm)))

if __name__ == "__main__":
    n = int(input("n? "))
    main(n)