from googletrans import Translator
from googletrans import LANGUAGES
import random

translator = Translator()

user_text = input("What do you want to translate? ")
number = int(input("How many times do you want to translate it? "))
language_codes = list(LANGUAGES.keys())

for _ in range(number):
    random = random.randint(1, len(language_codes))
    random_language = language_codes[random - 1]
    detected_lang = translator.detect(user_text).lang
    user_text = translator.translate(user_text, src=detected_lang, dest=random_language).text

result = translator.translate("Hello, how are you?", src="en", dest=random_language)



print(f"Translated text: {result.text}")