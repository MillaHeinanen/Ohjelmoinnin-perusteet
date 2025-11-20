def readFile(filename: str):
    values = []
    with open(filename, "r") as filehandler:
        for row in filehandler:
            row = row.strip()
            if row:
                values.append(float(row))
    return values

def calculate_sum(values: list[float]):
    return round(sum(values), 1)

def calculate_average(values: list[float]):
    return round(sum(values) / len(values), 1) if values else 0.0

def showOptions():
    print("\nOptions:")
    print("1 - Read values")
    print("2 - Amount of values")
    print("3 - Calculate sum of values")
    print("4 - Calculate average of values")
    print("0 - Exit")
    
def main():
    print("Program starting.")
    values: list[float] =[]
    
    while True:
        showOptions()
        choice = input("Your choice: ")
        
        if choice == "0":
            print("Exiting program.")
            break
        elif choice == "1":
            filename = input("Insert filename: ")
            values = readFile(filename)
        elif choice == "2":
            print(f"Amount of values: {len(values)}")
        elif choice == "3":
            print(f"Sum of values: {calculate_sum(values)}")
        elif choice == "4":
            print(f"Average of values: {calculate_average(values)}")
        else:
            print("Invalid choice. Please select 0-4.")
    
    print("\nProgram ending.")
if __name__ == "__main__":
    main()