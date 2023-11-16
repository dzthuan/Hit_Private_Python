def solve(input_):
    a = []
    for item in input_:
        if isinstance(item, list):
            a.extend(solve(item))
        else:
            a.append(item)
    return a
a = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
res = solve(a)
print(res)