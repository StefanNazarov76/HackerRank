# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

if __name__ == "__main__":
    line = input().split()

    for p in sorted(permutations(line[0], int(line[1]))):
        print(''.join(p))
