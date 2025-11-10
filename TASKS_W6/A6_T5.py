DELIMITER = ";"

def analyseValues(Pvalues: str) -> str:
    count = 0
    sum = 0
    greatest = 0
    currentvaluestr = ""
    for character in Pvalues:
        if character == DELIMITER:
            value = int(currentvaluestr)
            if value > greatest:
                greatest = value
            sum += value
            count += 1
            currentvaluestr = ""
        else:
            currentvaluestr += character
    value = int(currentvaluestr)
    if value > greatest:
        greatest = value
    sum += value
    count += 1
    average = sum/count
    results = "Count;Sum;Greatest;Average\n"
    results += f"{count};{sum};{greatest};{average:.2f}\n"
    return results

def readValues(Pfilename: str) -> str:
    content = ""
    with open(Pfilename, "r") as filehandle:
        lines = filehandle.readlines()
        for i, row in enumerate(lines):
            content += row.strip()
            if i < len(lines) - 1:
                content += DELIMITER
    return content


def displayResults(Pfilename: str, Panalysis: str) -> None:
    print("#### Number analysis START ####")
    print(f'File "{Pfilename}" results:')
    print(Panalysis.strip())
    print("\n#### Number analysis - END ####")
    return None
    
def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    values = readValues(filename)
    analysis = analyseValues(values)
    displayResults(filename, analysis)
    print("Program ending.")
    
if __name__ == "__main__":
    main()