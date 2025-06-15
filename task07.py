eng_katta = None

for i in range(5):
    son = int(input(f"{i+1}-sonni kiriting: "))
    if eng_katta is None or son > eng_katta:
        eng_katta = son

print("Eng katta son:", eng_katta)