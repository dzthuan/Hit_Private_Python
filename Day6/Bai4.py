from math import *


def docFile(f):
    temp = list(f.read().split())
    print(temp)
    a = list(map(float, temp[1:3]))
    b = list(map(float, temp[4:7]))
    return a, b


def khoangCach(a, b):
    return sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)


if __name__ == "__main__":
    f = open("C:\\HocCODE\\Hoc py\\Day6\\New folder\\input.txt", "r")
    a, b = docFile(f)
    f.close()
    f = open("output.txt", "w")
    f.write(str(round(khoangCach(a, b), 2)))