DS = {
    'SV001': 3.0,
    'SV002': 2.8,
    'SV003': 3.5,
    'SV004': 1.9,
}

soSV1 = sum(2.5 <= diem <= 3.5 for diem in DS.values())
print(f"So sv co diem [2.5 3.5]: {soSV1}")

DS['SV005'] = 3.2

xoaSV = [key for key, value in DS.items() if value < 2.0]

for sv in xoaSV:
    del DS[sv]

print(DS)
