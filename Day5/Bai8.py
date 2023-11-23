championLOL = ["Yasuo", "Lee Sin", "Zed", "Master Yi", "Garen", "Tryndamere"]
dataLOL = [
    {"price": 6300, "Ulti": "Trăn trối"},
    {"price": 4800, "Ulti": "Nộ Long Cước"},
    {"price": 4800, "Ulti": "Dấu Ấn Tử Thần"},
    {"price": 450, "Ulti": "Chiến Binh Sơn Cước"},
    {"price": 450, "Ulti": "Công Lý Demacia"},
    {"price": 1350, "Ulti": "Từ Chối Tử Thần"}
]

lol = {championLOL[i]: dataLOL[i] for i in range(len(championLOL))}

sinput = input()

if sinput in lol:
    price = lol[sinput]["price"]
    print(f"Giá của champion {sinput}: {price}")
else:
    print(f"Champion {sinput} không tồn tại trong danh sách.")
