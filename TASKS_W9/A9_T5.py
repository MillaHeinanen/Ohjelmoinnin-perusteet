########################################################
# Task A9_T5
# Milla Heinänen
# 2025-11-27
########################################################

def askIntByte(PPrompt: str) -> int:
    Feed = input(PPrompt)

    try:
        value = float(Feed)
    except ValueError:
        raise ValueError(f"\"{Feed}\" is non-numeric value.")
    if not value.is_integer():
        raise ValueError(f"\"{Feed}\" is non-numeric value.")
    value = int(value)
    if value < 0 or value > 255:
        raise ValueError(f"Value \"{Feed}\" is out of the range 0-255.")
    return value

def createHex(PRed: int, PGreen: int, PBlue: int) -> str:
    return "#{:02x}{:02x}{:02x}".format(PRed, PGreen, PBlue)

def main():
    print("Program starting.")

    try:
        red = askIntByte("Insert red: ")
        green = askIntByte("Insert green: ")
        blue = askIntByte("Insert blue: ")
        hex_color = createHex(red, green, blue)
        print(f"RGB Details:")
        print(f"{red:08b}")
        print(f"{green:08b}")
        print(f"{blue:08b}")
        print(f"{hex_color}")

    except Exception as e: 
        print(e)
        print("Couldn't perform the designed task due to the invalid input values.")

    print("Program ending.")

if __name__ == "__main__":
    main()