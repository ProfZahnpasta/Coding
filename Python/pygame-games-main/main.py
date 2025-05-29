import pygame
import random
import time
import subprocess

pygame.init()

width = 1280 
height = 720

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Minigames")
pygame.display.set_icon(pygame.image.load("./images/favicon.jpg"))

font = pygame.font.Font(None,20)
font2 = pygame.font.Font(None,100)
font3 = pygame.font.Font(None,40)
copyright = font.render('© 2025 by assistantmaster', True, (150,150,150))

jumpnrunimg_orig = pygame.image.load("./images/favicon1.png")
shooterimg_orig = pygame.image.load("./images/favicon2.jpg")
pongimg_orig = pygame.image.load("./images/favicon3.jpg")
flappyimg_orig = pygame.image.load("./images/favicon4.png")

background = pygame.image.load("./images/background.jpg")

jumpnrunimg = pygame.transform.scale(jumpnrunimg_orig, (250,250))
shooterimg = pygame.transform.scale(shooterimg_orig, (250,250))
pongimg = pygame.transform.scale(pongimg_orig, (250,250))
flappyimg = pygame.transform.scale(flappyimg_orig, (250,250))

jumpnrun = False
shooter = False
pong = False
flappy = False

prozess = None
window_hidden = False

clock = pygame.time.Clock()
running = True
while running:

    if prozess is not None and prozess.poll() is not None:
        jumpnrun = False
        shooter = False
        pong = False
        flappy = False
        prozess = None

    if prozess is not None:
        if not window_hidden:
            screen = pygame.display.set_mode((width, height), flags=pygame.HIDDEN)
            window_hidden = True
    else:
        if window_hidden:
            screen = pygame.display.set_mode((width, height), flags=pygame.SHOWN)
            window_hidden = False
        screen.blit(background, (0,0))

        mouse = pygame.mouse.get_pos()
        mouse_clicked = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_clicked = True

        if 132.5 < mouse[0] < 382.5 and 55 < mouse[1] < 305:
            img = pygame.transform.scale(jumpnrunimg_orig, (290,290))
            screen.blit(img, (112.5,35))
            if mouse_clicked and not jumpnrun:
                jumpnrun = True
                prozess = subprocess.Popen(['python', 'jumpnrun.py'], shell=True)
        else:
            img = pygame.transform.scale(jumpnrunimg_orig, (250,250))
            screen.blit(img, (132.5,55))

        if 132.5 < mouse[0] < 382.5 and 415 < mouse[1] < 665:
            img = pygame.transform.scale(shooterimg_orig, (290,290))
            screen.blit(img, (112.5,395))
            if mouse_clicked and not shooter:
                shooter = True
                prozess = subprocess.Popen(['python', 'shooter.py'], shell=True)
        else:
            img = pygame.transform.scale(shooterimg_orig, (250,250))
            screen.blit(img, (132.5,415))

        if 515 < mouse[0] < 765 and 55 < mouse[1] < 305:
            img = pygame.transform.scale(pongimg_orig, (290,290))
            screen.blit(img, (495,35))
            if mouse_clicked and not pong:
                pong = True
                prozess = subprocess.Popen(['python', 'pong.py'], shell=True)
        else:
            img = pygame.transform.scale(pongimg_orig, (250,250))
            screen.blit(img, (515,55))

        if 515 < mouse[0] < 765 and 415 < mouse[1] < 665:
            img = pygame.transform.scale(flappyimg_orig, (290,290))
            screen.blit(img, (495,395))
            if mouse_clicked and not flappy:
                flappy = True
                prozess = subprocess.Popen(['python', 'flappy.py'], shell=True)
        else:
            img = pygame.transform.scale(flappyimg_orig, (250,250))
            screen.blit(img, (515,415))
            
        if 897.5 < mouse[0] < 1147.5 and 55 < mouse[1] < 305:
            img = pygame.transform.scale(pongimg_orig, (290,290))
            screen.blit(img, (877.5,35))
            if mouse_clicked and not pong:
                pong = True
                prozess = subprocess.Popen(['python', 'pong.py'], shell=True)
        else:
            img = pygame.transform.scale(pongimg_orig, (250,250))
            screen.blit(img, (897.5,55))

        if 897.5 < mouse[0] < 1147.5 and 415 < mouse[1] < 665:
            img = pygame.transform.scale(pongimg_orig, (290,290))
            screen.blit(img, (877.5,395))
            if mouse_clicked and not pong:
                pong = True
                prozess = subprocess.Popen(['python', 'pong.py'], shell=True)
        else:
            img = pygame.transform.scale(pongimg_orig, (250,250))
            screen.blit(img, (897.5,415))

        screen.blit(copyright, (0,700))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()