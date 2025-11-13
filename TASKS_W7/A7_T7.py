ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def load_config(filename):
    rotors = []
    reflector = ""
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if line.startswith("Rotor"):
                    rotors.append(line.split(":")[1].strip())
                elif line.startswith("Reflector"):
                    reflector = line.split(":")[1].strip()
    except FileNotFoundError:
        print(f"Config file '{filename}' not found. Using default rotors and reflector.")
        rotors = [
            "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
            "AJDKSIRUXBLHWTMCQGZNPYFVOE",
            "BDFHJLCPRTXVZNYEIWGAKMUSQO"
        ]
        reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
    return rotors, reflector

def rotate_rotors(positions):
    positions[0] = (positions[0] + 1) % 26
    if positions[0] == 0:
        positions[1] = (positions[1] + 1) % 26
        if positions[1] == 0:
            positions[2] = (positions[2] + 1) % 26
    return positions

def encode_letter(letter, rotors, positions, reflector):
    index = ALPHABET.index(letter)

    for i in range(3):
        rotor = rotors[i]
        pos = positions[i]
        shifted_letter = ALPHABET[(index + pos) % 26]
        index = (rotor.index(shifted_letter) - pos + 26) % 26

    index = ALPHABET.index(reflector[index])

    for i in reversed(range(3)):
        rotor = rotors[i]
        pos = positions[i]
        shifted_index = (index + pos) % 26
        letter_at_pos = rotor[shifted_index]
        index = (ALPHABET.index(letter_at_pos) - pos + 26) % 26

    return ALPHABET[index]

def encode_row(row, rotor_positions, rotors, reflector):
    converted_row = ""
    positions = rotor_positions.copy()

    for char in row.upper():
        if char not in ALPHABET:
            converted_row += char
            continue

        positions = rotate_rotors(positions)

        encoded_char = encode_letter(char, rotors, positions, reflector)
        converted_row += encoded_char

    return converted_row

def main():
    filename = input("Insert config(filename):").strip()
    rotors, reflector = load_config(filename)

    rotor_positions_init = [0, 0, 0]

    plugs = input("Insert plugs (y/n)?: ").strip().lower()
    if plugs == "y":
        print("No extra plugs implemented. Continuing without plugboard.")
    else:
        print("No extra plugs inserted.")
    print("Enigma initialized.\n")

    while True:
        row = input("Insert row (empty stops): ").upper()
        if not row:
            print("\nEnigma closing.")
            break

        rotor_positions = rotor_positions_init.copy()

        print()
        converted = encode_row(row, rotor_positions, rotors, reflector)
        for c_in, c_out in zip(row, converted):
            print(f'Character "{c_in}" illuminated as "{c_out}"')
        print(f'Converted row - "{converted}".\n')

if __name__ == "__main__":
    main()