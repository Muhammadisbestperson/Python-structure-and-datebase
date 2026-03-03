numberLarge=int(input("Enter the greatest/largest number:"))
numberSmall=int(input("Enter the tiniest/smallest number "))
while(numberSmall):
    numberstore=numberSmall
    numberSmall=numberLarge%numberSmall
    numberLarge=numberstore
lcm=(numberLarge*numberSmall)
print("LCM is:",lcm)