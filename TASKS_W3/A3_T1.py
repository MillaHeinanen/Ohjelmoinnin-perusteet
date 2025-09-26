#Make Python program and implement if-statements in proper places.

#Ask user to insert two integers
print("Program starting.")
print("Insert two integers.")
num1 = int(input("Insert first integer: "))
num2 = int(input("Insert second integer: "))
#Compare the integers and then announce the greater number
print("Comparing inserted integers.")
if num1 > num2:
    print("First integer is greater.\n")
elif num2 > num1:
    print("Second integer is greater.\n")
else:
    print("Integers are the same.\n")
#Create sum of the two integers
print("Adding integers together")
sum = num1 + num2
print(f"{num1} + {num2} = {sum}\n")
#Check the parity of the sum (see modulo-operator ‘%’)
print("Checking the parity of the sum...")
if sum % 2==0:
    print("Sum is even.")
else:
    print("Sum is odd.")
print("Program ending.")