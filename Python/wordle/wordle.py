import random
import enchant
import google.generativeai as genai

genai.configure(api_key="AIzaSyDPL8c8DWH-5GxqsCq5Sxg15TUPLWtFpEY")
model = genai.GenerativeModel("gemini-1.5-flash")


language = str(input("In which language should the word be in: "))

target_word = model.generate_content(f"Only answer in one word. Give a 5-letter random word in the language {language}").text
lan_code = model.generate_content(f"Only answer the code. Put out the code for {language} (in this format: e.g. de_DE, fr_FR, en_GB, en_US)").text
if lan_code == '```\nde_DE\n```\n':
    dictionary = enchant.request_pwl_dict("200german_words.txt")
else: 
    dictionary = enchant.Dict(lan_code)

print(lan_code, target_word)

tries = int(input("Enter in how many tries you want to guess the word: "))

for i in range(tries):
    guess = str(input("Whats your guess? (Five Letters, no numbers, no spaces, only alphabetical letters, the word has to exist): "))
    if not len(guess) == 5:
        print("Your word must be 5 letters long.")
        continue
    elif not guess.find(" ") == -1:
        print("Your word must not contain spaces.")
        continue
    elif not guess.isalpha():
        print("Your word must consist of alphabetical letters.")
        continue
    elif not dictionary.check(guess):
        print("The word doesn't exist.")
        continue