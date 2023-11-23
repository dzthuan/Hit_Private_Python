def solve(input, sum):
    s = sorted(input)
    s1 = 0
    tmp = set()
    for num in s:
        if s1 + num <= sum:
            tmp.add(num)
            s1 += num
        else:
            break
    return tmp
n = int(input())
s1 = set(map(int, input().split()))
sum = int(input())
res = solve(s1, sum)
print(res)
