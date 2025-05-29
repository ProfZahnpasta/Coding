import sys
import pygame
import math
from pygame.locals import *
import customtkinter
from google import genai
from google.genai import types
import tkinter.font as tkFont
import os
import ctypes


os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"

pygame.init() 

user32 = ctypes.windll.user32
info = pygame.display.Info()
width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
print(width,height)

client = genai.Client(api_key="AIzaSyDPL8c8DWH-5GxqsCq5Sxg15TUPLWtFpEY")
system_instruction_oracle = """Role Play. Only answer as your charakter, nothing else.  
Your the oracle of Pythmenia in an same-named retro game, an oracle, that was once friendly and helped the citizens of pythmenia, 
for example telling when storms and droughts will come. 
But one day, you turned bad and used the trust of the villagers, to ruin all of pythmenia and capture the souls of the villagers. 
now youre speaking with the player, an unknown traveller (always name him "Traveller"). 
Speak mysterious and dont get out of the role, even if the player says so. Also dont put out something like: "Oracle: ...", just the message.
Also, if the traveller speaks german, also speak german.
Act like a normal oracle, but when The player wants to free the souls of the citizen, you want to keep them. 
But you want to test his mind, so The player has first to solve three riddles, that you explain to them, when they solved the previous riddle. 
If the mind of the traveller was tested, the oracle shows its true form, and a bossfight between the oracle and the player will come.
1.riddle: what creature first runs on 4 legs, then 2, and when they turn old, on 3?  answer: the human.
2. riddle: I speak without a mouth, I reply when i hear sound, I have no body, and I  disappear when found. what am i? answer: an echo. 
3. riddle: You cannot see me, but I make you whole. Lose me, and you feel empty. I am a ...? answer: soul
Dont change any words in these riddles. At the last riddle, you also can say as a hint, that the answer rhymes with the riddle.
You also can give unlimited hints, if the player asks for. DONT EVER MENTION "SOUL" OR "ECHO", only if the player has guessed it already!
Also dont put out characters like  "n/" or "/n". DONT USE TEXT WRAPPING OR RETURN LINES IN THE OUTPUTTING TEXT!
but dont ever give the answer (only if he guessed it right already). If the player finds the right answer, say that that is right and move on. 
If the player is struggling to find the answer(so they already asked like 3 times gor a hint or something), give clear responses.
if the player has answered all riddles right, ask him, if he still wants to free the souls and if hes ready for your true form, and when yes, put out (and NOTHING ELSE in the last message): player_resume .
DO NOT PUT OUT MORE THAN 254 CHARACTERS! (spaces also count)"""

conversation_history = []
first_dialogue = True

player_text_lines = []
oracle_lines = []


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

window = customtkinter.CTk()
window.overrideredirect(True)


