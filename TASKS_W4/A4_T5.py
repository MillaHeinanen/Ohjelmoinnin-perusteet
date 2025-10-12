print("Program starting.\n")
start=int(input("Insert starting point: "))
stop=int(input("Insert stopping point: "))
inspection=int(input("Insert inspection point: "))
errors=[]
if start>=stop:
    errors.append("Starting value must be less than the stopping point value.")
if not (start<=inspection<=stop):
    errors.append("Inspection value must be within the range of start and stop.")
if errors:
    for error in errors:
        print(error)
else:
    print("\nFirst loop - inspection with break:")
    for i in range(start,stop):
        if i==inspection:
            break
        print(i, end=" ")
    print()

    print("Second loop - inspection with continue:")
    for i in range(start,stop):
        if i==inspection:
            continue
    print(i, end=" ")
    print()
print("Program ending")
