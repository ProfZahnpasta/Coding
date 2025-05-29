import pygame
import random
import time

pygame.init()

width = 1280
height = 720

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("2D Shooter")
pygame.display.set_icon(pygame.image.load("./images/favicon2.jpg"))

font = pygame.font.Font(None,20)
font2 = pygame.font.Font(None,100)
font3 = pygame.font.Font(None,40)
copyright = font.render('© 2025 by assistantmaster', True, (150,150,150))

background = pygame.image.load("./images/background2.png")
player1 = pygame.image.load("./images/player1.png")
player2 = pygame.transform.flip(player1, True, False)
arrow_img = pygame.image.load("./images/arrow.png")

player1x = 20
player1y = 310
player2x = 1179
player2y = 310
playerspeed = 5
arrowspeed = 15
punkte1 = 0
punkte2 = 0
gamelength = 60

projectiles = []
can_shoot = {1: True, 2: True}

punkte1display = font3.render(f'Punkte: {punkte1}', True, (255,255,255))
punkte2display = font3.render(f'Punkte: {punkte2}', True, (255,255,255))

def shoot(player):
    if any(p["owner"] == player for p in projectiles):
        return
    if player == 1:
        projectile = {
            "x": player1x + player1.get_width(),
            "y": player1y + player1.get_height() // 2 - 5,
            "vx": arrowspeed,
            "owner": 1,
            "img": arrow_img
        }
        projectiles.append(projectile)
    if player == 2:
        projectile = {
            "x": player2x - 20,
            "y": player2y + player2.get_height() // 2 - 5,
            "vx": -arrowspeed,
            "owner": 2,
            "img": pygame.transform.flip(arrow_img, True, False)
        }
        projectiles.append(projectile)

def rects_collide(rect1, rect2):
    return (
        rect1[0] < rect2[0] + rect2[2] and
        rect1[0] + rect1[2] > rect2[0] and
        rect1[1] < rect2[1] + rect2[3] and
        rect1[1] + rect1[3] > rect2[1]
    )

for i in range(3, 0, -1):
    screen.blit(background, (0, 0))
    screen.blit(player1, (player1x,player1y))
    screen.blit(player2, (player2x,player2y))
    screen.blit(punkte1display, (20,20))
    screen.blit(punkte2display, (1130,20))
    countdown_text = font2.render(str(i), True, (255, 255, 255))
    screen.blit(countdown_text, (width // 2 - countdown_text.get_width() // 2, height // 2 - countdown_text.get_height() // 2))
    screen.blit(copyright, (0,700))
    pygame.display.flip()
    pygame.time.delay(1000)

starttime = time.time()

clock = pygame.time.Clock()
running = True
while running:
    currenttime = int(time.time() - starttime)
    timeleft = gamelength-currenttime
    timeleftmin = int(timeleft//60)
    timeleftsec = int(timeleft%60)
    if timeleftsec < 10:
        timeleftsec = f"0{timeleftsec}"
    punkte1display = font3.render(f'Punkte: {punkte1}', True, (255,255,255))
    punkte2display = font3.render(f'Punkte: {punkte2}', True, (255,255,255))
    timedisplay = font3.render(f'{timeleftmin}:{timeleftsec}', True, (255,255,255))

    screen.blit(background, (0, 0))
    screen.blit(player1, (player1x,player1y))
    screen.blit(player2, (player2x,player2y))
    screen.blit(copyright, (0,700))
    screen.blit(punkte1display, (20,20))
    screen.blit(punkte2display, (1130,20))
    screen.blit(timedisplay, (width // 2 - timedisplay.get_width() // 2, 20))

    for projectile in projectiles[:]:
        projectile["x"] += projectile["vx"]
        screen.blit(projectile["img"], (projectile["x"], projectile["y"]))

        if projectile["owner"] == 1:
            player_rect = (player2x, player2y, player2.get_width(), player2.get_height())
            proj_rect = (projectile["x"], projectile["y"], 20, 10)
            if rects_collide(proj_rect, player_rect):
                punkte1 += 1
                projectiles.remove(projectile)
        elif projectile["owner"] == 2:
            player_rect = (player1x, player1y, player1.get_width(), player1.get_height())
            proj_rect = (projectile["x"], projectile["y"], 20, 10)
            if rects_collide(proj_rect, player_rect):
                punkte2 += 1
                projectiles.remove(projectile)

        if projectile["x"] < 0 or projectile["x"] > width:
            projectiles.remove(projectile)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and player1y > 0:
        player1y -= playerspeed
    if keys[pygame.K_a] and player1x > 0:
        player1x -= playerspeed
    if keys[pygame.K_s] and player1y < 620:
        player1y += playerspeed
    if keys[pygame.K_d] and player1x < 1199:
        player1x += playerspeed

    if keys[pygame.K_SPACE]:
        if can_shoot[1]:
            shoot(1)
            can_shoot[1] = False
    else:
        can_shoot[1] = True

    if keys[pygame.K_UP] and player2y > 0:
        player2y -= playerspeed
    if keys[pygame.K_LEFT] and player2x > 0:
        player2x -= playerspeed
    if keys[pygame.K_DOWN] and player2y < 620:
        player2y += playerspeed
    if keys[pygame.K_RIGHT] and player2x < 1199:
        player2x += playerspeed

    if keys[pygame.K_RCTRL]:
        if can_shoot[2]:
            shoot(2)
            can_shoot[2] = False
    else:
        can_shoot[2] = True


    if int(timeleft) == 0:
        if punkte1 == punkte2:
            winner_text = font2.render("Unentschieden!", True, (255, 255, 255))
        elif punkte1 > punkte2:
            winner_text = font2.render("Spieler 1 gewinnt!", True, (255, 255, 255))
        else:
            winner_text = font2.render("Spieler 2 gewinnt!", True, (255, 255, 255))
        screen.blit(winner_text, (width // 2 - winner_text.get_width() // 2, 100))
        pygame.display.flip()
        pygame.time.delay(3000)
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()