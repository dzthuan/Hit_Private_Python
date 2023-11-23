s = set(map(int, input().split()))
if 11 not in s:
    s.add(11)

ans = []
for num in s:
    tmp = 11 - num
    if tmp in s and tmp != num:
        ans.append((num, tmp))
print(ans)
res = tuple(ans)
sum1 = sum([sum(pair) for pair in ans])
print(res)
print(sum1)