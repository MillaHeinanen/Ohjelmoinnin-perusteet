
import re

def bubbleSort(PValues: list[int], PAsc: bool = True) -> None:
    n = len(PValues)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if (PAsc and PValues[j] > PValues[j + 1]) or (not PAsc and PValues[j] < PValues[j + 1]):
                PValues[j], PValues[j + 1] = PValues[j + 1], PValues[j]
                swapped = True
        if not swapped:
            break
    return None

def readValues(filename: str) -> list[int]:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    items = re.findall(r"-?\d+", content)
    return [int(x) for x in items]

def displayValues(values: list[int]) -> None:
    print(", ".join(str(v) for v in values))
