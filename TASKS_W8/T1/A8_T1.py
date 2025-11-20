from library import activatePause

def optionMenu():
    print("\nOptions:")
    print("1 - Set pause duration")
    print("2 - Activate pause")
    print("0 - Exit")

def main() -> None:
    print("Program starting.")
    pause = None

    while True:
        optionMenu()
        choice = input("Your choice: ")
        if choice == "0":
            print("Exiting program.")
            print("\nProgram ending.")
            break        
        if choice == "1":
            pause = float(input("Insert pause duration (s): "))
        elif choice == "2":
            if pause is None:
                print("Pause is not set.\nSet pause first.")
            else:
                activatePause(pause)
        else:
            print("Unknown option!")
    return None
if __name__ == "__main__":
    main()