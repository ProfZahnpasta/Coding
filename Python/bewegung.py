import pygame
import random
import time

pygame.init()
width = 800
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bewegung")
window.fill((0, 180, 255))
player_x = 32
player_y = 32
clock = pygame.time.Clock()
rect = pygame.Rect(player_x, player_y, 64, 64)

running = True
while running:
    delta_time = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        
    keys = pygame.key.get_pressed()
    speed = 300
    if keys[pygame.K_RIGHT]:
        player_x += speed * delta_time

    if keys[pygame.K_LEFT]:
        player_x -= speed * delta_time
    
    if keys[pygame.K_DOWN]:
        player_y += speed * delta_time

    if keys[pygame.K_UP]:
        player_y -= speed * delta_time
        #if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        #    x = int(random.randint(1,350))
         #   y = int(random.randint(1,350))
          #  rect_height = int(random.randint(50,800))
           # rect_width = int(random.randint(50,500))
           # pygame.draw.rect(window, "red", (x, y, rect_width, rect_height))
            #pygame.display.update()
            #time.sleep(1)
    rect = pygame.Rect(player_x, player_y, 64, 64)

    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    if rect.collidepoint(mouse_pos) and mouse_click[0]:
        running = False
    window.fill((0, 180, 255))
        
    pygame.draw.rect(window, "red" , (player_x, player_y, 64, 64)) 

    pygame.display.update()
pygame.quit()
