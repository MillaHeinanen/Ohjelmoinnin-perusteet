DELIMITER = ";"

class TIMESTAMP:
    def __init__(self):
        self.weekday: str = ""
        self.hour: str = ""
        self.consumption: float = 0.0
        self.price: float = 0.0
        
def readTimestamps(Pfilename: str, Ptimestamps: list[TIMESTAMP]):
    print(f'Reading file: "{Pfilename}".')
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

def displayTimestamps(Ptimestamps: list[TIMESTAMP]):
    print("Electricity usage:")
    for ts in Ptimestamps:
        total = ts.consumption * ts.price
        print(f" - {ts.weekday} {ts.hour}, price {ts.price:.2f} €, consumption {ts.consumption:.2f} kWh, total {total:.2f} €")
    return None

def main():
    print("Program starting.")
    timestamps: list[TIMESTAMP] = []
    filename = input("Insert filename: ").strip()
    readTimestamps(filename, timestamps)
    displayTimestamps(timestamps)
    timestamps.clear()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()