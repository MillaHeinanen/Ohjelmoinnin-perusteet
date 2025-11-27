########################################################
# Task A9_T1
# Milla Heinänen
# 2025-11-26
########################################################

def main():
    print("Program starting.\n")
    total_sum = 0.0
    
    while True:
        value = input("Insert a floating-point value (0 to stop): ")
        try:
            float_value = float(value)
            if float_value == 0:
                break
            total_sum += float_value
        except ValueError:
            print("Error! '{}' couldn't be converted to float.".format(value))
            continue
    print("\nFinal sum is {:.2f}".format(total_sum))
    print("Program ending.")

if __name__ == "__main__":
    main()