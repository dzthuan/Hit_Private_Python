n = input()
a = list(map(int, input().split()))
sum1 = 0
sum2 = 0
for i in a:
    if (i % 2 == 0):
        sum1 += i
    else: sum2 += i
if (sum1 > sum2):
    print('even')
    print (sum1)
elif sum1 == sum2:
    print('equal')
else: print('odd')