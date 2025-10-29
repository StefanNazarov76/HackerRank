# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

if __name__ == "__main__":
    _ = input()
    sizes = Counter(int(x) for x in input().split())
    n_customers = int(input())

    total = 0
    for _ in range(n_customers):
        line = input().split()
        size = int(line[0])
        price = int(line[1])

        if sizes[size] > 0:
            total += price
            sizes[size] -= 1

    print(total)
