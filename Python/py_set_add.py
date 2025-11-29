# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    countries = set()

    for _ in range(int(input())):
        country = input()
        countries.add(country)

    print(len(countries))
