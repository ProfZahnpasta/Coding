import random
# start = str(input("Willst du starten? Dann drücke ENTER. Wenn du abbrechen willst drücke q und dann ENTER."))
score = 0
highscore = 0
lowscore = 0
versuche = 0
while True:
    # if start == "q":
    #    print("Du hast aufgehört. Dein Score ist:", score)
    #    break
    # else:
        fiftyfifty = random.randint(0,1)
        if fiftyfifty == 1:
            higher = True
        else:
            higher = False
        if higher == True:
            score += 1
        if higher == False:
            score -= 1
        versuche += 1
        #print("Dein aktueller Score ist:", score)
        if score > highscore:
            highscore = score#
        if score < lowscore:
            lowscore = score


        #print("(Highscore:" , highscore , ")")
        #print("(Lowscore:" , lowscore , ")")
        #print("Du hast bisher" , versuche , "Versuche gebraucht.")
        print(score, highscore, lowscore, versuche)
        if score == -15:
            #print("Dein Score ist unter -15 gesunken. Du hast verloren. Drücke ENTER um nochmal zu spielen.")
            #score = 0
            #versuche = 0
            continue
        if score == 100:
        #    print("Du hast den Score 100 erreicht und das Spiel durchgespielt. Wenn du aufhören willst, drücke q und dann ENTER.")
        #    freeplay = input("Willst du im Freeplay Modus weiterspielen? Dann drücke ENTER.")
        #    if freeplay == "q":
        #        break
        #    else:
            continue

        #repeat = input("Willst du weitermachen? Dann drücke ENTER. Wenn du aufhören willst, drücke q und dann ENTER.")
        repeat = 0
        if repeat == "q":
            print("Du hast aufgehört. Dein Score ist:", score)
            break
        else:
            continue


