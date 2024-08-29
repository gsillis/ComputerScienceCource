number = input("Digite o número: ")

arrayOfInt = [int(digit) for digit in number if digit.isdigit()]

lastItem = arrayOfInt[-1]

if lastItem == 0 or lastItem ==  5:
    print("Buzz")
else:
    print(number)
