def optionMenu() -> int:
    print("\nOptions:")
    print("1 - Insert word")
    print("2 - Show current word")
    print("3 - Show current word in reverse")
    print("0 - Exit")
    return int(input("Your choice: "))

def main() -> None:
    word = ""
    print("Program starting.")
    choice = -1

    while True:
        choice = optionMenu()
        if choice == 1:
            word = input("Insert word: ")
        elif choice == 2:
            print(f'Current word - "{word}"')
        elif choice == 3:
            print(f'Word reversed - "{word[::-1]}"')
        elif choice == 0:
            print("Exiting program.\n")
            print("Program ending.")
            break
        else:
            print("Unknown option! try again.")
    return None

main()