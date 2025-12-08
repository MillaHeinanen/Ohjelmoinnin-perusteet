########################################################
# Task A10_T1
# Milla Heinänen
# Date 2025-12-06
########################################################
def main():
    print("Program starting.")
    filename = input("Insert filename: ").strip()
    try:
        with open(filename, 'r') as file:
            lines = [line.strip() for line in file if line.strip()]
        
        print("# --- Vertically --- #")
        for value in lines:
            print(value)
        print("# --- Vertically --- #")

        print("# --- Horizontally --- #")
        print(", ".join(lines))
        print("# --- Horizontally --- #")
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    
    print("Program ending.")

if __name__ == "__main__":
    main()
