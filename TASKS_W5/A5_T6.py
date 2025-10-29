def showOptions():
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")
    return None
def askChoice():
    try:
        return int(input("Your choice: "))
    except ValueError:
        return -1
def main():
    print("Program starting.")
    count=0
    showOptions()
    choice = askChoice()   
    while choice != 0:
        if choice == 1:
            print(f"Current count - {count}\n")
        elif choice == 2:
            count += 1
            print("Count increased!\n")
        elif choice == 3:
            print("Cleared count!\n")
        else:
            print("Unknown option!\n")
        showOptions()
        choice = askChoice()
    print("Exiting program.")
    print("\nProgram ending.")
   
main()