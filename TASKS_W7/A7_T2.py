def collectIntegers(user_input):
    items = [item.strip() for item in user_input.split(",")]
    valid = []
    invalid = []
    for item in items:
        if item.lstrip("-").isdigit():
            valid.append(int(item))
        else:
            invalid.append(item)
    return valid, invalid

def analyze(numbers: list[int]):
    total = sum(numbers)
    parity = "even" if total % 2 == 0 else "odd"
    return total, parity

def main():
    print("Program starting.")
    user_input = input("Insert comma separated integers: ")
    numbers, invalid = collectIntegers(user_input)
    for invalid in invalid:
        print(f"Error: '{invalid}' is not a valid integer.")
    if numbers:
        count = len(numbers)
        total, parity = analyze(numbers)
        print(f"There are {count} integers in the list.")
        print(f"Sum of the integers is {total}, and it's {parity}")
    else:
        print("No valid integers to analyze.")
    print("Program ending.")
    
if __name__ == "__main__":
    main()