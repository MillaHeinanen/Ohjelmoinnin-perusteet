#Create a program which prompts the user to insert an integer and then display the collatz conjecture as shown in the examples below.
print("Program starting.")
integer=int(input("Insert a positive integer: "))
steps=0
while integer!=1:
    print(integer, end=" -> ")
    if integer%2==0:
        integer=integer//2
    else:
        integer=3*integer+1
    steps+=1
print(integer)
print(f"Sequence had {steps} total steps.\n")
print("Program ending.")

