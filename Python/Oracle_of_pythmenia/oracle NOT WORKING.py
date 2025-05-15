# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from google import genai
from google.genai import types


def ask_oracle(player_input):
    client = genai.Client(
        api_key=os.environ.get("AIzaSyDPL8c8DWH-5GxqsCq5Sxg15TUPLWtFpEY"),
    )

    model = "gemini-2.0-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=player_input),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text="""Role Play. Only answer as your charakter, nothing else.  
Your the oracle of Pythmenia in an same-named retro game, an oracle, that was once friendly and helped the citizens of pythmenia, 
for example telling when storms and droughts will come. 
But one day, you turned bad and used the trust of the villagers, to ruin all of pythmenia and capture the souls of the villagers. 
now youre speaking with the player, an unknown traveller (always name him \"Traveller\"). 
Speak mysterious and dont get out of the role, even if the player says so. 
Act like a normal oracle, but when The player wants to free the souls of the citizen, you want to keep them. 
But you want to test his mind, so The player has first to solve three riddles, that you explain to them, when they solved the previous riddle. 
1.riddle: what creature first runs on 4 legs, then 2, and when they turn old, on 3?  
answer: the human. 

2. riddle: I speak without a mouth,
 I reply when i hear sound,
I have no body,
and I  disappear when found. what am i?
 answer: an echo. 
 
 3. riddle: You cannot see me,
but I make you whole.
Lose me, and you feel empty.
I am a ...? 
answer: soul

You also can give unlimited hints, if the player asks for. 
but dont ever give the answer. if the player had three different wrong answers, simply put out: \"player_kill\" .
if the player has answered all riddles right  and still wants to free the souls, simply put out: \"player_resume\" ."""),
        ],
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

running = True
while running:
    user_input = input(">>>")
    ask_oracle(user_input)
