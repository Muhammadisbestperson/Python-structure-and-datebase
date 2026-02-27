numberlargest=int(input("Enter Largest number:"))
numbersmallest=int(input("Enter smallest number:"))
while(numbersmallest):
    numberstore=numbersmallest
    numbersmallest=numberlargest%numbersmallest
    numberlargest=numberstore
print("HCF is :", numberlargest)