def frameWord(Pword):
    print("*" * (len(Pword)+4))
    print(f"* {Pword} *")
    print("*" * (len(Pword)+4))
    return None

def main() -> None:
    print("Program starting.")
    word = input("Insert word: ")
    print("")
    frameWord(word)
    print("\nProgram ending.")
    return None

main()