# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    _ = input()
    numbers = set(map(int, input().split()))

    for _ in range(int(input())):
        command = input().split()

        if command[0] == 'pop':
            if numbers:
                smallest = min(numbers)
                numbers.remove(smallest)

        elif command[0] == 'remove':
            numbers.remove(int(command[1]))

        elif command[0] == 'discard':
            numbers.discard(int(command[1]))

    print(sum(numbers))