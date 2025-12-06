# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

pattern = re.compile(r'^[+-]?\d*\.\d+$')

for _ in range(int(input())):
    s = input().strip()
    print(bool(pattern.match(s)))
