# # Poistumiskoodiharjoitus
# # sys.exit(0) -> ohjelma päättyy onnistuneesti
# # Ohjelman kaatuessa koodi järjestelmälle voi olla 1-255
# # sys.exit(1) -> ohjelma päättyy epäonnistuneesti
# # sys.exit() 
# import sys

# def main():
#     print("Program starting.")
#     Feed = input("Insert exit code(0-255): ")
#     ExitCode = int(Feed)
#     if ExitCode == 0:
#         print("Clean exit.")
#     else:
#         print("Error code.")
#     sys.exit(ExitCode) # Järjestelmälle tieto ohjelman lopetuksesta
#     print("Program ending.")
#     return None
# main()
# # echo "$?" terminaalin komentoriville näyttää edellisen ohjelman poistumiskoodin
########################################################

# Tiedostojen hallinta ja virheidenkäsittely sekä exit komento

import sys

def readLines(Filename: str, Lines: list[str]):
    try:
        Filehandle = open(Filename, "r", encoding="utf-8") # avaa tiedosto filename, lue ("r") muotoisena, utf-8 koodauksella
        Line = Filehandle.readline() # luetaan ensimmäinen rivi
        while Line != "": # niin kauan kuin filessä on sisältöä, käydään filea läpi
            Lines.append(Line) # lisätään rivi listaan
            Line = Filehandle.readline() # luetaan seuraava rivi
    except Exception: # jos tiedoston avaamisessa tai lukemisessa tapahtuu virhe
        print("Could not read file")
        sys.exit(1) # poistutaan ohjelmasta virhekoodilla 1
    return None

def main():
    print("Program starting.")
    Lines: list[str] = [] # Lista merkkijonoja riveille
    Filename = input("Insert filename: ")
    readLines(Filename, Lines) # kutsutaan funktiota
    for Line in Lines: # haetaan kaikki rivit listasta
        print(Line.strip()) # tulostetaan rivi ilman ylimääräisiä välilyöntejä
    print("Program ending.")
    
    return None
main()

