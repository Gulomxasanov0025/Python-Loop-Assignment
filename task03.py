matn = input("Matn kiriting: ")
katta_sana = 0
katta_harf = "  "

for harf in matn:
    if harf.isupper():  
        katta_sana += 1
        katta_harf += harf  +   "   "

print(f"{katta_sana} ta katta harf bor: { katta_harf }  " )