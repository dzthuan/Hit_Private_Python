import re
def check(tmp):
    a = re.findall(r'-?\d+', tmp)
    ans = sum(map(int, a))
    return ans
s = input()
print(check(s))