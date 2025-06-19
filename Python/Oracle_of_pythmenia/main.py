import sys
import pygame
import math
import customtkinter
import google
import google.genai
import tkinter.font
import os
import ctypes
import random
import time

os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"

pygame.init() 

user32 = ctypes.windll.user32
info = pygame.display.Info()
#width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
width, height = 1920,1080
print(width,height)

client = google.genai.Client(api_key="AIzaSyDPL8c8DWH-5GxqsCq5Sxg15TUPLWtFpEY")
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


def get_mousclick_coords():
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        print(f"Mouse clicked at: ({x}, {y})")

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
        config=google.genai.types.GenerateContentConfig(
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

def move_dodge_item(rect, target_coords, speed):

    current_pos = pygame.Vector2(rect.center)
    target = pygame.Vector2(target_coords)
    direction = (target - current_pos)

    if direction.length() < speed or direction.length() == 0:
        rect.center = target_coords
    else:
        direction = direction.normalize() * speed
        new_pos = current_pos + direction
        rect.center = (round(new_pos.x), round(new_pos.y))

    return rect

def phase1_attack_3_normal_fast_balls1():
    global attack_start_time, attack_beginning, boss_pose
    global ball1_rect, ball2_rect, ball3_rect, dodge_item_ball
    global player_sprite_left, player_sprite_right, player_sprite_standing, player_sprite_up
    global player_sprite_left_rect, player_sprite_right_rect, player_sprite_standing_rect, player_sprite_up_rect
    global current_sprite
    dodge_speed = 20
    #global target_ball1_y, target_ball2_y, target_ball3_y
    if attack_beginning:
        attack_start_time = pygame.time.get_ticks()
        attack_beginning = False
        ball1_rect.center = (width//2 - 150, height//2 - 200)
        ball2_rect.center = (width//2 - 150, height//2 - 200)
        ball3_rect.center = (width//2 + 150, height//2 - 200)
        no_hit = True
        no_finish = True

    screen.blit(dodge_item_ball, ball1_rect)
    screen.blit(dodge_item_ball, ball2_rect)
    screen.blit(dodge_item_ball, ball3_rect)
    target_ball1_x, target_ball1_y = 660 ,1080
    target_ball2_x, target_ball2_y = 960 ,1080
    target_ball3_x, target_ball3_y = 1110 ,1080
    elapsed = pygame.time.get_ticks() - attack_start_time
    if elapsed >= 2000:
        ball1_rect = move_dodge_item(ball1_rect, (target_ball1_x, target_ball1_y), dodge_speed)
        ball2_rect = move_dodge_item(ball2_rect, (target_ball2_x, target_ball2_y), dodge_speed)
        ball3_rect = move_dodge_item(ball3_rect, (target_ball3_x, target_ball3_y), dodge_speed)
    if elapsed >= 2300:
        boss_pose = "both down"
    ball_mask1 = pygame.mask.from_surface(dodge_item_ball1)
    ball_mask2 = pygame.mask.from_surface(dodge_item_ball2)
    ball_mask3 = pygame.mask.from_surface(dodge_item_ball3)

    player_mask = pygame.mask.from_surface(current_sprite)

    for ball_rect, ball_mask in zip([ball1_rect, ball2_rect, ball3_rect], [ball_mask1, ball_mask2, ball_mask3]):
        offset = (ball_rect.x - current_sprite_rect.x, ball_rect.y - current_sprite_rect.y)
        if player_mask.overlap(ball_mask, offset):
            print("hit")
            return True#, boss_pose
            #no_hit = False
    
    if ball1_rect.centery >= target_ball1_y and ball2_rect.centery >= target_ball2_y and ball3_rect.centery >= target_ball3_y:
        return False#, boss_pose
        #no_finish = False

    #if no_hit and no_finish:
        #return None, boss_pose

def phase1_attack_3_normal_fast_balls2():
    global attack_start_time, attack_beginning, boss_pose
    global ball1_rect, ball2_rect, ball3_rect, dodge_item_ball
    global player_sprite_left, player_sprite_right, player_sprite_standing, player_sprite_up
    global player_sprite_left_rect, player_sprite_right_rect, player_sprite_standing_rect, player_sprite_up_rect
    global current_sprite
    dodge_speed = 20
    #global target_ball1_y, target_ball2_y, target_ball3_y
    if attack_beginning:
        attack_start_time = pygame.time.get_ticks()
        attack_beginning = False
        ball1_rect.center = (width//2 - 150, height//2 - 200)
        ball2_rect.center = (width//2 + 150, height//2 - 200)
        ball3_rect.center = (width//2 + 150, height//2 - 200)
        no_hit = True
        no_finish = True

    screen.blit(dodge_item_ball, ball1_rect)
    screen.blit(dodge_item_ball, ball2_rect)
    screen.blit(dodge_item_ball, ball3_rect)
    target_ball1_x, target_ball1_y = 810 ,1080
    target_ball2_x, target_ball2_y = 1110 ,1080
    target_ball3_x, target_ball3_y = 960 ,1080
    elapsed = pygame.time.get_ticks() - attack_start_time
    if elapsed >= 2000:
        ball1_rect = move_dodge_item(ball1_rect, (target_ball1_x, target_ball1_y), dodge_speed)
        ball2_rect = move_dodge_item(ball2_rect, (target_ball2_x, target_ball2_y), dodge_speed)
        ball3_rect = move_dodge_item(ball3_rect, (target_ball3_x, target_ball3_y), dodge_speed)
    if elapsed >= 2300:
        boss_pose = "both down"
    ball_mask1 = pygame.mask.from_surface(dodge_item_ball1)
    ball_mask2 = pygame.mask.from_surface(dodge_item_ball2)
    ball_mask3 = pygame.mask.from_surface(dodge_item_ball3)

    player_mask = pygame.mask.from_surface(current_sprite)

    for ball_rect, ball_mask in zip([ball1_rect, ball2_rect, ball3_rect], [ball_mask1, ball_mask2, ball_mask3]):
        offset = (ball_rect.x - current_sprite_rect.x, ball_rect.y - current_sprite_rect.y)
        if player_mask.overlap(ball_mask, offset):
            print("hit")
            return True#, boss_pose
            #no_hit = False
    
    if ball1_rect.centery >= target_ball1_y and ball2_rect.centery >= target_ball2_y and ball3_rect.centery >= target_ball3_y:
        return False#, boss_pose
        #no_finish = False

    #if no_hit and no_finish:
        #return None, boss_pose

def phase1_attack_2_fast_speers():
    global attack_start_time, attack_beginning, boss_pose
    global dodge_item_speer1, dodge_item_speer2, dodge_item_speer2_rect, dodge_item_speer1_rect
    global player_sprite_left, player_sprite_right, player_sprite_standing, player_sprite_up
    global player_sprite_left_rect, player_sprite_right_rect, player_sprite_standing_rect, player_sprite_up_rect
    global current_sprite
    dodge_speed = 50
    #global target_ball1_y, target_ball2_y, target_ball3_y
    if attack_beginning:
        attack_start_time = pygame.time.get_ticks()
        attack_beginning = False
        dodge_item_speer1_rect.center = (width//2 - 150, height//2 - 200)
        dodge_item_speer2_rect.center = (width//2 + 150, height//2 - 200)
        no_hit = True
        no_finish = True

    screen.blit(dodge_item_speer1, dodge_item_speer1_rect)
    screen.blit(dodge_item_speer2, dodge_item_speer2_rect)
    target_item1_x, target_item1_y = width//2 - 150,1080
    target_item2_x, target_item2_y = width//2 + 150,1080
    elapsed = pygame.time.get_ticks() - attack_start_time
    if elapsed >= 500:
        dodge_item_speer1_rect = move_dodge_item(dodge_item_speer1_rect, (target_item1_x, target_item1_y), dodge_speed)
        dodge_item_speer2_rect = move_dodge_item(dodge_item_speer2_rect, (target_item2_x, target_item2_y), dodge_speed)
    if elapsed >= 2300:
        boss_pose = "both down"
    item_mask1 = pygame.mask.from_surface(dodge_item_speer1)
    item_mask2 = pygame.mask.from_surface(dodge_item_speer2)

    player_mask = pygame.mask.from_surface(current_sprite)

    for item_rect, item_mask in zip([dodge_item_speer1_rect, dodge_item_speer2_rect], [item_mask1, item_mask2,]):
        offset = (item_rect.x - current_sprite_rect.x, item_rect.y - current_sprite_rect.y)
        if player_mask.overlap(item_mask, offset):
            print("hit")
            return True#, boss_pose
            #no_hit = False
    
    if dodge_item_speer1_rect.centery >= target_item1_y and dodge_item_speer2_rect.centery >= target_item2_y:
        return False#, boss_pose
        #no_finish = False

    #if no_hit and no_finish:
        #return None, boss_pose


pygame.init()
fps = 60
fpsClock = pygame.time.Clock()


icon = pygame.image.load("Oracle_of_pythmenia/imgs/icon.png")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Oracle of Pythmenia")


player_sprite_standing = pygame.transform.scale(pygame.image.load("Oracle_of_pythmenia/imgs/Explorer steht.png"),(525/4,882.6/4))
player_sprite_left = pygame.transform.scale(pygame.image.load("Oracle_of_pythmenia/imgs/Explorer links.png"),(525/3.6,764/3.6))
player_sprite_right = pygame.transform.scale(pygame.image.load("Oracle_of_pythmenia/imgs/Explorer rechts.png"),(525/3.6,765/3.6))
player_sprite_up =  pygame.transform.scale(pygame.image.load("Oracle_of_pythmenia/imgs/Explorer oben.png"),(561,867))
background_wall = pygame.transform.scale(pygame.image.load("Oracle_of_pythmenia/imgs/Background_Wall.png"),(16000,1024))
background_hall = pygame.transform.scale(pygame.image.load("Oracle_of_pythmenia/imgs/Background_Hall.png"),(1024,1024))
oracle_sprite_normal = pygame.transform.scale(pygame.image.load("Oracle_of_pythmenia/imgs/Orakel_transparent.png"),(300,300))
player_dialogue_box_texture = pygame.transform.scale(pygame.image.load("Oracle_of_pythmenia/imgs/player dialogue box.png"),(600,600))
oracle_dialogue_box_texture = pygame.transform.scale(pygame.image.load("Oracle_of_pythmenia/imgs/oracle_dialogue box.png"),(600,600))
background_bossfight = pygame.transform.scale(pygame.image.load("Oracle_of_pythmenia/imgs/background_bossfight.png"),(1920,1280))
bossfight_outline = pygame.transform.scale(pygame.image.load("Oracle_of_pythmenia/imgs/bossfight_outline.png"),(600,600))   
bossfight_raw_outline = pygame.transform.scale(pygame.image.load("Oracle_of_pythmenia/imgs/bossfight_raw_outline.png"),(600,600))
dodge_item_ball = pygame.transform.scale(pygame.image.load("Oracle_of_pythmenia/imgs/dodge_item_ball.png"),(100,100))
dodge_item_ball1 = pygame.transform.scale(pygame.image.load("Oracle_of_pythmenia/imgs/dodge_item_ball.png"),(100,100))
dodge_item_ball2 = pygame.transform.scale(pygame.image.load("Oracle_of_pythmenia/imgs/dodge_item_ball.png"),(100,100))
dodge_item_ball3 = pygame.transform.scale(pygame.image.load("Oracle_of_pythmenia/imgs/dodge_item_ball.png"),(100,100))
dodge_item_flash_alert_copy = pygame.transform.scale(pygame.image.load("Oracle_of_pythmenia/imgs/dodge_item_flash_alert.png"),(600,600))
dodge_item_flash = pygame.transform.scale(pygame.image.load("Oracle_of_pythmenia/imgs/dodge_item_flash.png"),(600,600))
dodge_item_speer = pygame.transform.scale(pygame.image.load("Oracle_of_pythmenia/imgs/dodge_item_speer.png"),(600,600))
dodge_item_speer1 = pygame.transform.scale(pygame.image.load("Oracle_of_pythmenia/imgs/dodge_item_speer.png"),(300,300))
dodge_item_speer2 = pygame.transform.scale(pygame.image.load("Oracle_of_pythmenia/imgs/dodge_item_speer.png"),(300,300))
oracle_both_down = pygame.transform.scale(pygame.image.load("Oracle_of_pythmenia/imgs/oracle_both_down.png"),(400,400))
oracle_left_down = pygame.transform.scale(pygame.image.load("Oracle_of_pythmenia/imgs/oracle_left_down.png"),(600,600))
oracle_right_down = pygame.transform.scale(pygame.image.load("Oracle_of_pythmenia/imgs/oracle_right_down.png"),(600,600))
oracle_true_form = pygame.transform.scale(pygame.image.load("Oracle_of_pythmenia/imgs/oracle_true_form.png"),(600,600))
damage_item = pygame.transform.scale(pygame.image.load("Oracle_of_pythmenia/imgs/damage_item.png"),(600,600))
potion_item = pygame.transform.scale(pygame.image.load("Oracle_of_pythmenia/imgs/potion_item.png"),(600,600))


player_sprite_standing_rect = player_sprite_standing.get_rect(); player_sprite_standing_rect.center = ((width/2, height-160))
player_sprite_left_rect = player_sprite_left.get_rect(); player_sprite_left_rect.center = ((width/2, height-160))
player_sprite_right_rect = player_sprite_right.get_rect(); player_sprite_right_rect.center = ((width/2, height-160))
player_sprite_up_rect = player_sprite_up.get_rect(); player_sprite_up_rect.center = ((width/2, height-160))
background_wall_rect = background_wall.get_rect(); background_wall_rect.bottomleft = (0, height)
background_hall_rect = background_hall.get_rect(); background_hall_rect.center = (width/2, height/2)
oracle_sprite_normal_rect = oracle_sprite_normal.get_rect(); oracle_sprite_normal_rect.center = (width/2, height/2)
player_dialogue_box_texture_rect = player_dialogue_box_texture.get_rect(); player_dialogue_box_texture_rect.center = (width/1.85, height-160)
oracle_dialogue_box_texture_rect = oracle_dialogue_box_texture.get_rect(); oracle_dialogue_box_texture_rect.center = (width/1.9, height/2 - 200)
background_bossfight_rect = background_bossfight.get_rect(); background_bossfight_rect.center = (width/2,height/2)
bossfight_outline_rect = bossfight_outline.get_rect(); bossfight_outline_rect.center = (width/2,height/2 + 250)
bossfight_raw_outline_rect = bossfight_raw_outline.get_rect(); bossfight_raw_outline_rect.center = (width/2,height/2 + 250)
dodge_item_ball_rect = dodge_item_ball.get_rect(); dodge_item_ball_rect.center = (0,0)
dodge_item_flash_alert_copy_rect = dodge_item_flash_alert_copy.get_rect(); dodge_item_flash_alert_copy_rect.center = (0,0)
dodge_item_flash_rect = dodge_item_flash.get_rect(); dodge_item_flash_rect.center = (0,0)
dodge_item_speer_rect = dodge_item_speer.get_rect(); dodge_item_speer_rect.center = (0,0)
oracle_both_down_rect = oracle_both_down.get_rect(); oracle_both_down_rect.center = (width/2,height/2 - 200)
oracle_left_down_rect = oracle_left_down.get_rect(); oracle_left_down_rect.center = (0,0)
oracle_right_down_rect = oracle_right_down.get_rect(); oracle_right_down_rect.center = (0,0)
oracle_true_form_rect = oracle_true_form.get_rect(); oracle_true_form_rect.center = (0,0)
ball1_rect = dodge_item_ball1.get_rect(); ball1_rect.center = (width//2 - 150, height//2 - 200)
ball2_rect = dodge_item_ball2.get_rect(); ball2_rect.center = (width//2 - 150, height//2 - 200)
ball3_rect = dodge_item_ball3.get_rect(); ball3_rect.center = (width//2 + 150, height//2 - 200)
dodge_item_speer1_rect = dodge_item_speer1.get_rect(); dodge_item_speer1_rect.center = (width//2 - 150, height//2 - 200)
dodge_item_speer2_rect = dodge_item_speer2.get_rect(); dodge_item_speer2_rect.center = (width//2 + 150, height//2 - 200)
damage_item_rect = damage_item.get_rect(); damage_item_rect.center = (0, 0)



font = pygame.font.Font("Oracle_of_pythmenia/font/VT323-Regular.ttf",25)
title_font = pygame.font.Font("Oracle_of_pythmenia/font/VT323-Regular.ttf",170)
middle_font = pygame.font.Font("Oracle_of_pythmenia/font/VT323-Regular.ttf",90)
boss_text1 = font.render("You were smarter than I thought,", True, (255,255,255))
boss_text2 = font.render("but can you fight?", True, (255,255,255))

boss_text1_rect = boss_text1.get_rect(center=(width/2,height/2 - 500))
boss_text2_rect = boss_text2.get_rect(center=(width/2,height/2 - 450))

death_screen_text = title_font.render("YOU DIED", True, (255,255,255))
death_option1_text = middle_font.render("Try again", True, (255,255,255))
death_option2_text = middle_font.render("Give up", True, (255,255,255))
selection_text = middle_font.render("^", True, (255,255,255))

death_screen_text_rect = death_screen_text.get_rect(center=(width/2,height/2 - 200))
death_option1_text_rect = death_option1_text.get_rect(center=(width/2 - 300,height/2 + 200))
death_option2_text_rect = death_option2_text.get_rect(center=(width/2 + 300,height/2 + 200))
selection_text_rect = selection_text.get_rect(center=(width/2 - 300,height/2 + 300))

wall_speed = 10
oracle_shown = False
oracle_start_time = None
bossfight_start_time = None
window_there = True
float_offset = 0 
float_speed = 0.05
float_amplitude = 10
running = True
current_sprite = player_sprite_standing
current_sprite_rect = player_sprite_standing_rect 
player_x = width // 2
player_y = height - 160
player_speed = 8
respawn = False
#also after death9
dead = None
bossfight_phase = 1
next_attack = True
boss_pose = "both up"
selec = "left"
attack_3_counter = 0
attack_start_time = None
attack_beginning = True
spawn_damage_item = False
damage_item_there = False

first_stage = False
second_stage = False
third_stage = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()



    if first_stage:
        screen.fill((70, 144, 184, 255))
        screen.blit(background_wall, background_wall_rect)

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            current_sprite = player_sprite_left
            current_sprite_rect = player_sprite_left_rect
            if background_wall_rect.x + wall_speed <= 0:
                background_wall_rect.x += wall_speed
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:  
            current_sprite = player_sprite_right
            current_sprite_rect = player_sprite_right_rect
            if background_wall_rect.x - wall_speed >= -(background_wall.get_width() - width):
                background_wall_rect.x -= wall_speed  
        else:  
            current_sprite = player_sprite_standing
            current_sprite_rect = player_sprite_standing_rect

        if background_wall_rect.x <= -13680:
            if keys[pygame.K_RETURN]:
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
                rect = surf.get_rect(midtop=(oracle_dialogue_box_texture_rect.centerx - 35, y1))
                screen.blit(surf, rect)
                y1 += font.get_height() + 5

            window.update()
            window.deiconify()
            entry.focus_set()

    elif third_stage:
        if window_there:
            window.destroy()
            window_there = False
        if dead == False or dead == None:
            screen.blit(background_bossfight, background_bossfight_rect)
            float_offset += float_speed
            oracle_both_down_rect.centery = (height/2 - 200) + math.sin(float_offset)*float_amplitude
            boss_text1_rect.centery = (height/2 - 470) + math.sin(float_offset)*float_amplitude
            boss_text2_rect.centery = (height/2 - 450) + math.sin(float_offset)*float_amplitude
            screen.blit(oracle_both_down, oracle_both_down_rect)
            screen.blit(bossfight_outline, bossfight_outline_rect)
            screen.blit(bossfight_raw_outline, bossfight_raw_outline_rect)
            player_sprite_standing = pygame.transform.scale(pygame.image.load("Oracle_of_pythmenia/imgs/Explorer steht.png"),(525/7.3,882.6/7.3))
            player_sprite_left = pygame.transform.scale(pygame.image.load("Oracle_of_pythmenia/imgs/Explorer links.png"),(525/6.5,764/6.5))
            player_sprite_right = pygame.transform.scale(pygame.image.load("Oracle_of_pythmenia/imgs/Explorer rechts.PNG"),(525/6.5,765/6.5))
            player_sprite_up =  pygame.transform.scale(pygame.image.load("Oracle_of_pythmenia/imgs/Explorer oben.png"),(561/7.3,867/7.3))

            player_sprite_standing_rect = player_sprite_standing.get_rect(); player_sprite_standing_rect.center = ((width/2, height-160))
            player_sprite_left_rect = player_sprite_left.get_rect(); player_sprite_left_rect.center = ((width/2, height-160))
            player_sprite_right_rect = player_sprite_right.get_rect(); player_sprite_right_rect.center = ((width/2, height-160))
            player_sprite_up_rect = player_sprite_up.get_rect(); player_sprite_up_rect.center = ((width/2, height-160))
            standing = True
            old_x, old_y = player_x, player_y
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                player_speed = 8
                current_sprite = player_sprite_left
                player_x -= player_speed
                last_coords = "-x"
                standing = False
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                player_speed = 8
                current_sprite = player_sprite_right
                player_x += player_speed 
                last_coords = "+x"
                standing = False
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                player_speed = 8
                current_sprite = player_sprite_up
                player_y -= player_speed
                last_coords = "-y"
                standing = False
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                player_speed = 4
                current_sprite = player_sprite_standing
                player_y += player_speed
                last_coords = "+y"
                standing = False
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                if keys[pygame.K_SPACE] or keys[pygame.K_LSHIFT]:
                    player_speed = 14
                    current_sprite = player_sprite_left
                    player_x -= player_speed
                    last_coords = "-x"
                    standing = False
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                if keys[pygame.K_SPACE] or keys[pygame.K_LSHIFT]:
                    player_speed = 14
                    current_sprite = player_sprite_right
                    player_x += player_speed 
                    last_coords = "+x"
                    standing = False
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                if keys[pygame.K_SPACE] or keys[pygame.K_LSHIFT]:
                    player_speed = 14
                    current_sprite = player_sprite_up
                    player_y -= player_speed
                    last_coords = "-y"
                    standing = False
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                if keys[pygame.K_SPACE] or keys[pygame.K_LSHIFT]:
                    player_speed = 14
                    current_sprite = player_sprite_standing
                player_y += player_speed
                last_coords = "+y"
                standing = False
            if standing:  
                current_sprite = player_sprite_standing

            current_sprite_rect = current_sprite.get_rect(); current_sprite_rect.center = (player_x, player_y)

            player_mask = pygame.mask.from_surface(current_sprite)
            outline_mask = pygame.mask.from_surface(bossfight_raw_outline)

            offset = (bossfight_raw_outline_rect.x - current_sprite_rect.x, bossfight_raw_outline_rect.y - current_sprite_rect.y)

            if player_mask.overlap(outline_mask, offset):
                player_x, player_y = old_x, old_y
                current_sprite_rect.center = (player_x, player_y)
                
            screen.blit(current_sprite, current_sprite_rect)
            if bossfight_start_time is None:
                bossfight_start_time = pygame.time.get_ticks()

            elapsed = pygame.time.get_ticks() - bossfight_start_time
            if elapsed <= 5000:
                screen.blit(boss_text1,boss_text1_rect)
                screen.blit(boss_text2,boss_text2_rect)
            if elapsed >= 5000:
                #phase1_attack_3_normal_fast_balls1()
                #print("test")
                if bossfight_phase == 1:
                    if next_attack == True:
                        rng_attacks = random.randint(1,3)
                        print(rng_attacks)
                        next_attack = False
                        attack_3_counter =+ 1
                        print(attack_3_counter)
                        if attack_3_counter == 3:
                            attack_3_counter = 0
                            spawn_damage_item = True
                    if rng_attacks == 1:
                        dead = phase1_attack_3_normal_fast_balls1()
                        #if dead:
                        #    time.sleep(1)
                    if rng_attacks == 2:
                        dead = phase1_attack_3_normal_fast_balls2()
                        #if dead:
                        #    time.sleep(1)
                    if rng_attacks == 3:
                        dead = phase1_attack_2_fast_speers()
                        if dead:
                            time.sleep(1)

                    if dead == False:
                        next_attack = True
                        attack_start_time = None
                        attack_beginning = True
                        dead = None
                        attack_3_counter = 0
                        print("next attack")
                #if bossfight_phase == 2:
                    #rng_attacks = random.randint(1,3) ...
                if spawn_damage_item:
                    randomx_in_outline = random.randint(734,1178)
                    randomy_in_outline = random.randint(609,973)
                    damage_item_rect = damage_item.get_rect(); damage_item_rect.center = (609, 973)
                    damage_item_there = True
                    spawn_damage_item = False    
                if damage_item_there:
                    screen.blit(damage_item, damage_item_rect)         
            if dead:
                screen.fill((0, 0, 0))
                screen.blit(death_screen_text, death_screen_text_rect)
                screen.blit(death_option1_text, death_option1_text_rect)
                screen.blit(death_option2_text, death_option2_text_rect)
                screen.blit(selection_text, selection_text_rect)

                
                if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    selection_text_rect = selection_text.get_rect(center=(width/2 - 300,height/2 + 300))
                    selec = "left"
                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    selection_text_rect = selection_text.get_rect(center=(width/2 + 300,height/2 + 300))
                    selec = "right"
                
                if keys[pygame.K_RETURN] and selec == "left":
                    #print("respawn")
                    attack_start_time = None
                    attack_beginning = True
                    bossfight_start_time = None
                    dead = None
                    bossfight_phase = 1
                    next_attack = True
                    boss_pose = "both up"
                    selec = "left"
                    elapsed = 0
                if keys[pygame.K_RETURN] and selec == "right":
                    pygame.quit()
                    sys.exit()
    #get_mousclick_coords()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
    pygame.display.flip()
    fpsClock.tick(fps)








