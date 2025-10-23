if __name__ == '__main__':
    records = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    scores = sorted({r[1] for r in records})
    second_lowest = scores[1]

    names = sorted([r[0] for r in records if r[1] == second_lowest])
    for name in names:
        print(name)
