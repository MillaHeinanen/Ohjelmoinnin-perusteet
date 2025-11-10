import os
LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DELIMITER = ";"

def readfile(Pfilename):
    content = ""
    filehandle = open(Pfilename, "r")
    row = filehandle.readline()
    while row != "":
        content += row
        row = filehandle.readline()
    filehandle.close()
    return content

def writefile(filename, content):
    with open(filename, "w") as filehandle:
        filehandle.write(content)
    return None

def appendtofile(filename, content):
    with open(filename, "a") as filehandle:
        filehandle.write(content)
    return None

def shiftCharacter(Character: str, Alphabets: str, Shift: int = 13) -> str:
    """Shifts a character by 'Shift' positions in the given alphabet (ROT13 logic)."""
    NewCharacter = Character
    for i in range(len(Alphabets)):
        if Character == Alphabets[i]:
            ShiftedIndex = (i + Shift) % len(Alphabets)
            NewCharacter = Alphabets[ShiftedIndex]
            break

    return NewCharacter

def rot(PContent: str, PShift: int = 13) -> str:
    NewContent = ""
    for Character in PContent:
        if (Character in LOWER_ALPHABETS):  # Lowercase letter
            NewContent += shiftCharacter(Character, LOWER_ALPHABETS, PShift)
        elif (Character in UPPER_ALPHABETS):  # Uppercase letter
            NewContent += shiftCharacter(Character, UPPER_ALPHABETS, PShift)
        else:
            NewContent += Character  # Non-alphabet characters remain unchanged
    return NewContent

def getlocation(locationid):
    location = "unknown"
    if locationid == 1:
        location = "Galba's palace"
    elif locationid == 2:
        location = "Otho's palace"
    elif locationid == 3:
        location = "Vitellius's palace"
    elif locationid == 4:
        location = "Vespasian's palace"
    elif locationid == 0:
        location = "Home"
    return location
    

def main():
    print("Travel starting.")
    playerprogressfilename = "player_progress.txt"
    progress = readfile(playerprogressfilename)
    
    lines = [line for line in progress.strip().split('\n') if line.strip() != '']
    lastprogress = lines[-1].split(DELIMITER)

    currentlocationid = int(lastprogress[0])
    currentlocation = getlocation(currentlocationid)
    nextlocationid = int(lastprogress[1])
    nextlocation = getlocation(nextlocationid)
    passphrase = lastprogress[2]
    plainpassphrase = rot(passphrase)
    
    print(f"Currently at {currentlocation}.")
    print(f"Travelling to {nextlocation}...")
    print(f"...Arriving to the {nextlocation}.")
    print("Passing the guard at the entrance.")
    print(f"{plainpassphrase}!")
    print("Looking for the messsage in the palace...")
    gkgfilename = f"{nextlocationid}_{passphrase}.gkg"
    if not os.path.exists(gkgfilename):
        print(f"Error: {gkgfilename} not found!")
        return
    cipheredmessage = readfile(gkgfilename).split('\n')[0]
    print("Ah, there it is! Seems cryptic.")
    print("[Game] Progress autosaved!")
    appendtofile(playerprogressfilename, f"{currentlocationid};{nextlocationid};{passphrase};{cipheredmessage}")

    plain_message = rot(cipheredmessage)
    plainfilename = f"{nextlocationid}-{plainpassphrase}.txt"
    writefile(plainfilename, plain_message)

    print("Deciphering Emperor's message...")
    print("Looks like I've got now the plain version copy of the Emperor's message.")
    print("Time to leave...")
    print("Travel ending.")
    
    return None

main()