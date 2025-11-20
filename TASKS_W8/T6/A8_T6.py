from drawLib import drawCircle, drawSquare, saveSvg, Drawing

def main() -> None:
    Dwg = Drawing()
    print("Program starting.")
    while True:
        showOptions()
        choice = askChoice()
        match choice:
            case 1:
                print('Insert square')
                left = float(askValue1("Left edge position"))
                top = float(askValue1("Top edge position"))
                sideLength = float(askValue1("Side length"))
                color = askValue1("Fill color")
                strokeColor = askValue1("Stroke color")
                drawSquare(Dwg, left, top, sideLength, color, strokeColor)
            case 2:
                print('Insert circle')
                centerX = float(askValue1("Center X position"))
                centerY = float(askValue1("Center Y position"))
                radius = float(askValue1("Radius"))
                color = askValue1("Fill color")
                strokeColor = askValue1("Stroke color")
                drawCircle(Dwg, centerX, centerY, radius, color, strokeColor)
            case 3:
                filename = askValue2("Insert filename")
                print(f'Saving file to "{filename}"')
                confirm = askValue2("Proceed? (y/n)")
                if confirm.lower() == "y":
                    saveSvg(Dwg, filename)
                    print("Vector saved successfully!")
                else:
                    print("Save cancelled.")
            case 0:
                print("Exiting program.\n")
                break
            case _:
                print("Invalid choice. Please select 0-3.")
        print()
    print("Program ending.")

def showOptions() -> None:
    print("Options:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Save svg")
    print("0 - Exit")

def askChoice() -> int:
    return int(input("Your choice: "))

def askValue1(PPrompt: str) -> str:
    return input(f"- {PPrompt}: ")

def askValue2(PPrompt: str) -> str:
    return input(f"{PPrompt}: ")

if __name__ == "__main__":
    main()