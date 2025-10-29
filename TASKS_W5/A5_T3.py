def askName():
    name = input("Insert name: ")
    return name

def greetUser(Pname) -> None:
    print(f"Hello {Pname}!")
    return None
    
def main() -> None:
    print("Program starting.")
    name = askName()
    greetUser(name)
    print("Program ending.")
    return None
    
main()