print("Nhap a = ")
a = int(input())
print ("Nhap b = ")
b = int(input())
print(a ,"+", b ," = ", a + b )
print (a, "-", b, " = ", a - b)
print (a, "*", b, " = ", a * b)
print (a, "/", b, " = ", a / b)
print (a, "**", b, " = ", a ** b)
print (a, "%", b, " = ", a % b)
print ("Compare ", a, "with ", b, ":", "a==b" if a == b else "a>b" if a > b else "a<b")
print (a, "AND", b, "=", a and b)
print (a, "OR", b, "=", a or b)
print (a, "XOR", b, "=", not (a or b))
print ("NOT", a, "==", b, "=", not a == b)
print (a, "a SL 5 bit", a << 5)
print (a, "a SR 5 bit", a >> 5)
print (bin(a) [2:][::-1])