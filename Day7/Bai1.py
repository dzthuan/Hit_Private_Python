
class Pycon:
    count = 0
    total_age = 0

    def __init__(self, name, age):
        Pycon.count += 1
        self.id = Pycon.count
        self.name = name
        self.age = age
        Pycon.total_age += age

    def nhap(self):
        self.name = input("Nhập tên: ")
        self.age = int(input("Nhập tuổi: "))
        Pycon.total_age += self.age

    @classmethod
    def averAge(cls):
        if cls.count == 0:
            return 0
        return cls.total_age / cls.count

    def __str__(self):
        return f"Id: {self.id} || Tên: {self.name} || Tuổi: {self.age}"

n = int(input())
pycons = []
for _ in range(n):
    pycon = Pycon("", 0)
    pycon.nhap()
    pycons.append(pycon)
for pycon in pycons:
    print(pycon)
print(f"Trung bình tuổi: {Pycon.averAge()}")
