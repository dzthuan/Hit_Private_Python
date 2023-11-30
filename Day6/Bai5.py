from math import gcd

def solve(a, b):
    tmp = gcd(a, b)
    a //= tmp
    b //= tmp
    return a, b

n = int(input())
a = 1
b = 1
while n > 0:
    a1, b1 = map(int, input().split())
    n -= 1
    a *= a1
    b *= b1
a, b = solve(a, b)
print(a, b)