n = int(input("Digite um número inteiro > 1: "))
factor = 2
multiplicity = 0

while n > 1:
  while n % factor == 0: 
    multiplicity += 1
    n /= factor
  if multiplicity > 0:
    print("fator ", factor, "multiplicidade = ", multiplicity)
  factor += 1
  multiplicity = 0



