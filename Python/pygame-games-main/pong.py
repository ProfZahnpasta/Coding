import pygame
import math
import time
import random

pygame.init()

width = 1280
height = 720

screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Pong")
pygame.display.set_icon(pygame.image.load("./images/favicon3.jpg"))

font = pygame.font.Font(None,20)
font2 = pygame.font.Font(None,100)
font3 = pygame.font.Font(None,40)
copyright = font.render('© 2025 by assistantmaster', True, (150,150,150))

background = pygame.image.load("./images/background3.jpg")

p1y = 300
p2y = 300
ballx = screen.get_width()/2
bally = screen.get_height()/2

punkte1 = 0
punkte2 = 0
punkte1display = font3.render(f'Punkte: {punkte1}', True, (255,255,255))
punkte2display = font3.render(f'Punkte: {punkte2}', True, (255,255,255))

gamelength = 60

pspeed = 6
if random.randint(0,1) == 0:
    ballspeedx = 8
else:
    ballspeedx = -8
ballspeedy = random.uniform(-math.pi,math.pi)*2

for i in range(3, 0, -1):
    screen.blit(background, (0,0))
    pygame.draw.rect(screen, (255, 255, 255), (40, p1y, 10, 100))
    pygame.draw.rect(screen, (255, 255, 255), (screen.get_width()-50, p2y, 10, 100))
    pygame.draw.circle(screen, (255, 255, 255), (screen.get_width()/2, screen.get_height()/2),10)
    screen.blit(punkte1display, (20,20))
    screen.blit(punkte2display, (screen.get_width()-150,20))
    countdown_text = font2.render(str(i), True, (255, 255, 255))
    screen.blit(countdown_text, (screen.get_width() // 2 - countdown_text.get_width() // 2, screen.get_height() // 2 - countdown_text.get_height() // 2))
    screen.blit(copyright, (0,screen.get_height()-20))
    pygame.display.flip()
    pygame.time.delay(1000)

starttime = time.time()

clock = pygame.time.Clock()
running = True
while running:
    
    screen.blit(background, (0,0))
    pygame.draw.rect(screen, (255, 255, 255), (40, p1y, 10, 100))
    pygame.draw.rect(screen, (255, 255, 255), (screen.get_width()-50, p2y, 10, 100))
    pygame.draw.circle(screen, (255, 255, 255), (ballx, bally),10)
    currenttime = int(time.time() - starttime)
    timeleft = gamelength-currenttime
    timeleftmin = int(timeleft//60)
    timeleftsec = int(timeleft%60)
    if timeleftsec < 10:
        timeleftsec = f"0{timeleftsec}"
    punkte1display = font3.render(f'Punkte: {punkte1}', True, (255,255,255))
    punkte2display = font3.render(f'Punkte: {punkte2}', True, (255,255,255))
    timedisplay = font3.render(f'{timeleftmin}:{timeleftsec}', True, (255,255,255))
    screen.blit(punkte1display, (20,20))
    screen.blit(punkte2display, (screen.get_width()-150,20))
    screen.blit(timedisplay, (screen.get_width() // 2 - timedisplay.get_width() // 2, 20))
    screen.blit(copyright, (0,screen.get_height()-20))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and p1y > 0:
        p1y -= pspeed
    
    if keys[pygame.K_s] and p1y < screen.get_height()-100:
        p1y += pspeed
    
    if keys[pygame.K_UP] and p2y > 0:
        p2y -= pspeed
    
    if keys[pygame.K_DOWN] and p2y < screen.get_height()-100:
        p2y += pspeed

    ballx -= ballspeedx
    bally -= ballspeedy
    
    if bally <= 10 or bally >= screen.get_height()-10:
        ballspeedy = -ballspeedy

    if ballx <= 50 and ballx > 40 and p1y <= bally <= p1y + 100:
        ballspeedx = -ballspeedx
        ballspeedy += random.randint(-10,10)/2

    if ballx >= screen.get_width()-50 and ballx < screen.get_width()-40 and p2y <= bally <= p2y + 100:
        ballspeedx = -ballspeedx
        ballspeedy += random.randint(-10,10)/2

    
    if ballx < 0:
        punkte2 += 1
        ballx = screen.get_width()/2
        bally = screen.get_height()/2
        ballspeedx = 8
        ballspeedy = random.uniform(-math.pi,math.pi)*2

    if ballx > screen.get_width():
        punkte1 += 1
        ballx = screen.get_width()/2
        bally = screen.get_height()/2
        ballspeedx = -8
        ballspeedy = random.uniform(-math.pi,math.pi)*2

    if int(timeleft) == 0:
        if punkte1 == punkte2:
            winner_text = font2.render("Unentschieden!", True, (255, 255, 255))
        elif punkte1 > punkte2:
            winner_text = font2.render("Spieler 1 gewinnt!", True, (255, 255, 255))
        else:
            winner_text = font2.render("Spieler 2 gewinnt!", True, (255, 255, 255))
        screen.blit(winner_text, (screen.get_width() // 2 - winner_text.get_width() // 2, 100))
        pygame.display.flip()
        pygame.time.delay(3000)
        running = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()