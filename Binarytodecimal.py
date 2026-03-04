number = int(input("Enter a binary number: "))

decimalNumber = 0
power = 0
temp = number

while temp > 0:
    digit = temp % 10
    decimalNumber += digit * (2 ** power)
    power += 1
    temp //= 10

print("Decimal number is:", decimalNumber)

