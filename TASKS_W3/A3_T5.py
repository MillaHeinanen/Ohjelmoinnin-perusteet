# Create a temperature unit conversion program.
print("Program starting.\n")
# Start the program by listing options for the user:
print("Options: ")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")
choice=input("Your choice: ")
if choice=="1":
    celsius=float(input("Insert the amount of Celsius: "))
    fahrenheit=celsius*1.8+32
    print(f"{celsius} °C equals to {round(fahrenheit,1)} °F\n")
elif choice=="2":
    fahrenheit=float(input("Insert the amount of Fahrenheit: "))
    celsius=(fahrenheit-32)/1.8
    print(f"{fahrenheit} °F equals to {round(celsius,1)} °C\n")
elif choice=="0":
    print("Exiting...\n")
else:
    print("Unknown option.\n")
print("Program ending.")
    
    
# Prompt user to insert choice. After the decision to convert, ask the amount of current temperature (use the floating point datatype). Lastly show the converted value to the user.