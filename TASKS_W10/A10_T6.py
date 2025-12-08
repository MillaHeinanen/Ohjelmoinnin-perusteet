########################################################
# Task A10_T6
# Milla Heinänen
# Date 2025-12-08
########################################################
import copy
import time
from typing import Callable
import re

def readValues(PValues: list[int], PFilename: str) -> None:
    PValues.clear()
    try:
        with open(PFilename, "r", encoding="utf-8") as fh:
            for line in fh:
                for token in re.findall(r"-?\d+", line):
                    PValues.append(int(token))
    except FileNotFoundError:
        print(f"Error: File '{PFilename}' not found.")
    except Exception as e:
        print(f"Error reading '{PFilename}': {e}")

def bubbleSort(PNums: list[int]) -> list[int]:
    n = len(PNums)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if PNums[j] > PNums[j + 1]:
                PNums[j], PNums[j + 1] = PNums[j + 1], PNums[j]
                swapped = True
        if not swapped:
            break
    return PNums

def quickSort(PNums: list[int]) -> list[int]:
    if len(PNums) <= 1:
        return PNums[:]
    pivot = PNums[len(PNums) // 2]
    left  = [x for x in PNums if x <  pivot]
    mid   = [x for x in PNums if x == pivot]
    right = [x for x in PNums if x >  pivot]
    return quickSort(left) + mid + quickSort(right)

def measureSortingTime(PSortingAlgorithm: Callable, PArr: list[int]) -> int:
    start_ns = time.perf_counter_ns()
    PSortingAlgorithm(PArr)
    end_ns = time.perf_counter_ns()
    elapsed_ns = end_ns - start_ns
    return elapsed_ns

def printMenu() -> None:
    print("Options:")
    print("1 - Read dataset values")
    print("2 - Measure speeds")
    print("3 - Save results")
    print("0 - Exit")

def main() -> None:
    Values: list[int] = []
    Results: list[str] = []
    dataset_name: str | None = None

    print("Program starting.")

    while True:
        print()
        printMenu()
        choice = input("Your choice: ").strip()

        if choice == "1":
            dataset_name = input("Insert dataset filename: ").strip()
            readValues(Values, dataset_name)
            Results.clear()

        elif choice == "2":
            if not Values:
                print("No dataset loaded. Please choose option 1 first.")
                continue
            if dataset_name is None:
                print("No dataset name set. Please choose option 1 first.")
                continue
            builtin_ns = measureSortingTime(sorted, copy.deepcopy(Values))
            bubble_ns  = measureSortingTime(bubbleSort, copy.deepcopy(Values))
            quick_ns   = measureSortingTime(quickSort, copy.deepcopy(Values))

            print(f"Measured speeds for dataset '{dataset_name}':")
            print(f" - Built-in sorted {builtin_ns} ns")
            print(f" - Bubble sort {bubble_ns} ns")
            print(f" - Quick sort {quick_ns} ns")
            Results = [
                f"Measured speeds for dataset '{dataset_name}':",
                f" - Built-in sorted {builtin_ns} ns",
                f" - Bubble sort {bubble_ns} ns",
                f" - Quick sort {quick_ns} ns",
            ]

        elif choice == "3":
            if not Results:
                print("No results to save. Measure speeds first (option 2).")
                continue
            out_name = input("Insert results filename: ").strip()
            try:
                with open(out_name, "w", encoding="utf-8") as fh:
                    fh.write("\n".join(Results) + "\n")
                print(f"Results saved to '{out_name}'.")
            except Exception as e:
                print(f"Error saving results: {e}")

        elif choice == "0":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please select 0, 1, 2, or 3.")
    Values.clear()
    Results.clear()
    print("\nProgram ending.")

if __name__ == "__main__":
    main()
