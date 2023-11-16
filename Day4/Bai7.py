def solve(input, n):
    tmp = len(input) // n
    res = []
    for i in range(n):
        a = []
        for j in range(tmp):
            idx = i * tmp + j
            a.append(input[idx])
        res.append(a)
    return res
a = input().split()
n = int(input())
res = solve(a, n)
print(res)