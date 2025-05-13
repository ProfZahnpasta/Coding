import sys
import pygame
import math
from pygame.locals import *
import customtkinter
import google.generativeai as genai
import tkinter.font as tkFont

pygame.init()

info = pygame.display.Info()
width, height = info.current_w, info.current_h
#print(info.current_h)


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

window = customtkinter.CTk()
window.overrideredirect(True)
window.geometry("300x70+800+970")
window.update_idletasks()
#window.geometry("300x30+width/1.85+height-160")
#window.geometry("340x155")
#window.title("Ask the Oracle anything...")
#window.resizable(False, False)

x, y = 300, 200
#window.geometry(f"330x35+{x}+{y}")

def ask_oracle(event=None):
    window.destroy()
    player_input = entry.get()

pixel_font = customtkinter.CTkFont(family="Pixelify Sans Standard", size=20, weight="normal")
entry = customtkinter.CTkEntry(master=window, font=pixel_font, width=300, height=30,placeholder_text="Ask the oracle anything...")
entry.pack(pady=20)
entry.bind("<Return>", ask_oracle)  # ask_oracle



pygame.init()
 
fps = 60
fpsClock = pygame.time.Clock()
 

screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Oracle of Pythmenia")

player_sprite_standing = pygame.image.load("Oracle_of_pythmenia\imgs\Explorer steht.png")
player_sprite_standing = pygame.transform.scale(player_sprite_standing,(194,259.6))
player_sprite_standing_rect = player_sprite_standing.get_rect()
player_sprite_standing_rect.center = ((width/2, height-160))


player_sprite_left = pygame.image.load("Oracle_of_pythmenia\imgs\Explorer links.png")
player_sprite_left = pygame.transform.scale(player_sprite_left,(280,280))
player_sprite_left_rect = player_sprite_left.get_rect()
player_sprite_left_rect.center = ((width/2, height-160))


player_sprite_right = pygame.image.load("Oracle_of_pythmenia\imgs\Explorer rechts.PNG")
player_sprite_right = pygame.transform.scale(player_sprite_right,(280,280))
player_sprite_right_rect = player_sprite_right.get_rect()
player_sprite_right_rect.center = ((width/2, height-160))

background_wall = pygame.image.load("Oracle_of_pythmenia\imgs\Background_Wall.png")
background_wall = pygame.transform.scale(background_wall,(16000,1024))
background_wall_rect = background_wall.get_rect()
background_wall_rect.bottomleft = (0, height)
#background_wall.center = ((1400/2, 800/1.5))

background_hall = pygame.image.load("Oracle_of_pythmenia\imgs\Background_Hall.png")
background_hall = pygame.transform.scale(background_hall,(1024,1024))
background_hall_rect = background_hall.get_rect()
background_hall_rect.center = (width/2, height/2)

oracle_sprite_normal = pygame.image.load("Oracle_of_pythmenia\imgs\Orakel_transparent.png")
oracle_sprite_normal = pygame.transform.scale(oracle_sprite_normal,(300,300))
oracle_sprite_normal_rect = oracle_sprite_normal.get_rect()
oracle_sprite_normal_rect.center = (width/2, height/2)

player_dialogue_box_texture = pygame.image.load("Oracle_of_pythmenia\imgs\player dialogue box.png")
player_dialogue_box_texture = pygame.transform.scale(player_dialogue_box_texture,(600,600))
player_dialogue_box_texture_rect = player_dialogue_box_texture.get_rect()
player_dialogue_box_texture_rect.center = (width/1.85, height-160)



oracle_dialogue_box_texture = pygame.image.load("Oracle_of_pythmenia\imgs\oracle_dialogue box.png")
oracle_dialogue_box_texture = pygame.transform.scale(oracle_dialogue_box_texture,(600,600))
oracle_dialogue_box_texture_rect = oracle_dialogue_box_texture.get_rect()
oracle_dialogue_box_texture_rect.center = (width/1.9, height/2)


speed = 10
first_stage = False
second_stage = True
third_stage = False


oracle_shown = False
oracle_start_time = None 


float_offset = 0 
float_speed = 0.02
float_amplitude = 10

running = True
current_sprite = player_sprite_standing
current_sprite_rect = player_sprite_standing_rect 

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    
    keys = pygame.key.get_pressed()

    if first_stage:
        screen.fill((70, 144, 184, 255))
        
        
        screen.blit(background_wall, background_wall_rect)
        
        if keys[K_a]:
            current_sprite = player_sprite_left
            current_sprite_rect = player_sprite_left_rect
            
            if background_wall_rect.x + speed <= 0:
                background_wall_rect.x += speed  
        elif keys[K_d]:  
            current_sprite = player_sprite_right
            current_sprite_rect = player_sprite_right_rect
            
            if background_wall_rect.x - speed >= -(background_wall.get_width() - width):
                background_wall_rect.x -= speed  
        else:  
            current_sprite = player_sprite_standing
            current_sprite_rect = player_sprite_standing_rect
        #print(f"Background X: {background_wall_rect.x}")

        
        if background_wall_rect.x <= -13680:
            if keys[K_RETURN]:
                second_stage = True
                first_stage = False

        
        screen.blit(current_sprite, current_sprite_rect)

    elif second_stage:
        
        screen.fill((0, 0, 0))
        screen.blit(background_hall, background_hall_rect)
        screen.blit(player_sprite_standing, player_sprite_standing_rect)

        if oracle_start_time is None:
            oracle_start_time = pygame.time.get_ticks()

        elapsed_time = pygame.time.get_ticks() - oracle_start_time

        if elapsed_time >= 3000:  
            
            float_offset += float_speed
            float_y = math.sin(float_offset) * float_amplitude
            oracle_sprite_normal_rect.centery = (height / 2) + float_y

            
            screen.blit(oracle_sprite_normal, oracle_sprite_normal_rect)
            oracle_shown = True

        if elapsed_time >= 7000:
            oracle_sprite_normal_rect.center = (width/2-380, height/2)
            
            float_offset += float_speed
            float_y = math.sin(float_offset) * float_amplitude
            oracle_sprite_normal_rect.centery = (height / 2) + float_y

            
            screen.blit(oracle_sprite_normal, oracle_sprite_normal_rect)
            oracle_shown = True

            player_sprite_standing_rect.center = ((width/2-380, 920))
            screen.blit(player_sprite_standing, player_sprite_standing_rect)

        if elapsed_time >= 9000:
            screen.blit(player_dialogue_box_texture,player_dialogue_box_texture_rect)
            screen.blit(oracle_dialogue_box_texture,oracle_dialogue_box_texture_rect)
            window.mainloop()
    elif third_stage:
        screen.fill((0, 0, 0))

    
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()

    pygame.display.flip()
    fpsClock.tick(fps)