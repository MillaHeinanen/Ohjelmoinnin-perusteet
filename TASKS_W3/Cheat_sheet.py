# # print("Welcome to the temp app!")
# # Temp=int(input("What is the temperature of CPU? "))
# # if(Temp>80):
# #     print("Warning, temperature too high!")
# # else:
# #     print("All cool, keep on going!")


# # Tee ohjelma joka testaa, onko annettu numero parillinen vai pariton.
# # numero=int(input("Anna numero: "))
# # if numero%2==0:
# #     print("Numero on parillinen.")
# # else:
# #     print("Numero on pariton.")

# # if(Temp>80):
# #     if(Temp>90):
# #         print("You are toast")
# #     else:
# #         print("Warning")
# # else:
# #     print("You are ok")
    
# # if(Temp>90):
# #     print("You are toast")
# # elif(Temp>80):
# #     print("Warning!")
# # else:
# #     print("You are ok")
    
# # # Tee ohjelma joka kysyy kahta nimeä. Testaa, kumpi nimistä on pidempi vai onko ne saman
# # #mittaisia.
# # name1=input("First name: ")
# # name2=input("Second name: ")
# # if len(name1)>len(name2):
# #     print(f"{name1} is longer than {name2}")
# # elif len(name2)>len(name1):
# #     print(f"{name2} is longer than {name1}")
# # else:
# #     print(f"{name1} and {name2} are the same length")

# # town="Lahti"
# # street="Mukkulankatu"
# # building=19
# # if(town=="Lahti" and street=="Mukkulankatu" and building==19):
# #     print("You are at LAB")
# # elif(town=="Lahti" and (street!="Mukkulankatu" or building!=19)):
# #     print("You are in the correct town, but check the street address again.")
# # elif not(town=="Lahti" and street=="Mukkulankatu" and building==19):
# #     print("You are completely lost...")

# import random
# # print(random.random())
# # print(random.randint(1,10))

# # Tee yksinkertainen kivi, sakset, paperi peli random-metodia käyttäen.
# vaihtoehdot=["kivi", "sakset", "paperi"]
# pelaaja=input("Valitse kivi, sakset tai paperi: ").lower()
# tietokone=random.choice(vaihtoehdot)
# print(f"Tietokone valitsi: {tietokone}")
# if pelaaja==tietokone:
#     print("Tasapeli!")
# elif (pelaaja=="kivi" and tietokone=="sakset") or \
#     (pelaaja=="sakset" and tietokone=="paperi") or \
#     (pelaaja=="paperi" and tietokone=="kivi"):
#         print("Voitit!")
# elif pelaaja in vaihtoehdot:
#     print("Hävisit!")
# else:
#     print("Virheellinen valinta.")
