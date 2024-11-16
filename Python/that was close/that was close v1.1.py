import pygame
import time
import random
import os


pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

pygame.display.set_caption("That was close!")

font = pygame.font.Font(None,50)
fontklein = pygame.font.Font(None,23)

regeln = True
text = font.render('That was close! V1.1', True, (255,255,255))
text2 = fontklein.render('Regeln: Wenn man das Spiel geschlossen hat, hat man es durchgespielt.', True, (0,0,0))
text3 = fontklein.render('Wenn das Spiel abgestürzt ist, gilt es nicht als durchgespielt.', True, (0,0,0))
text4 = fontklein.render('Die Kommandozeile zu schließen oder das Spiel über den Taskmanager zu beenden, ist nicht erlaubt.', True, (0,0,0))
text5 = fontklein.render('Deutsch', True, (0,0,0))
text6 = fontklein.render('English', True, (0,0,0))
text5_selected = font.render('• Deutsch', True, (0,0,0))
text6_selected = font.render('• English', True, (0,0,0))
text_rect = text.get_rect(center=(400,300))
text_rect2 = text2.get_rect(center=(400,400))
text_rect3 = text3.get_rect(center=(400,450))
text_rect4 = text4.get_rect(center=(400,500))
text_rect5 = text5.get_rect(center=(266,200))
text_rect6 = text6.get_rect(center=(266*2,200))
text_rect5_selected = text5_selected.get_rect(center=(266,200))
text_rect6_selected = text6_selected.get_rect(center=(266*2,200))

nebenfenster = False
altf4 = True
en_language = False
selected = "left"
language_selection = True
with open("./gtnn.txt", "w") as file:
    file.write("11")

def gtnncheck():
    nebenfenster = False
    if en_language:
        pygame.display.set_caption("Right!")
    elif en_language == False:
        pygame.display.set_caption("Richtig!")
    font = pygame.font.Font(None,20)
    if en_language:
        text = font.render("Have no idea? Look in the folder of this game!", True, (0,0,0))
    elif en_language == False:
        text = font.render("Ratlos? Guck doch mal im Ordner von diesem Spiel nach!", True, (0,0,0))
    text_rect = text.get_rect(center=(400,400))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.delay(3000)
    with open("./hint.txt", "w") as hintfile:
        if en_language:
            hintfile.write("Maybe try to drag and drop this file in the game window!")
        elif en_language == False:
            hintfile.write("Droppe diese Datei doch mal ins Game-Fenster!")

