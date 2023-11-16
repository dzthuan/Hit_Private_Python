def nhom(input):
    new_list = []
    a = []
    for i in input:
        if not a or i != a[-1]:
            a = [i]
            new_list.append(a)
        else:
            a.append(i)
    return new_list
input = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
input.sort()
res = nhom(input)
print(res)