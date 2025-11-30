# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

items = OrderedDict()
n = int(input())

for _ in range(n):
    *name_parts, price = input().split()
    name = ' '.join(name_parts)
    price = int(price)

    if name in items:
        items[name] += price
    else:
        items[name] = price

for name, total in items.items():
    print(name, total)
