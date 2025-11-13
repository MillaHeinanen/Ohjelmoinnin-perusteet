DELIMITER = ";"
WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday")

class TIMESTAMP:
    def __init__(self):
        self.weekday: str = ""
        self.hour: str = ""
        self.consumption: float = 0.0
        self.price: float = 0.0
        
class DAY_USAGE:
    def __init__(self):
        self.weekday: str = ""
        self.total_consumption: float = 0.0
        self.total_cost: float = 0.0
        
def readTimestamps(Pfilename: str, Ptimestamps: list[TIMESTAMP]):
    print(f'Reading file "{Pfilename}".')
    Ptimestamps.clear()
    with open(Pfilename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines[1:]:
            line = line.strip()
            if line == "":
                continue
            columns = line.split(DELIMITER)
            ts = TIMESTAMP()
            ts.weekday = columns[0]
            ts.hour = columns[1]
            ts.consumption = float(columns[2])
            ts.price = float(columns[3])
            Ptimestamps.append(ts)
    return None

def analyseTimestamps(Ptimestamps: list[TIMESTAMP], Presults: list[str]):
    print("Analysing timestamps.")
    Presults.clear()
    day_usage_list: list[DAY_USAGE] = []
    for weekday in WEEKDAYS:
        day = DAY_USAGE()
        day.weekday = weekday
        day_usage_list.append(day)
    for ts in Ptimestamps:
        for day in day_usage_list:
            if ts.weekday == day.weekday:
                day.total_consumption += ts.consumption
                day.total_cost += ts.consumption * ts.price
    for day in day_usage_list:
        Presults.append(f" - {day.weekday} usage {day.total_consumption:.2f} kWh, cost {day.total_cost:.2f} €")
    return None

def displayResults(Presults: list[str]):
    print("Displaying results.")
    print("### Electricity consumption summary ###")
    for result in Presults:
        print(result)
    print("### Electricity consumption summary ###")
    return None

def main():
    print("Program starting.")
    timestamps: list[TIMESTAMP] = []
    results: list[str] = []
    filename = input("Insert filename: ").strip()
    readTimestamps(filename, timestamps)
    analyseTimestamps(timestamps, results)
    displayResults(results)
    timestamps.clear()
    results.clear()
    print("Program ending.")
    return None
if __name__ == "__main__":
    main()