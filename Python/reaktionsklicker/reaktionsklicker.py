import pygame
import random
import time
import os

pygame.init()
width = 800
height = 600
window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Reaktionsklicker")
font = pygame.font.Font("D:\Eigene Dateien\Schule\Fächer\Informatik Berk\Python\Reaktionsklicker\Mina-Regular.ttf",30)
text = font.render("", True, (255,255,255))
text_rect = text.get_rect(center=(width//2, height//0.2))
window.fill((0, 180, 255))
x = int(random.randint(1,350))
y = int(random.randint(1,350))
rect = pygame.Rect(y, x, 64, 64)
zeit = 0
highscore = 256
clock = pygame.time.Clock()
file_path = "D:/Eigene Dateien/Schule/Fächer/Informatik Berk/Python/Reaktionsklicker/highscore.txt"
if not os.path.exists(file_path):
    with open("highscore.txt", "w") as file:
        file.write(str(highscore))
with open("highscore.txt", "r") as rfile:
    highscore = int(rfile.read())
if not highscore == 256:
    pygame.display.set_caption(f"Reaktionsklicker (Highscore: {highscore/100:.2f} Sekunden)")

running = True
while running:
    text_rect = text.get_rect(center=(width//2, height//2))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            if rect.collidepoint(mouse_pos):
                x = int(random.randint(1,width - 64))
                y = int(random.randint(1,height - 64))
                rect = pygame.Rect(x, y, 64, 64)
                if zeit < highscore:
                    highscore = zeit
                    with open("highscore.txt", "w") as file:
                        file.write(str(highscore))
                    pygame.display.set_caption(f"Reaktionsklicker (Highscore: {highscore/100:.2f} Sekunden)")
                textzeit = f"Deine Reaktionszeit: {zeit/100:.2f} Sekunden"
                text = font.render(textzeit, True, (255,255,255))
                zeit = 0

            elif not rect.collidepoint(mouse_pos):
                running = False
                window.fill((255, 0, 0))
                text = font.render("Verloren", True, (255,255,255))
                text_rect = text.get_rect(center=(width//2, height//2))
                window.blit(text, text_rect)
                pygame.display.update()
                time.sleep(2)
                pygame.quit()
    window.fill((0, 180, 255))
    clock.tick(100)
    zeit += 1
    window.blit(text, text_rect)
        
    pygame.draw.rect(window, "red" , rect) 

    pygame.display.update()
pygame.quit()
