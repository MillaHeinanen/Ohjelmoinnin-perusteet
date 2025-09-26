print("Program starting.")
print("Welcome to the unit conversion program!")
print("Follow the instructions below.\n")

print("Options:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")
choice=input("Your choice: ")
if choice=="1":
    print("\nLength options:")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")
    length_choice=input("Your choice: ")
    if length_choice=="1":
        meters=float(input("Insert meters: "))
        kilometers=meters/1000
        print(f"{meters} m is {round(kilometers,1)} km")
    elif length_choice=="2":
        kilometers=float(input("Insert the amount of kilometers: "))
        meters=kilometers*1000
        print(f"{kilometers} km is {round(meters,1)} m")
    elif length_choice=="0":
        print("Exiting...")
    else:
        print("Unknown option.\n")
elif choice=="2":
    print("\nWeight options:")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")
    weight_choice=input("Your choice: ")
    if weight_choice=="1":
        grams=float(input("Insert grams: "))
        pounds=grams/453.6
        print(f"{grams} g is {round(pounds,1)} lb")
    elif weight_choice=="2":
        pounds=float(input("Insert pounds: "))
        grams=pounds*453.6
        print(f"{pounds} lb is {round(grams,1)} g")
    elif weight_choice=="0":
        print("Exiting...")
    else:
        print("Unknown option.")
elif choice=="0":
    print("Exiting...")
else:
    print("Unknown option.")
print("\nProgram ending.")