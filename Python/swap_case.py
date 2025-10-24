def swap_case(s):
    new_string = ''

    for i in s:
        if i.islower():
            new_string += i.upper()
        else:
            new_string += i.lower()

    return new_string


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
