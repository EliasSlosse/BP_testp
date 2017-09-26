# Dit is commentaar (commentarieer je programma)
# Labo_Intro Oef1


# naam = input("Wat is jouw naam?")
# voornaam = "Elias"
# leeftijd = int(input("Wat is jouw leeftijd?"))
# leeftijd = leeftijd + 10

#naam = "Slosse"
#print("Welkom", voornaam, "\t", naam)

#print("Welkom {0}. Jouw naam is {1}. \nJij bent {2:.2f} jaar.".format(voornaam, naam, leeftijd))
#------
#oef 5: driehoek oppervlakte
# basis = float(input("Geef de basis van de driehoek op : "))
# hoogte = float(input("Geef de hoogte van de driehoek op : "))
# opp = float(basis * hoogte/2)
#
# print("De oppervlakte bedraagt {0:.2f}".format(opp))
#-------
#oef 6: Werken met tijd
# dagen = float(input("Geef het aantal dagen op: "))
# uren = float(input("Geef het aantal uren op: "))
# minuten = float(input("Geef het aantal minuten op: "))
# seconden = float(input("Geef het aantal seconden op: "))
#
# tot = (dagen*60*60*24) + (uren*60*60) + (minuten*60) + (seconden)
#
# print("Het totale aantal seconden bedraagt {0:.0f}".format(tot))

#--alternatief
# dagen = int(input("Geef het aantal dagen op: ")) *60*60*24
# uren = int(input("Geef het aantal uren op: ")) *3600
# minuten = int(input("Geef het aantal minuten op: ")) *60
# seconden = int(input("Geef het aantal seconden op: "))
# time = dagen + uren + minuten + seconden

#print("Het totale aantal seconden bedraagt: ", time)
#------
#oef 7: werken met tijd

secg = int(input("Geef het aantal seconden op: "))

dagen = (secg/60/60/24)
uren = (secg/3600)
minuten = (secg/60)
seconden = secg


print("d:h:m:s -> {0:.0f}:{1:.0f}:{2:.0f}:{3:.0f}".format(dagen, uren, minuten, seconden))

test="dit is een eerste wijziging"
test2="dit is een tweede wijziging"