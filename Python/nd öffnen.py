import pygame
from datetime import datetime

now = datetime.now()

current_datetime = now.strftime("%Y-%m-%d %H:%M:%S")

pygame.init()
width = 1000
height = 480
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Uhr")

font = pygame.font.Font(None,74)

text = font.render('Du kannst das nicht schließen lol', True, (255,255,255))
text_rect = text.get_rect(center=(500,240))



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            text = font.render('Nicht so', True, (0,0,0))
    screen.fill((0, 180, 255))

    
    
    screen.blit(text, text_rect)
    
    pygame.display.flip()
    
pygame.quit()