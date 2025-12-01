# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

d = deque()

for _ in range(int(input())):
    command = input().split()

    if 'append' == command[0]:
        d.append(command[1])
    elif 'appendleft' == command[0]:
        d.appendleft(command[1])
    elif 'pop' == command[0]:
        d.pop()
    elif 'popleft' == command[0]:
        d.popleft()

print(' '.join(d))