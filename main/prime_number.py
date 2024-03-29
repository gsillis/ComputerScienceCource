
def find_prime_number():
  n = int(input("Digite um número inteiro > 1: "))

  while n > 0: 
    if is_prime(n): 
      print(n, "é um número primo")
    else:
      print(n, "não é um número primo")
    n = int(input("Digite um número inteiro >1: "))


def is_prime(n):
  factor = 2
  while n % factor != 0 and n <= n/2:
    factor += 1
  if n % factor == 0:
    return False
  else:
    return True
  
find_prime_number()