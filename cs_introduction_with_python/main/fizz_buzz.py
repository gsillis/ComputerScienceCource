number = input("Digite o número: ")
arrayOfInt = [int(digit) for digit in number if digit.isdigit()]

lastItem = arrayOfInt[-1]
isDivisibleByFive = lastItem == 0 or lastItem ==  5

sumOfNumers = sum(arrayOfInt)
isDivisibleByThree = sumOfNumers % 3 == 0

if isDivisibleByThree and isDivisibleByFive:
    print("FizzBuzz")
else:
    print(number)
