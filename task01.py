# 1. Stringdagi unli harflarni sanang
text = input("Matinni kiriting.").lower()
unlilar = "aeiou"
sana = 0 

for harf in text:
    if harf in unlilar:
        sana+=1
        print(f"{sana}    ta unli harif bor ")