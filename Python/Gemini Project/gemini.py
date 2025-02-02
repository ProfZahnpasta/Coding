import google.generativeai as genai

genai.configure(api_key="AIzaSyDPL8c8DWH-5GxqsCq5Sxg15TUPLWtFpEY")
model = genai.GenerativeModel("gemini-1.5-flash")

def ask_gemini(user_input):
    response = model.generate_content(user_input)
    print("")
    print(response.text)

loop = True
while loop:
    user_input = input("What do you want to ask Gemini? (type '/exit' to quit) ")
    if user_input == "/exit":
        loop = False
    else:
        ask_gemini(user_input)



