import math

a = float(input("adicione o valor de a: "))
b = float(input("adicione o valor de b: "))
c = float(input("adicione o valor de c: "))

delta = (b ** 2) - 4 * a * c 

if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("raiz 1 igual:", x1, "raiz 2 igual:", x2)
elif delta == 0:
    x = -b / (2 * a)
    print("raiz igual:", x)
else:
    print("Delta negativo")