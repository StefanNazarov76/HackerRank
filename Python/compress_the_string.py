# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

pairs = [(len(list(g)), int(d)) for d, g in groupby(input())]
print(' '.join(map(str, pairs)))
