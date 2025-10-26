# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    thickness = int(input().strip())
    symbol = 'H'

    for i in range(thickness):
        print((symbol * i).rjust(thickness - 1) + symbol + (symbol * i).ljust(thickness - 1))

    for _ in range(thickness + 1):
        print((symbol * thickness).center(thickness * 2) + (symbol * thickness).center(thickness * 6))

    for _ in range((thickness + 1) // 2):
        print((symbol * thickness * 5).center(thickness * 6))

    for _ in range(thickness + 1):
        print((symbol * thickness).center(thickness * 2) + (symbol * thickness).center(thickness * 6))

    for i in range(thickness):
        print(
            ((symbol * (thickness - i - 1)).rjust(thickness) + symbol +
             (symbol * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6)
        )