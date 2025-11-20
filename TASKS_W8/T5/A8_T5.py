from loginLib import login, register, viewProfile, change_password

def main() -> None:
    print("Program starting.")
    mainMenu()
    print("Program ending.")

def showOptions() -> None:
    print("Options:")
    print("1 - Login")
    print("2 - Register")
    print("0 - Exit")

def showUserMenu() -> None:
    print("User menu:")
    print("1 - View profile")
    print("2 - Change password")
    print("0 - Logout")

def mainMenu() -> None:

    logged_in_user = None

    while True:
        if logged_in_user is None:
            showOptions()
            choice = askChoice()

            if choice == 0:
                print("Exiting program.")
                break
            elif choice == 1:
                username = askValue("username")
                password = askValue("password")
                if login(username, password):
                    print("Authentication successful!")
                    logged_in_user = username
                    userMenu(logged_in_user)
                else:
                    print("Authentication failed!")
            elif choice == 2:
                username = askValue("username")
                password = askValue("password")
                register(username, password)
                print("User registration completed!")
            else:
                print("Invalid choice. Please select 0-2.")
        else:
            pass


def userMenu(PUsername: str) -> None:
    while True:
        showUserMenu()
        choice = askChoice()

        if choice == 0:
            print("Logging out...")
            break
        elif choice == 1:
            profile = viewProfile(PUsername)
            if profile:
                print(f"Profile ID: {profile[0]} - {profile[1]}")
            else:
                print("Profile not found.")
        elif choice == 2:
            new_password = askValue("new password")
            change_password(PUsername, new_password)
            print("Password changed successfully!")
        else:
            print("Invalid choice. Please select 0-2.")

def askChoice() -> int:
    return int(input("Your choice: "))

def askValue(PPrompt: str) -> str:
    return input(f"Insert {PPrompt}: ")

if __name__ == "__main__":
    main()
