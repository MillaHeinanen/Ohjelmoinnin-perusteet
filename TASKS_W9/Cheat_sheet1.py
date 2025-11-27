# # Virheenkäsittelyrakenne:
# # try-ohjelma yrittää toteuttaa toimenpiteen
# # except-osa suoritetaan, jos toimenpiteessä tapahtuu virhe
# # finally-osa on vapaaehtoinen, tekee virheenkäsittelyn jälkeiset toimet
# # ELI: yritetään jotain try:ssä, jos menee pieleen niin sit tehdään except kohta
# #  ja kun sekin on tehty niin jos haluaa, finally kohta

# def main():
#     sum = 0
#     Value = -1 # alustetaan Value arvoon, joka ei ole 0, jotta while silmukka alkaa
#     print("Program starting.")
#     while Value != 0: # jatketaan niin kauan kuin käyttäjä ei syötä 0
#         Feed = input("Insert a number, 0 to stop: ")
#         try: # try-ohjelma yrittää toteuttaa toimenpiteen
#             Value = float(Feed)
#             sum += Value
#         except ValueError: # except-osa suoritetaan, jos toimenpiteessä tapahtuu virhe// 
#             # ValueError tarttuu tyyppierroriin, jos syöte ei ole numero
#             print(f"Error! '{Feed}' is not a number.")
#         except Exception: #  Exception tarttuu mihin tahansa virheeseen
#             print(f"'{Feed}' is not a number.")
#         finally: # finally-osa on vapaaehtoinen, tekee virheenkäsittelyn jälkeiset toimet
#             print("Task completed.")
            
#     print(f"The sum of the given numbers is: {sum}")
#     print("Program ending.")
#     return None

# main()                

########################################################

#Itsenostettu virhetilanne

TEMP_MIN = -200
TEMP_MAX = 1000

def collectCelsius():
    '''
    This is a docstring.
    This function collects a Celsius temperature from user input.
    It raises an exception if the input is out of the allowed range.
    '''
    Celsius = float(input("Insert Celsius: "))
    if(Celsius < TEMP_MIN) or (Celsius > TEMP_MAX): # tarkistetaan onko arvo sallitulla välillä
        raise Exception(f"{Celsius} out of range") # Itsenostettu virhetilanne
    return Celsius

def main():
    print("Program starting.")
    try: # yritetään tätä osaa
        Celsius = collectCelsius()
        print(f"You inserted {Celsius} {chr(176)}C")
    except Exception as e: # jos virhe tapahtuu, suoritetaan tämä osa
        print(f"Error: {e}") # tulostetaan virheviesti
    print("Program ending.")
    return None
main()