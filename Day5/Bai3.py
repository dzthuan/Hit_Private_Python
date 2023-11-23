a  = input().split()
tmp = {}
for x in a:
    if x in tmp:
        tmp[x] += 1
    else: tmp[x] = 1

kq = []
for x, fre in tmp.items():
    if fre == max(tmp.values()):
        kq.append((x, fre))
print(tuple(kq))