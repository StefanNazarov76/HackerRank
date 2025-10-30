# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    _ = input()
    a = set(int(x) for x in input().split())
    _ = input()
    b = set(int(x) for x in input().split())

    ans = a.symmetric_difference(b)
    print('\n'.join(str(x) for x in sorted(ans)))
