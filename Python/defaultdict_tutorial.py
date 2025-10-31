# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

if __name__ == '__main__':
    n, m = map(int, input().split())
    word_positions = defaultdict(list)

    for i in range(1, n + 1):
        word = input().strip()
        word_positions[word].append(i)

    for _ in range(m):
        query = input().strip()
        if word_positions[query]:
            print(' '.join(map(str, word_positions[query])))
        else:
            print(-1)
