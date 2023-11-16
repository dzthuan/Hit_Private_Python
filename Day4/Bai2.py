def check(tmp):
    a = {1, 3, 5, 7, 9}
    t1 = tmp % 10
    return t1 in a
n = int(input())
a = list(map(int, input().split()))
ans = [tmp for tmp in a if check(tmp)]
ans.sort()
print(len(ans))
print(" ".join(map(str, ans)))