# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()

lower = []
upper = []
odd = []
even = []

for ch in s:
    if ch.islower():
        lower.append(ch)
    elif ch.isupper():
        upper.append(ch)
    elif ch.isdigit():
        if int(ch) % 2:
            odd.append(ch)
        else:
            even.append(ch)

print(''.join(sorted(lower) + sorted(upper) + sorted(odd) + sorted(even)))
