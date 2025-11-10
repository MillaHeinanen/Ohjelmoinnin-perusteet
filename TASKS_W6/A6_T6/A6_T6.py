LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def shiftCharacter(char: str, alphabet: str) -> str:
    if char in alphabet:
        index = alphabet.index(char)
        new_index = (index + 13) % len(alphabet)
        return alphabet[new_index]
    return char

def rot13(text: str) -> str:
    result = ""
    for char in text:
        if char in LOWER_ALPHABETS:
            result += shiftCharacter(char, LOWER_ALPHABETS)
        elif char in UPPER_ALPHABETS:
            result += shiftCharacter(char, UPPER_ALPHABETS)
        else:
            result += char
    return result

def writefile(filename: str, content: str):
    with open(filename, "w", encoding="UTF-8") as filehandle:
        filehandle.write(content)
    return None

def main():
    print("Program starting.\n")
    print("Collecting plain text rows for ciphering.")
    lines = []
    while True:
        row = input("Insert row(empty stops): ")
        if not row:
            break
        lines.append(row)
    original_content = "\n".join(lines) + "\n"
    ciphered_content = rot13(original_content)
    print("\n### Ciphered text ###")
    print(ciphered_content)
    print("### Ciphered text ###")
    filename = input("Insert filename to save: ")
    writefile(filename, ciphered_content)
    print("Ciphered text saved!")
    print("Program ending.")
if __name__ == "__main__":
    main()