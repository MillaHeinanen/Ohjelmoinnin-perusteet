# Program starting.
print("Program starting.")
# Testing decision structures.
print("Testing decision structures.")
# Insert an integer: 250
integer=int(input("Insert an integer: "))
# Options:
print("Options:")
# 1 - In one multi-branched decision
print("1 - In one multi-branched decision")
# 2 - In multiple independent if-statements
print("2 - In multiple independent if-statements")
# 0 - Exit
print("0 - Exit")
# Your choice: 1
choice=input("Your choise: ")

if choice=="1":
    print("Using one multi-branched decision structure.")
    if integer>=400:
        integer+=44
    elif integer>=200:
        integer+=22
    elif integer>=100:
        integer+=11
    print(f"Result is {integer}")
    
elif choice=="2":
    print("Using multiple independent if-statements structure.")
    if integer>=400:
        integer+=44
    if integer>=200:
        integer+=22
    if integer>=100:
        integer+=11
    print(f"Result is {integer}")
    
elif choice=="0":
    print("Exiting...")
else:
    print("Unknown option.")
print("\nProgram ending.")