WEEKDAYS: tuple[str] = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
def readFile(Pfilename: str, Prows: list[str]) -> None:
    print(f'Reading file: "{Pfilename}".')
    Prows.clear()
    with open(Pfilename, "r", encoding="UTF-8") as file:
        header_skipped = False
        for line in file:
            line = line.strip()
            if not header_skipped:
                header_skipped = True
                continue
            if line != "":
                continue
            Prows.append(line)
    return None

def analyseTimestamps(Prows: list[str], Presults: list[str]) -> None:
    print("Analysing timestamps.")
    Presults.clear()
    WeekdayTimestampAmount: list[int] = [0] * len(WEEKDAYS)
    for row in Prows:
        for i, weekday in enumerate(WEEKDAYS):
            if row.startswith(weekday):
                WeekdayTimestampAmount[i] += 1
    for i, weekday in enumerate(WEEKDAYS):
        Presults.append(f" - {weekday} {WeekdayTimestampAmount[i]} stamps")
    return None

def displayResults(Presults: list[str]) -> None:
    print("Displaying results.")
    print("### Timestamp analysis ###")
    for result in Presults:
        print(result)
    print("### Timestamp analysis ###")
    return None

def main():
    print("Program starting.")
    rows: list[str] = []
    results: list[str] = []
    filename = input("Insert filename: ").strip()
    readFile(filename, rows)
    analyseTimestamps(rows, results)
    displayResults(results)
    rows.clear()
    results.clear()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()