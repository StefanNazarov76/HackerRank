# Enter your code here. Read input from STDIN. Print output to STDOUT

A = set(input().split())
flag = True

for _ in range(int(input())):
    B = set(input().split())

    if not (A > B):
        flag = False
        break

print(flag)
