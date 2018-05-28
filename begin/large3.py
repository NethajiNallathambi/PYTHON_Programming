num1 = (input("Enter the num1 number: "))
num2 = (input("Enter  the num2 number: "))
num3 = (input("Enter  the num3  number: "))
 
if (num1 > num2) and (num1 > num3):
   largest = num1
elif (num2 > num1) and (num2 > num3):
   largest = num2
else:
   largest = num3
 
print("The largest number is",largest)
