def konyvhossz(oldalszam):
    if oldalszam > 150:
        return True
    else:
        return False

terjedelem = "x"
konyvcim = "x"
while konyvcim:
    konyvcim = input("Írd be a könyv címét:")
    if konyvcim:
        oldalszam = input("Hány oldalból áll a könyv?")
        oldalszam = int(oldalszam)

        if konyvhossz(oldalszam) == True:
            terjedelem = "hosszú"
        if konyvhossz(oldalszam) == False:
            terjedelem = "rövid"
        

        print("A/az", konyvcim, "egy", terjedelem, "terjedelmű alkotás")
    else:
        exit


