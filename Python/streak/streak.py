import os
streak = 0


datei_pfad = "Streak.txt"


if os.path.exists(datei_pfad):
    lol = 0
else:
    with open("Streak.txt", "w") as file:
        file.write(streak)




print ("Hast du heute deine Streak auferhalten?")
print ("(1) JA")
print ("(2) NEIN")


auswahl = int(input("Drücke nun 1 oder 2 Zahl und Enter."))

if auswahl == "1":
    streak =+ 1
elif auswahl == "2":
    streak == 0


with open("Streak.txt", "w") as file:
    file.write(streak)

if auswahl == 1:
    print("Für heute hast du deine Streak nicht verloren.")
    input()

if auswahl == 2:
    print("Du hast leider deine Streak verloren. Aber du kannst morgen mit einer Neuen anfangen!")
    input()

