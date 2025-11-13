def positiveIntegers():
    print("Collecct positive integers.")
    numbers = []
    while True:
        user_input = input("Insert positive integer(negative stops): ")
        user_input = int(user_input)
        if user_input < 0:
            print("Stopped collecting positive integers.")
            break
        elif user_input > 0:
            numbers.append(user_input)
        else:
            print("No integers to display.")
    return numbers

def displayIntegers(numbers: list[int]):
    if numbers:
        print(f"Displaying {len(numbers)} integers:")
        for index, value in enumerate(numbers):
            ordinal = index + 1
            print(f"- Index {index} => Ordinal {ordinal} => Integer {value}")
    else:
        print("No integers to display.")
    return None 

def main():
    print("Program starting.")
    numbers = positiveIntegers()
    displayIntegers(numbers)
    print("Program ending.")
    
if __name__ == "__main__":
    main()
