from library import add, subtract, multiply, divide

def askValue(PPrompt: str) -> float:
   while True:
        try:
            return float(input(PPrompt))
        except ValueError:
            print("Please enter a valid number.")
            
def getPrompts(choice: int) -> tuple[str, str]:
    if choice == 1:
        return ("Insert first addend value: ", "Insert second addend value: ")
    elif choice == 2:
        return ("Insert minuend value: ", "Insert subtrahend value: ")
    elif choice == 3:
        return ("Insert multiplicand value: ", "Insert multiplier value: ")
    elif choice == 4:
        return ("Insert dividend value: ", "Insert divisor value: ")
    else:
        return ("Insert first value: ", "Insert second value: ")


def askChoice() -> int:
    while True:
        try:
            choice = int(input("Your choice: "))
            if choice in [0, 1, 2, 3, 4]:
                return choice
            else:
                print("Invalid choice. Please select 0-4.")
        except ValueError:
            print("Please enter a valid integer.")

def showOptions() -> None:
    print("\nOptions:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("0 - Exit")


def main() -> None:
    print("Program starting.")
    while True:
        showOptions()
        choice = askChoice()
        
        if choice == 0:
            print("Exiting program.")
            break
        
        prompt1, prompt2 = getPrompts(choice)
        num1 = askValue(prompt1)
        num2 = askValue(prompt2)
        
        if choice == 1:
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")
        elif choice == 2:
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif choice == 3:
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")
        elif choice == 4:
            try:
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
            except ZeroDivisionError as e:
                print(e)
    print ("\nProgram ending.")
if __name__ == "__main__":
    main()