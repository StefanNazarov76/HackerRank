# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    _ = input()
    arr = [int(x) for x in input().split()]
    a = set(int(x) for x in input().split())
    b = set(int(x) for x in input().split())

    happiness = 0

    for num in arr:
        if num in a:
            happiness += 1
        elif num in b:
            happiness -= 1

    print(happiness)
