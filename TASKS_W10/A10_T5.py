########################################################
# Task A10_T5
# Milla Heinänen
# Date 2025-12-08
########################################################

import sys

def recursiveFactorial(PNum: int) -> int:
    if PNum == 0 or PNum == 1:
        return 1
    return PNum * recursiveFactorial(PNum - 1)

def main() -> None:
    print("Program starting.")
    try:
        raw = input("Insert factorial: ").strip()
        n = int(raw)

        if n < 0:
            print("Error: Factorial is not defined for negative integers.")
            print("Program ending.")
            return
        result = recursiveFactorial(n)

        print(f"Factorial {n}!")
        print(f"{n} = {result}")

    except ValueError:
        print("Error: Please enter a valid integer.")
    except RecursionError:
        print("Error: Recursion depth exceeded. Try a smaller number.")
    finally:
        print("Program ending.")

if __name__ == "__main__":
    main()
