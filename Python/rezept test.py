portionen = int(input("Wie viele Portionen?"))
zutat1 = str(input("Was ist die erste Zutat(in Mehrzahl angeben)?"))
zutat2 = str(input("Was ist die zweite Zutat(in Mehrzahl angeben)?"))
zutat3 = str(input("Was ist die dritte Zutat(in Mehrzahl angeben)?"))
zutat1einheit = str(input("Was ist die Einheit für die erste Zutat(wenn es keine gibt, dann freilassen)?"))
zutat2einheit = str(input("Was ist die Einheit für die zweite Zutat(wenn es keine gibt, dann freilassen)?"))
zutat3einheit = str(input("Was ist die Einheit für die dritte Zutat(wenn es keine gibt, dann freilassen)?"))
print("Dies sind deine Zutaten:")
for x in [str(portionen*2) + " " + zutat1einheit + " " + zutat1, str(portionen*100) + " " + zutat2einheit + " " + zutat2, str(portionen*150) + " " + zutat3einheit + " " + zutat3]:

    print(x)
input("")

