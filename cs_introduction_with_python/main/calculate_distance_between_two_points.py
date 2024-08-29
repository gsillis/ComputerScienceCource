import math

xa = int(input("adicione o primeiro eixo x: "))
ya = int(input("adicione o primeiro eixo y: "))
xb = int(input("adicione o segundo eixo x: "))
yb = int(input("adicione o segundo eixo y: "))


dab2 = (xa - xb) ** 2 + (yb - ya) ** 2
dab = math.sqrt(dab2)

if int(dab) >= 10:
    print("longe")
else:
    print("perto")
