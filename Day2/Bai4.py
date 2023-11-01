a = int(input())
if a < 0:
    a = -a
print("so bit can thiet : ", a.bit_length())

if (isinstance(a, (int, float))):
    method = dir(a)
    print ("danh sach thuoc tinh va pt cua bien so:")
    for i in method:
        print(i)
else:
    print("khong phai kieu bien so10")