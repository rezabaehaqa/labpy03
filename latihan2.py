maks = 0
while True:
    b = int(input("masukan bilangan = "))
    if maks < b:
        maks = b
    if b == 0:
        break
print("Bilangan Terbesarnya adalah =", maks)