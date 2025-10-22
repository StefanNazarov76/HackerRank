if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    arr = list(arr)
    max_score = max(arr)
    while max_score in arr:
        arr.remove(max_score)

    print(max(arr))
