########################################################
# Task A9_T4
# Milla Heinänen
# 2025-11-27
########################################################

TEMP_MIN = -200
TEMP_MAX = 1000

def collectCelsius():
    Celsius = float(input("Insert Celsius: "))
    if(Celsius < TEMP_MIN) or (Celsius > TEMP_MAX):
        raise Exception(f"{Celsius} out of range")
    return Celsius

def main():
    print("Program starting.")
    try:
        Celsius = collectCelsius()
        print(f"You inserted {Celsius} {chr(176)}C")
    except Exception as e:
        print(f"Error: {e}")
    print("Program ending.")
    return None
main()