# Enter your code here. Read input from STDIN. Print output to STDOUT

n = input()
l = input().split(' ')
print(all([int(a) > 0 for a in l]) and any([int(a) == int(str(a)[::-1]) for a in l]))
