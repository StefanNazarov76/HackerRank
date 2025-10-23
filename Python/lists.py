if __name__ == '__main__':
    N = int(input())
    l = []

    for _ in range(N):
        command = input().split()
        cmd = command[0]

        if cmd == 'insert':
            l.insert(int(command[1]), int(command[2]))
        elif cmd == 'print':
            print(l)
        elif cmd == 'remove':
            l.remove(int(command[1]))
        elif cmd == 'append':
            l.append(int(command[1]))
        elif cmd == 'sort':
            l.sort()
        elif cmd == 'pop':
            l.pop()
        elif cmd == 'reverse':
            l.reverse()
