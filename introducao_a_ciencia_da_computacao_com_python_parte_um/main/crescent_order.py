number = list(input("Insira os números: "))

arrayOfInt = [int(digit) for digit in number if digit.isdigit()]
isCrescent = False

for item in range(len(arrayOfInt) - 1):
    if arrayOfInt[item] > arrayOfInt[item + 1]:
        print("não esta em ordem crescente")
        break
else:
    print("crescente")  