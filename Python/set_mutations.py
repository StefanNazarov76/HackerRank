# Enter your code here. Read input from STDIN. Print output to STDOUT

_ = input()
a = set(input().split())

for _ in range(int(input())):
    command = input().split()[0]
    b = set(input().split())

    if command == 'intersection_update':
        a.intersection_update(b)
    elif command == 'symmetric_difference_update':
        a.symmetric_difference_update(b)
    elif command == 'difference_update':
        a.difference_update(b)
    elif command == 'update':
        a.update(b)

print(sum(int(x) for x in a))
