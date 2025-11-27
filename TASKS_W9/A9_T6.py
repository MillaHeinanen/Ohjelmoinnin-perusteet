########################################################
# Task A9_T6
# Milla Heinänen
# 2025-11-27
########################################################
open = open
def showOptions() -> None:
    print("Options:")
    print("1 - Insert line")
    print("2 - Save lines")
    print("0 - Exit")

def askChoice() -> int:
    choice = input("Your choice: ")
    try:
        return int(choice)
    except ValueError:
        return -1

def saveLines(PLines: list[str]) -> None:
    filename = input("Insert filename: ")
    try:
        with open(filename, "w", encoding="UTF-8") as file:
            file.writelines(PLines)

    except OSError:
        print("Error: Could not save the file.")

def insertLine(PLines: list[str]) -> None:
    text = input("Insert text: ")
    PLines.append(text)

def onInterrupt(PLines: list[str]) -> None:
    print("Keyboard interrupt and unsaved progress!")
    if PLines:
        confirm = input("Save before quit(y/n)?: ").strip().lower()
        if confirm == "y":
            saveLines(PLines)

def main() -> None:
    Lines: list[str] = []
    Choice = -1
    print("Program starting.")
    try:
        while Choice != 0:
            showOptions()
            Choice = askChoice()
            if Choice == 1:
                insertLine(Lines)
            elif Choice == 2:
                if Lines:
                    saveLines(Lines)
                else:
                    print("No lines to save.")
            elif Choice == 0:
                print("Exiting program.")
            else:
                print("Unknown option!")
            print("")
    except KeyboardInterrupt:
        onInterrupt(Lines)

    print("Program ending.")

if __name__ == "__main__":
    main()