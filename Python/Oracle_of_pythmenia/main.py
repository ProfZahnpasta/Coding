import sys
 
import pygame
from pygame.locals import *
 
pygame.init()
 
fps = 60
fpsClock = pygame.time.Clock()
 
width, height = 1400, 800
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Oracle of Pythmenia")

player_sprite_standing = pygame.image.load("Oracle_of_pythmenia\imgs\Explorer steht.png")
player_sprite_standing = pygame.transform.scale(player_sprite_standing,(194,259.6))
player_sprite_standing_rect = player_sprite_standing.get_rect()
player_sprite_standing_rect.center = ((1400/2, 800/1.5))


player_sprite_left = pygame.image.load("Oracle_of_pythmenia\imgs\Explorer links.png")
player_sprite_left = pygame.transform.scale(player_sprite_left,(280,280))
player_sprite_left_rect = player_sprite_left.get_rect()
player_sprite_left_rect.center = ((1400/2, 800/1.5))


player_sprite_right = pygame.image.load("Oracle_of_pythmenia\imgs\Explorer rechts.PNG")
player_sprite_right = pygame.transform.scale(player_sprite_right,(280,280))
player_sprite_right_rect = player_sprite_right.get_rect()
player_sprite_right_rect.center = ((1400/2, 800/1.5))

running = True
current_sprite = player_sprite_standing  # Start with the standing sprite
current_sprite_rect = player_sprite_standing_rect 

while running:
    screen.fill((0, 180, 255))
    
    # Check which keys are currently pressed
    keys = pygame.key.get_pressed()
    if keys[K_a]:  # If 'A' is held down
        current_sprite = player_sprite_left
        current_sprite_rect = player_sprite_left_rect
    elif keys[K_d]:  # If 'D' is held down
        current_sprite = player_sprite_right
        current_sprite_rect = player_sprite_right_rect
    else:  # If neither 'A' nor 'D' is held down
        current_sprite = player_sprite_standing
        current_sprite_rect = player_sprite_standing_rect

    # Draw the current sprite
    screen.blit(current_sprite, current_sprite_rect)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.flip()
    fpsClock.tick(fps)