import pygame
from datetime import datetime

now = datetime.now()

current_datetime = now.strftime("%Y-%m-%d %H:%M:%S")

pygame.init()
width = 640
height = 480
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

pygame.display.set_caption("Uhr")

font = pygame.font.Font(None,74)

text = font.render(current_datetime, True, (255,255,255))
text_rect = text.get_rect(center=(320,240))



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 180, 255))
    now = datetime.now()
    current_datetime = now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-5]
    text = font.render(current_datetime, True, (255,255,255))
    text_rect = text.get_rect(center=(width/2,height/2))
    screen.blit(text, text_rect)
    
    pygame.display.flip()
    
pygame.quit()