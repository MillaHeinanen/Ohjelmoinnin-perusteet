from library import MONTHS, WEEKDAYS, count_by_year, count_by_month, count_by_weekday

def read_timestamps(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return [line.strip() for line in f if line.strip()]

def showOptions():
    print("\nOptions:")
    print("1 - Calculate amount of timestamps during year")
    print("2 - Calculate amount of timestamps during month")
    print("3 - Calculate amount of timestamps during weekday")
    print("0 - Exit")

def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    timestamps = read_timestamps(filename)

    while True:
        showOptions()
        choice = input("Your choice: ")

        if choice == "0":
            print("Exiting program.")
            break
        elif choice == "1":
            year = input("Insert year: ")
            print(f"Amount of timestamps during year '{year}' is {count_by_year(timestamps, year)}")
        elif choice == "2":
            month = input("Insert month: ")
            if month in MONTHS:
                print(f"Amount of timestamps during month '{month}' is {count_by_month(timestamps, month)}")
            else:
                print("Invalid month name.")
        elif choice == "3":
            weekday = input("Insert weekday: ")
            if weekday in WEEKDAYS:
                print(f"Amount of timestamps during weekday '{weekday}' is {count_by_weekday(timestamps, weekday)}")
            else:
                print("Invalid weekday name.")
        else:
            print("Invalid choice. Please select 0-3.")

    print("Program ending.")

if __name__ == "__main__":
    main()