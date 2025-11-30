# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

s, k = input().split()
s = ''.join(sorted(s))
k = int(k)

for comb in combinations_with_replacement(s, k):
    print(''.join(comb))