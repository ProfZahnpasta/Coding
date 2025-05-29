import pygame
import random

pygame.init()

width = 1280
height = 720

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Flappy Bird")
pygame.display.set_icon(pygame.image.load("./images/favicon4.png"))

font = pygame.font.Font(None,20)
font2 = pygame.font.Font(None,40)
copyright = font.render('© 2025 by assistantmaster', True, (150,150,150))

background = pygame.image.load("./images/background4.png")
player = pygame.image.load("./images/flappy_bird.png")
pipetop = pygame.image.load("./images/pipe.png")
pipebottom = pygame.transform.flip(pipetop, False, True)

playerx = 50
playery = 300
playerspeed = 5
punkte = 0
pipespeedx = 5
pipefrequency = 120
pipegap = 150
pipesy = []
pipesx = []
pipestop = []
pipesbottom = []

def new_pipe():
    pipestop.append(pipetop)
    pipesbottom.append(pipebottom)
    pipesx.append(1280)
    pipesy.append(random.randint(200,500))

def move_pipes():
    for i in range(len(pipesx)):
        pipesx[i] -= pipespeedx
        screen.blit(pipestop[i], (pipesx[i], pipesy[i]-height))
        screen.blit(pipesbottom[i], (pipesx[i], pipesy[i]+pipegap))

def collision():
    player_rect = pygame.Rect(playerx, playery, player.get_width(), player.get_height())
    for i in range(len(pipesx)):
        top_rect = pygame.Rect(pipesx[i], pipesy[i] - pipetop.get_height(), pipetop.get_width(), pipetop.get_height())
        bottom_rect = pygame.Rect(pipesx[i], pipesy[i] + pipegap, pipebottom.get_width(), pipebottom.get_height())
        if player_rect.colliderect(top_rect) or player_rect.colliderect(bottom_rect):
            return True
        else:
            return False

pipeindex = 150

clock = pygame.time.Clock()
running = True
while running:

    screen.blit(background, (0,0))
    move_pipes()
    screen.blit(player, (playerx,playery))
    punktedisplay = font2.render(f'Punkte: {punkte}', True, (255,255,255))
    screen.blit(punktedisplay, (20, 20))
    screen.blit(copyright, (0,700))

    pipeindex += 1
    if pipeindex > pipefrequency:
        pipeindex = 0
        new_pipe()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if playery > 0:
            playery -= playerspeed
    else:
        if playery < 639:
            playery += playerspeed
    
    player_rect = pygame.Rect(playerx, playery, player.get_width(), player.get_height())
    for i in range(len(pipesx)):
        top_rect = pygame.Rect(pipesx[i], pipesy[i] - pipetop.get_height(), pipetop.get_width(), pipetop.get_height())
        bottom_rect = pygame.Rect(pipesx[i], pipesy[i] + pipegap, pipebottom.get_width(), pipebottom.get_height())
        if player_rect.colliderect(top_rect) or player_rect.colliderect(bottom_rect):
            pygame.time.delay(1000)
            running = False
    
    for i in pipesx:
        if pipesx[pipesx.index(i)] < 50 and pipesx[pipesx.index(i)] > 50 - 1.5*pipespeedx:
            punkte += 1
    
    if pipesx and pipesx[0] < -pipetop.get_width():
        pipesx.pop(0)
        pipesy.pop(0)
        pipestop.pop(0)
        pipesbottom.pop(0)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()