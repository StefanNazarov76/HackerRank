# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

if __name__ == '__main__':
    m, d, y = map(int, input().split())
    day_index = calendar.weekday(y, m, d)

    print(calendar.day_name[day_index].upper())
