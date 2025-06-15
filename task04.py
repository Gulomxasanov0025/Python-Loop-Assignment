#Random son topish o‘yini
import random
tugri_son = random.randint(1, 20)

while True:
    taxmin = int(input(" 1  - dan 20 gacha son topish .  : " ))
    if taxmin == tugri_son:
        print("Topdingiz. " )
        break
    else:
        print("Yana urinib ko'ring. " )