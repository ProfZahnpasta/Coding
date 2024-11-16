import random
import time
import os
import pygame

run = True
again = False
gtnn = random.randint(0, 9)
with open("./gtnn.txt", "w") as file:
    file.write(str(gtnn)) 

with open("./language.txt", "r") as gtnfile:
    en_language = str(gtnfile.read())
if en_language == "True":
    en_language = True
else:
    en_language = False

pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("That was also close!")
font = pygame.font.Font(None, 40)
if en_language:
    text = font.render('Now you have to also close this! (Press SPACE!)', True, (0, 0, 0))
elif en_language == False:
    text = font.render('Das musst du jetzt auch schließen! (Drücke SPACE!)', True, (0, 0, 0))
text_rect = text.get_rect(center=(400, 300))

gn = None

while run:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and gn is None and again == False:
                if en_language:
                    text = font.render("Guess a number between 0 and 9", True, (0,0,0))
                elif en_language == False:
                    text = font.render("Rate eine Zahl zwischen 0 und 9", True, (0,0,0))
                text_rect = text.get_rect(center=(400, 300))
                screen.fill((255, 255, 255))
                screen.blit(text, text_rect)
                pygame.display.update()

            if event.key in range(pygame.K_0, pygame.K_9 + 1):
                gn = event.key - pygame.K_0

                if gn == gtnn:
                    screen.fill((255, 255, 255))
                    pygame.display.update()
                    time.sleep(0.1)
                    if en_language:
                        text = font.render("Try pressing this number somewhere else!", True, (0,0,0))
                    elif en_language == False:
                        text = font.render("Versuch diese Zahl mal woanders einzugeben!", True, (0, 0, 0))
                    text_rect = text.get_rect(center=(400, 300))
                    screen.fill((255, 255, 255))
                    screen.blit(text, text_rect)
                    pygame.display.update()
                    time.sleep(2)
                    run = False
                elif gn < gtnn:
                    screen.fill((255, 255, 255))
                    pygame.display.update()
                    time.sleep(0.1)
                    if en_language:
                        text = font.render("Too low, try again!", True, (0,0,0))
                    elif en_language == False:
                        text = font.render("Zu tief, versuchs nochmal!", True, (0, 0, 0))
                    text_rect = text.get_rect(center=(400, 300))
                    screen.fill((255, 255, 255))
                    screen.blit(text, text_rect)
                    pygame.display.update()
                    gn = None
                    again = True
                elif gn > gtnn:
                    screen.fill((255, 255, 255))
                    pygame.display.update()
                    time.sleep(0.1)
                    if en_language:
                        text = font.render("Too high, try again!", True, (0,0,0))
                    elif en_language == False:
                        text = font.render("Zu hoch, versuchs nochmal!", True, (0, 0, 0))
                    text_rect = text.get_rect(center=(400, 300))
                    screen.fill((255, 255, 255))
                    screen.blit(text, text_rect)
                    pygame.display.update()
                    gn = None
                    again = True

    screen.fill((255, 255, 255))
    screen.blit(text, text_rect)
    pygame.display.update()

pygame.quit()

