import string

def print_rangoli(size):
    alpha = string.ascii_lowercase
    width = 4 * size - 3
    lines = []

    for i in range(size):
        s = '-'.join(alpha[size - 1:i:-1] + alpha[i:size])
        lines.append(s.center(width, '-'))

    print('\n'.join(lines[::-1] + lines[1:]))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
