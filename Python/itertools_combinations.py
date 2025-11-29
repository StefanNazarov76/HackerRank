# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

if __name__ == '__main__':
    s, k = input().split()

    s = ''.join(sorted(s))
    k = int(k)

    for i in range(1, k + 1):
        for combo in sorted(combinations(s, i)):
            print(''.join(combo))