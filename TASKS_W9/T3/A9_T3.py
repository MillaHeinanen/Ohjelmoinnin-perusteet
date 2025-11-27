########################################################
# Task A9_T3
# Milla Heinänen
# 2025-11-27
########################################################

import sys

def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    
    try:
        with open(filename, "r") as file:
            content = file.read().rstrip()
            print(f"## {filename} ##")
            print(content)
            print(f"## {filename} ##")
    except FileNotFoundError:
        print(f"Couldn't read file \"{filename}\".")
        sys.exit(1)
    print("Program ending.")
    return None
main()