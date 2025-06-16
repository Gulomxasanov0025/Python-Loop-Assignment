# PIN kod ochish o‘yini
import random

pin = random.randint(1000, 9999)

for urinish in range(7):
    taxmin = int(input("4 xonali PIN kiriting: "))
    if taxmin == pin:
        print("Tabriklaymiz, topdingiz!")
        break
    elif taxmin > pin:
        print("Juda katta son!")
    else:
        print("Juda kichik son!")

else:
    print("Afsus, urinishingiz tugadi. PIN:", pin)