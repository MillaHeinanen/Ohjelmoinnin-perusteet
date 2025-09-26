# Extend the previous menu program by adding three more options to the menu.
print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs.")
name=input("Before the menu, please insert your name: ")

# Options:
print("\nOptions: ")
print("1 - Print welcome message")
print("2 - Print the name backwards")
print("3 - Print the first character")
print("4 - Show the amount of characters in the name")
print("0 - Exit")
choice=input("Your choice: ")
# Print the name backwards
if choice=="1":
     print(f"Welcome {name}!\n")
elif choice=="2":
    print(f'Your name backwards is "{name[::-1]}"\n')
# Print the first character
elif choice=="3":
    print(f'The first character in name "{name}" is "{name[0]}"\n')
 # Show the amount of characters in the name   
elif choice=="4":
    print(f'There are {len(name)} characters in the name "{name}"\n')
elif choice=="0":
    print("Exiting...\n")
print("Program ending.")
