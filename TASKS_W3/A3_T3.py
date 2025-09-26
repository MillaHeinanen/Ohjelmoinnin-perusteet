# Create a program with a plain menu.
print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs.")
# Prompt username first
name=input("Before the menu, please insert your name: ")

# Make program menu with following options:
# Print welcome message
print("\nOptions: ")
print("1 - Print welcome message")
print("0 - Exit")
# Prompt user to choose option “Your choice:”
choice=input("Your choice: ")
# Welcome {Name}!
if choice=="1":
    print(f"Welcome {name}!\n")
# Exiting...
elif choice=="0":
    print("Exiting...\n")
else:
    print("Unknown option.\n")
print("Program ending.")


# Perform actions based on the user input
# Creating menus like this is a really handy way to make tiny text-based programs and there will be more exercises like this in the future.

# The expectation at this point is that the user is able to choose option by inserting corresponding number. No error handling is required, it will be introduced later.