########################################################
# Task A10_T2
# Milla Heinänen
# Date 2025-12-06
########################################################
import sys

def readValues(PFilename: str, PValues: list[int]):
    try:
        with open(PFilename, "r", encoding="UTF-8") as filehandler:
            for line_no, raw in enumerate(filehandler, start=1):
                s = raw.strip()
                if not s:
                    continue
                try:
                    value = int(s)
                except ValueError:
                    print(f"Error: Non-integer value on lline {line_no}: {s!r}")
                    sys.exit(2)
                PValues.append(value)
    except FileNotFoundError:
        print(f"Error: File '{PFilename}' not found.")
        sys.exit(1)
    except OSError as e:
        print(f"Error: Could not read file '{PFilename}': {e}")
        sys.exit(1)
    return None

def sumOfValues(PValues: list[int]):
    return sum(PValues)

def productOfValues(PValues: list[int]):
    product = 1
    for value in PValues:
        product *= value
    return product

def main():
    Values: list[int] = []
    print("Program starting.")
    filename = input("Insert filename: ").strip()
    readValues(filename, Values)
    Sum = sumOfValues(Values)
    Product = productOfValues(Values)
    print("# --- Sum of numbers --- #")
    print(Sum)
    print("# --- Sum of numbers --- #")
    print("# --- Product of numbers --- #")    
    print(Product)
    print("# --- Product of numbers --- #")
    Values.clear()
    print("Program ending.")
    return None
if __name__ == "__main__":
    main()