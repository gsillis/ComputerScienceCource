n = int(input("Digite um número inteiro: "))
sum = 0

while n > 0:
    sum += n % 10
    n //= 10

print(sum)
