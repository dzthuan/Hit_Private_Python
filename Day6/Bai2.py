def printMaxtrix(s, n, m):
    for i in range(0, m):
        for j in range(0, n):
            print(s[j][i], end = " ")
        print()



n, m = map(int, input().split())
s = []
for i in range(0, n):
    numbers = list(map(int, input().split()))
    s.append(numbers)
printMaxtrix(s, n, m)
