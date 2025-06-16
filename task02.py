#  Raqamdagi raqamlar yig‘indisini hisoblang
son = input("Son kiriting: ")
yigindi = 0

for raqam in son:
    if raqam.isdigit():  # raqam bo'lsa (manfiy belgi yoki boshqalar bo'lmasin)
        yigindi += int(raqam)

print(f"Raqamlar yig'indisi: {yigindi}")