running = True
while running:
    screen.fill((0, 180, 255))

    screen.blit(text, text_rect)
        
    if language_selection:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    selected = "right"
                elif event.key == pygame.K_LEFT:
                    selected = "left"
                elif event.key == pygame.K_RETURN:
                    language_selection = False
                    en_language = selected == "right"
                    with open("./language.txt", "w") as file:
                        file.write(str(en_language))     
        if selected == "left":
            screen.blit(text5_selected, text_rect5_selected)
            screen.blit(text6, text_rect6)
        else:
            screen.blit(text5, text_rect5)
            screen.blit(text6_selected, text_rect6_selected)

    else:
        if regeln:
            if en_language:
                text2 = fontklein.render('Rules: If you managed to close the game, you\'ve won.', True, (0,0,0))
            elif en_language == False:
                text2 = fontklein.render('Regeln: Wenn man das Spiel geschlossen hat, hat man es durchgespielt.', True, (0,0,0))
            if en_language:
                text3 = fontklein.render('When the game has crashed, is\'nt it a valid win.', True, (0,0,0))
            elif en_language == False:
                text3 = fontklein.render('Wenn das Spiel abgestürzt ist, gilt es nicht als durchgespielt.', True, (0,0,0))
            if en_language:
                text4 = fontklein.render('To close the commandline or to quit the game using the taskmanager, is not allowed.', True, (0,0,0))
            elif en_language == False:
                text4 = fontklein.render('Die Kommandozeile zu schließen oder das Spiel über den Taskmanager zu beenden, ist nicht erlaubt.', True, (0,0,0))
            text_rect2 = text2.get_rect(center=(400,400))
            text_rect3 = text3.get_rect(center=(400,450))
            text_rect4 = text4.get_rect(center=(400,500))
            screen.blit(text2, text_rect2)
            screen.blit(text3, text_rect3)
            screen.blit(text4, text_rect4)

        
    for event in pygame.event.get():
        screen.blit(text, text_rect)
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT and altf4:
            regeln = False
            welchertext = random.randint(1, 15)
            if welchertext == 1:
                if en_language:
                    welchertext = "This would be the easy way."
                elif en_language == False:
                    welchertext = "Das wär der einfache Weg."
            if welchertext == 2:
                if en_language:
                    welchertext = "Not like this ._."
                elif en_language == False:
                    welchertext = "So nicht ._."
            if welchertext == 3:
                if en_language:
                    welchertext = "Did you really thought this would work xD"
                elif en_language == False:
                    welchertext = "Haste gedenkt ne xD"
            if welchertext == 4:
                if en_language:
                    welchertext = "Sadly not"
                elif en_language == False:
                    welchertext = "Leider nein"
            if welchertext == 5:
                if en_language:
                    welchertext = "Still NO"
                elif en_language == False:
                    welchertext = "Immer noch nicht"
            if welchertext == 6:
                if en_language:
                    welchertext = "What are you trying to achieve?"
                elif en_language == False:
                    welchertext = "Was versuchst du zu versuchen?"
            if welchertext == 7:
                if en_language:
                    welchertext = "Better luck next time!"
                elif en_language == False:
                    welchertext = "Ein Satz mit x"
            if welchertext == 8:
                if en_language:
                    welchertext = "Nope"
                elif en_language == False:
                    welchertext = "Dödum"
            if welchertext == 9 or welchertext == 11 or welchertext == 12 or welchertext == 13 or welchertext == 14 or welchertext == 15:
                if en_language:
                    welchertext = "You have to ESCape..."
                elif en_language == False:
                    welchertext = "Du musst ESCapen..."
            if welchertext == 10:
                if en_language:
                    welchertext = "Nice! Go on :o"
                elif en_language == False:
                    welchertext = "Gut! Weiter so :o"
            
            text = font.render(f"{welchertext}", True, (0,0,0))
            text_rect = text.get_rect(center=(400,300))
            pygame.display.flip()

        if keys[pygame.K_ESCAPE]:
            screen = pygame.display.set_mode((width, height), flags=pygame.HIDDEN)
            time.sleep(5)
            screen = pygame.display.set_mode((width, height), flags=pygame.SHOWN)
            if en_language:
                    pygame.display.set_caption("That was close!      (Dont press STRG + Q)")
            elif en_language == False:
                    pygame.display.set_caption("That was close!      (Drück nicht STRG + Q)")
            text = font.render("SIKE!", True, (255,0,0))
            text_rect = text.get_rect(center=(400,300))
        if keys[pygame.K_a] and keys[pygame.K_l] and keys[pygame.K_t] and keys[pygame.K_f] and keys[pygame.K_4]:
            font = pygame.font.Font(None,50)
            if en_language:
                    text = font.render("You\'ve won!", True, (0,0,0))
            elif en_language == False:
                    text = font.render("Du hast es geschafft!", True, (0,0,0))
            text_rect = text.get_rect(center=(400,300))
            screen.fill((0, 180, 255))
            screen.blit(text, text_rect)
            pygame.display.update()
            time.sleep(1)
            running = False
            if os.path.exists(".\hinweis.txt"):
                os.remove(".\hinweis.txt")

        
        if os.path.exists("./gtnn.txt"):
            with open("./gtnn.txt", "r") as gtnfile:
                gtnn = int(gtnfile.read())
        if (keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]) and keys[pygame.K_q]:
            os.system('py "./that_was_close_nebenfenster.py"')
            nebenfenster = True



        if event.type == pygame.KEYDOWN and nebenfenster == True:
            if gtnn == 0 and keys[pygame.K_0]:
                gtnncheck()
            elif gtnn == 1 and keys[pygame.K_1]:
                gtnncheck()
                """nebenfenster = False
                pygame.display.set_caption("Richtig!")
                font = pygame.font.Font(None,20)
                text = font.render("Ratlos? Guck doch mal im Ordner von diesem Spiel nach!", True, (0,0,0))
                text_rect = text.get_rect(center=(400,300))
                with open("./hinweis.txt", "w") as hintfile:
                    hintfile.write("Droppe diese Datei doch mal ins Fenster!")"""
            elif gtnn == 2 and keys[pygame.K_2]:
                gtnncheck()
                """nebenfenster = False
                pygame.display.set_caption("Richtig!")
                font = pygame.font.Font(None,20)
                text = font.render("Ratlos? Guck doch mal im Ordner von diesem Spiel nach!", True, (0,0,0))
                text_rect = text.get_rect(center=(400,300))
                with open("./hinweis.txt", "w") as hintfile:
                    hintfile.write("Droppe diese Datei doch mal ins Fenster!")"""
            elif gtnn == 3 and keys[pygame.K_3]:
                gtnncheck()
                """nebenfenster = False
                pygame.display.set_caption("Richtig!")
                font = pygame.font.Font(None,20)
                text = font.render("Ratlos? Guck doch mal im Ordner von diesem Spiel nach!", True, (0,0,0))
                text_rect = text.get_rect(center=(400,300))
                with open("./hinweis.txt", "w") as hintfile:
                    hintfile.write("Droppe diese Datei doch mal ins Fenster!")"""
            elif gtnn == 4 and keys[pygame.K_4]:
                gtnncheck()
                """nebenfenster = False
                pygame.display.set_caption("Richtig!")
                font = pygame.font.Font(None,20)
                text = font.render("Ratlos? Guck doch mal im Ordner von diesem Spiel nach!", True, (0,0,0))
                text_rect = text.get_rect(center=(400,300))
                with open("./hinweis.txt", "w") as hintfile:
                    hintfile.write("Droppe diese Datei doch mal ins Fenster!")"""
            elif gtnn == 5 and keys[pygame.K_5]:
                gtnncheck()
                """nebenfenster = False
                pygame.display.set_caption("Richtig!")
                font = pygame.font.Font(None,20)
                text = font.render("Ratlos? Guck doch mal im Ordner von diesem Spiel nach!", True, (0,0,0))
                text_rect = text.get_rect(center=(400,300))
                with open("./hinweis.txt", "w") as hintfile:
                    hintfile.write("Droppe diese Datei doch mal ins Fenster!")"""
            elif gtnn == 6 and keys[pygame.K_6]:
                gtnncheck()
                """nebenfenster = False
                pygame.display.set_caption("Richtig!")
                font = pygame.font.Font(None,20)
                text = font.render("Ratlos? Guck doch mal im Ordner von diesem Spiel nach!", True, (0,0,0))
                text_rect = text.get_rect(center=(400,300))
                with open("./hinweis.txt", "w") as hintfile:
                    hintfile.write("Droppe diese Datei doch mal ins Fenster!")"""
            elif gtnn == 7 and keys[pygame.K_7]:
                gtnncheck()
                """nebenfenster = False
                pygame.display.set_caption("Richtig!")
                font = pygame.font.Font(None,20)
                text = font.render("Ratlos? Guck doch mal im Ordner von diesem Spiel nach!", True, (0,0,0))
                text_rect = text.get_rect(center=(400,300))
                with open("./hinweis.txt", "w") as hintfile:
                    hintfile.write("Droppe diese Datei doch mal ins Fenster!")"""
            elif gtnn == 8 and keys[pygame.K_8]:
                gtnncheck()
                """nebenfenster = False
                pygame.display.set_caption("Richtig!")
                font = pygame.font.Font(None,20)
                text = font.render("Ratlos? Guck doch mal im Ordner von diesem Spiel nach!", True, (0,0,0))
                text_rect = text.get_rect(center=(400,300))
                with open("./hinweis.txt", "w") as hintfile:
                    hintfile.write("Droppe diese Datei doch mal ins Fenster!")"""
            elif gtnn == 9 and keys[pygame.K_9]:
                gtnncheck()
                """nebenfenster = False
                pygame.display.set_caption("Richtig!")
                font = pygame.font.Font(None,20)
                text = font.render("Ratlos? Guck doch mal im Ordner von diesem Spiel nach!", True, (0,0,0))
                text_rect = text.get_rect(center=(400,300))
                with open("./hinweis.txt", "w") as hintfile:
                    hintfile.write("Droppe diese Datei doch mal ins Fenster!")"""
            else:
                if en_language:
                    pygame.display.set_caption("Thats wrong. Try again.")
                elif en_language == False:
                    pygame.display.set_caption("Leider Falsch. Versuche es noch einmal.")
        
        if event.type == pygame.DROPFILE:
            dropped_file = event.file
            dateiname = os.path.basename(dropped_file)
            if dateiname == "hint.txt":
                altf4 = False
                if en_language:
                    text = fontklein.render("Hint: Did you try ALTF4?", True, (0,0,0))
                elif en_language == False:
                    text = fontklein.render("Hinweis: Hast du es schonmal mit ALTF4 versucht?", True, (0,0,0))
                text_rect = text.get_rect(center=(400,300))

        if event.type == pygame.QUIT and not altf4:
            if en_language:
                text = fontklein.render("I guess I forgot the seperation between all the letters...", True, (0,0,0))
            elif en_language == False:
                text = fontklein.render("Ich habe wohl die Trennung zwischen allen Buchstaben vergessen ...", True, (0,0,0))
            text_rect = text.get_rect(center=(400,300))
    

        

    pygame.display.flip()
if os.path.exists(".\language.txt"):
    os.remove(".\language.txt")
if os.path.exists(".\hint.txt"):
    os.remove(".\hint.txt")
if os.path.exists("./gtnn.txt"):
    os.remove("./gtnn.txt")
pygame.quit()