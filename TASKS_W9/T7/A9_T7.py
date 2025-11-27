########################################################
# Task A9_T7
# Milla Heinänen
# 2025-11-27
########################################################


import sys
import os

def showHelp() -> None:
    print("Invalid amount of arguments.")
    print("Usage: python copy_tool.py <source_file> <destination_file>")

def copyFile(PSrcFile: str, PDstFile: str) -> None:
    proceed = True
    if os.path.exists(PDstFile):
        overwrite = input(f"Destination file '{PDstFile}' exists. Overwrite? (y/n): ").strip().lower()
        if overwrite != "y":
            print("Operation cancelled.")
            proceed = False

    if proceed:
        try:
            with open(PSrcFile, "r", encoding="UTF-8") as src:
                content = src.read()
            with open(PDstFile, "w", encoding="UTF-8") as dst:
                dst.write(content)
            print(f"Copying file \"{PSrcFile}\" to \"{PDstFile}\".")
        except OSError:
            print(f"Error: Cannot copy file '{PSrcFile}' to '{PDstFile}'.")
            sys.exit(-1)

def main() -> None:
    if len(sys.argv) != 3:
        showHelp()
        sys.exit(-1)

    srcFile = sys.argv[1]
    dstFile = sys.argv[2]

    print("Program starting.")
    print(f"Source file \"{srcFile}\"")
    print(f"Destination file \"{dstFile}\"")

    if not os.path.exists(srcFile):
        print(f"Error: Source file '{srcFile}' does not exist.")
        sys.exit(-1)

    copyFile(srcFile, dstFile)

    print("Copying operation complete.")
    print("Program ending.")

if __name__ == "__main__":
    main()
