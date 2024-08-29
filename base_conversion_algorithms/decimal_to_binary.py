decimal_number = int(input("Digite o numero em decimal: "))

binary = ""
while decimal_number > 0:
    mod = decimal_number %  2
    decimal_number = decimal_number // 2
    binary = str(mod) + binary
print("O número decimal em binário é ", binary)
