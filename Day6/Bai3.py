def prefixSum(s, n, q):
    F = [0] * n
    F[0] = s[0]
    for i in range(1, n):
        F[i] = F[i - 1] + s[i]
    while q > 0:
        if (q == 0):
            break
        q -= 1
        idx = int(input())
        print(F[idx])
        

n = int(input())
s = list(map(int, input().split()))
q = int(input())
prefixSum(s, n, q)