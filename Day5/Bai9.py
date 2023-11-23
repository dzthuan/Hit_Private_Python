import random
n = int(input("Nhap n: "))
res = {}
a = ["CNTT", "KHMT", "KTPM", "HTTT"]
for i in range(0, n):
    print("Nhap sinh vien thu", i + 1, ":")
    tmp1 = {}
    tmp2 = {}
    msv = input("MSV: ")
    tmp1["Username"] = msv
    tmp2["Password"] = random.choice(a) + msv
    Account =  "Account" + str(i + 1)
    tmp1.update(tmp2)
    res[Account] = tmp1
print(res)