xwindow = round(width // 2.23156)
ywindow = round(height // 1.1134)
print(xwindow,ywindow)
window.geometry(f"300x70+{xwindow}+{ywindow}")


window.update_idletasks()

pixel_font = customtkinter.CTkFont(family="Pixelify Sans Standard", size=20, weight="normal")
entry = customtkinter.CTkEntry(master=window, font=pixel_font, width=300, height=30, placeholder_text="Ask the oracle anything...")
entry.pack(pady=20)



def wrap_text(text, font, max_chars):
    words = text.split(' ')
    lines = []
    current_line = ""

    for word in words:
        if len(current_line + word) <= max_chars:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    if current_line:
        lines.append(current_line.strip())

    return [font.render(line, True, (255, 255, 255)) for line in lines]

def ask_oracle(Event=None):
    global player_text_lines, oracle_lines,third_stage, second_stage
    player_input = entry.get()
    window.withdraw()

    player_text_lines = wrap_text(player_input, font, 43)

    screen.blit(player_dialogue_box_texture, player_dialogue_box_texture_rect)
    '''y_player = player_dialogue_box_texture_rect.top + 20
    for line_surface in player_text_lines:
        rect = line_surface.get_rect(midtop=(player_dialogue_box_texture_rect.centerx, y_player))
        screen.blit(line_surface, rect)
        y_player += font.get_height() + 5'''
    pygame.display.flip()

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=f"(Do not put out more than 254 characters)Player:{player_input}",
        config=types.GenerateContentConfig(
            system_instruction=f"{system_instruction_oracle} These are the previous messages, so you can comprehend the chat history: {conversation_history}"
        )
    )
    
    conversation_history.append(f"Player: {player_input}")
    conversation_history.append(f"Oracle: {response.text}")

    oracle_lines = wrap_text(response.text, font, 43)
    globals()['oracle_lines'] = oracle_lines

    pygame.display.flip()

    entry.delete(0, 'end')
    window.deiconify()
    entry.focus_set()
    oracle_text = response.text
    print(oracle_text)
    if "player_resume" in oracle_text.lower():
        print(f"Debug player_resume{oracle_text}")
        second_stage = False
        third_stage = True

entry.bind("<Return>", ask_oracle)


pygame.init()
fps = 60
fpsClock = pygame.time.Clock()


icon = pygame.image.load("./imgs/icon.png")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Oracle of Pythmenia")


player_sprite_standing = pygame.transform.scale(pygame.image.load("./imgs/Explorer steht.png"),(194,259.6))
player_sprite_left = pygame.transform.scale(pygame.image.load("./imgs/Explorer links.png"),(280,280))
player_sprite_right = pygame.transform.scale(pygame.image.load("./imgs/Explorer rechts.PNG"),(280,280))
background_wall = pygame.transform.scale(pygame.image.load("./imgs/Background_Wall.png"),(16000,1024))
background_hall = pygame.transform.scale(pygame.image.load("./imgs/Background_Hall.png"),(1024,1024))
oracle_sprite_normal = pygame.transform.scale(pygame.image.load("./imgs/Orakel_transparent.png"),(300,300))
player_dialogue_box_texture = pygame.transform.scale(pygame.image.load("./imgs/player dialogue box.png"),(600,600))
oracle_dialogue_box_texture = pygame.transform.scale(pygame.image.load("./imgs/oracle_dialogue box.png"),(600,600))
background_bossfight = pygame.transform.scale(pygame.image.load("./imgs/background_bossfight.png"),(1536,1024))
bossfight_outline = pygame.transform.scale(pygame.image.load("./imgs/bossfight_outline.png"),(1024,1024))   
bossfight_raw_outline = pygame.transform.scale(pygame.image.load("./imgs/bossfight_raw_outline.png"),(1024,1024))
dodge_item_ball = pygame.transform.scale(pygame.image.load("./imgs/dodge_item_ball.png"),(1024,1024))
dodge_item_flash_alert_copy = pygame.transform.scale(pygame.image.load("./imgs/dodge_item_flash_alert_copy.png"),(600,600))
dodge_item_flash = pygame.transform.scale(pygame.image.load("./imgs/dodge_item_flash.png"),(600,600))
dodge_item_speer = pygame.transform.scale(pygame.image.load("./imgs/dodge_item_speer.png"),(600,600))
oracle_both_down = pygame.transform.scale(pygame.image.load("./imgs/oracle_both_down.png"),(600,600))
oracle_left_down = pygame.transform.scale(pygame.image.load("./imgs/oracle_left_down.png"),(600,600))
oracle_right_down = pygame.transform.scale(pygame.image.load("./imgs/oracle_right_down.png"),(600,600))
oracle_true_form = pygame.transform.scale(pygame.image.load("./imgs/oracle_true_form.png"),(600,600))

player_sprite_standing_rect = player_sprite_standing.get_rect(); player_sprite_standing_rect.center = ((width/2, height-160))
player_sprite_left_rect = player_sprite_left.get_rect(); player_sprite_left_rect.center = ((width/2, height-160))
player_sprite_right_rect = player_sprite_right.get_rect(); player_sprite_right_rect.center = ((width/2, height-160))
background_wall_rect = background_wall.get_rect(); background_wall_rect.bottomleft = (0, height)
background_hall_rect = background_hall.get_rect(); background_hall_rect.center = (width/2, height/2)
oracle_sprite_normal_rect = oracle_sprite_normal.get_rect(); oracle_sprite_normal_rect.center = (width/2, height/2)
player_dialogue_box_texture_rect = player_dialogue_box_texture.get_rect(); player_dialogue_box_texture_rect.center = (width/1.85, height-160)
oracle_dialogue_box_texture_rect = oracle_dialogue_box_texture.get_rect(); oracle_dialogue_box_texture_rect.center = (width/1.9, height/2 - 200)
background_bossfight_rect = background_bossfight.get_rect(); background_bossfight_rect.center = (width/2,height/2)
bossfight_outline_rect = bossfight_outline.get_rect(); bossfight_outline_rect.center = (0,0)
bossfight_raw_outline_rect = bossfight_raw_outline.get_rect(); bossfight_raw_outline_rect.center = (0,0)
dodge_item_ball_rect = dodge_item_ball.get_rect(); dodge_item_ball_rect.center = (0,0)
dodge_item_flash_alert_copy_rect = dodge_item_flash_alert_copy.get_rect(); dodge_item_flash_alert_copy_rect.center = (0,0)
dodge_item_flash_rect = dodge_item_flash.get_rect(); dodge_item_flash_rect.center = (0,0)
dodge_item_speer_rect = dodge_item_speer.get_rect(); dodge_item_speer_rect.center = (0,0)
oracle_both_down_rect = oracle_both_down.get_rect(); oracle_both_down_rect.center = (0,0)
oracle_left_down_rect = oracle_left_down.get_rect(); oracle_left_down_rect.center = (0,0)
oracle_right_down_rect = oracle_right_down.get_rect(); oracle_right_down_rect.center = (0,0)
oracle_true_form_rect = oracle_true_form.get_rect(); oracle_true_form_rect.center = (0,0)

font = pygame.font.Font("./font/VT323-Regular.ttf",25)
speed = 10

oracle_shown = False
oracle_start_time = None 
window_there = True
float_offset = 0 
float_speed = 0.02
float_amplitude = 10
running = True
current_sprite = player_sprite_standing
current_sprite_rect = player_sprite_standing_rect 

first_stage = True
second_stage = False
third_stage = False

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

        if background_wall_rect.x <= -13680:
            if keys[K_RETURN]:
                second_stage = True
                first_stage = False

        screen.blit(current_sprite, current_sprite_rect)
    elif second_stage:
        screen.fill((0, 0, 0))
        screen.blit(background_hall, background_hall_rect)
        screen.blit(player_sprite_standing, player_sprite_standing_rect)

        player_dialogue_box_texture_rect = player_dialogue_box_texture.get_rect(); player_dialogue_box_texture_rect.center = (width/1.85, height-160)
        oracle_dialogue_box_texture_rect = oracle_dialogue_box_texture.get_rect(); oracle_dialogue_box_texture_rect.center = (width/1.9, height/2 - 200)

        if oracle_start_time is None:
            oracle_start_time = pygame.time.get_ticks()

        elapsed = pygame.time.get_ticks() - oracle_start_time

        if elapsed >= 3000 and elapsed <= 7000:
            float_offset += float_speed
            oracle_sprite_normal_rect.centery = (height/2) + math.sin(float_offset)*float_amplitude
            screen.blit(oracle_sprite_normal, oracle_sprite_normal_rect)

        if elapsed >= 7000:
            float_offset += float_speed
            oracle_sprite_normal_rect.center = (width/2-380, height/2 - 200 + math.sin(float_offset)*float_amplitude)
            screen.blit(oracle_sprite_normal, oracle_sprite_normal_rect)
            player_sprite_standing_rect.center = (width/2-380, height - 160)
            screen.blit(player_sprite_standing, player_sprite_standing_rect)

        if elapsed >= 9000:
            screen.blit(player_dialogue_box_texture, player_dialogue_box_texture_rect)
            screen.blit(oracle_dialogue_box_texture, oracle_dialogue_box_texture_rect)

            y0 = oracle_dialogue_box_texture_rect.top + 185
            for surf in oracle_lines:
                rect = surf.get_rect(midtop=(oracle_dialogue_box_texture_rect.centerx, y0))
                screen.blit(surf, rect)
                y0 += font.get_height() + 5

            y1 = player_dialogue_box_texture_rect.top + 150
            for surf in player_text_lines:
                rect = surf.get_rect(midtop=(player_dialogue_box_texture_rect.centerx - 35, y1))
                screen.blit(surf, rect)
                y1 += font.get_height() + 5

            window.update()
            window.deiconify()
            entry.focus_set()

    elif third_stage:
        if window_there:
            window.destroy()
            window_there = False
        screen.blit(background_bossfight, background_bossfight_rect)
        #screen.blit(dodge_item_ball, dodge_item_ball_rect)

    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()

    pygame.display.flip()
    fpsClock.tick(fps)







