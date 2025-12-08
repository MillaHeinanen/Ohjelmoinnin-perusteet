########################################################
# Task A10_T3
# Milla Heinänen
# Date 2025-12-06
########################################################

import sys
from A10_TLib import readValues, displayValues, bubbleSort

def main() -> None:
    Values: list[int] = []
    Filename = ""

    print("Program starting.")

    if len(sys.argv) == 2:
        Filename = sys.argv[1]
    else:
        Filename = input("Insert filename: ")

    try:
        Values = readValues(Filename)
    except FileNotFoundError:
        print(f"Error: File '{Filename}' not found.")
        return
    except Exception as e:
        print(f"Error reading '{Filename}': {e}")
        return

    # Print raw values
    print(f"Raw '{Filename}' -> ", end="")
    displayValues(Values)

    bubbleSort(Values, PAsc=True)
    print(f"Ascending '{Filename}' -> ", end="")
    displayValues(Values)

    bubbleSort(Values, PAsc=False)
    print(f"Descending '{Filename}' -> ", end="")
    displayValues(Values)

    Values.clear()

if __name__ == "__main__":
    main()
