number=int(input("Enter your number for the check please :"))
reversed_number=0
temp=number
while temp > 0:
    digit=temp % 10
    reversed_number=reversed_number*10+digit
    temp//=10
if number == reversed_number:
    print(f"{number} is a palindrome")
else:
    print(f"{number} is not a palindrome")