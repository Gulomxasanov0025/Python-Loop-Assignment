parol = "python123"

for urinish in range(3):
    kirish = input("Parolni kiriting: ")
    if kirish == parol:
        print("Parol to‘g‘ri!")
        break
    else:
        print("Yana urinib ko‘ring.")

else:
    print("Bloklandiz.")