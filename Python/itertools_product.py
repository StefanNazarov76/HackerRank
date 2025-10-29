# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

if __name__ == "__main__":
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    print(*product(A, B))
