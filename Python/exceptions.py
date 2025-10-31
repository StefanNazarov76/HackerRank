# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        a, b = input().split()
        try:
            a_int = int(a)
            b_int = int(b)
            print(a_int // b_int)
        except Exception as e:
            print('Error Code:', e)
