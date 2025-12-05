# Enter your code here. Read input from STDIN. Print output to STDOUT

X, N = map(int, input().split())

scores = [list(map(float, input().split())) for _ in range(N)]

for student in zip(*scores):
    print(sum(student) / N)
