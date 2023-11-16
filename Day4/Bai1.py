def solve(date):
    day, month, year = map(int, date.split('/'))
    a = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        a[2] = 29
    cnt = sum(a[month : ]) - day + 1
    return cnt
date = input()
print(solve(date))

