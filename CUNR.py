def count_unrooted_binary_trees(n):
    result = 1
    for i in range(2 * n - 5, 1, -2):
        result = (result * i) % 10**6
    return result

def main(n):
    result = count_unrooted_binary_trees(n)
    print(result)

if __name__ == "__main__":
    n = int(input("n? (n<=1000): "))
    main(n)