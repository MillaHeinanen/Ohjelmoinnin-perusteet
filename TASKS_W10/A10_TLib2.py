import re

def readValues(filename: str) -> list[int]:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    items = re.findall(r"-?\d+", content)
    return [int(x) for x in items]

def displayValues(values: list[int]) -> None:
    print(", ".join(str(v) for v in values))

def merge(PLeft: list[int], PRight: list[int], PMerge: list[int], PAsc: bool = True) -> None:
    i = j = k = 0
    lenL, lenR = len(PLeft), len(PRight)

    while i < lenL and j < lenR:
        if (PAsc and PLeft[i] <= PRight[j]) or (not PAsc and PLeft[i] >= PRight[j]):
            PMerge[k] = PLeft[i]
            i += 1
        else:
            PMerge[k] = PRight[j]
            j += 1
        k += 1

    while i < lenL:
        PMerge[k] = PLeft[i]
        i += 1; k += 1
    while j < lenR:
        PMerge[k] = PRight[j]
        j += 1; k += 1
    return None

def mergeSort(PValues: list[int], PAsc: bool = True) -> None:
    n = len(PValues)
    if n <= 1:
        return None

    mid = n // 2
    left = PValues[:mid]
    right = PValues[mid:]

    mergeSort(left, PAsc)
    mergeSort(right, PAsc)

    merge(left, right, PValues, PAsc)
    return None
