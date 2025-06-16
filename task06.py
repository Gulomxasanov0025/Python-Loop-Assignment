# Kiritilgan so‘zda nechta gap borligini aniqlang
matn = input("Matn kiriting: ")
gap_soni = 0

for belgi in matn:
    if belgi == ".":
        gap_soni += 1

print("Gaplar soni:", gap_soni)