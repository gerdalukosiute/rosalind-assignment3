def count_subsets(n):
    result = pow(2, n, 1000000)
    return result

def main(n):
    result = count_subsets(n)
    print(result)

if __name__ == "__main__":
    n = int(input(""))
    main(n)