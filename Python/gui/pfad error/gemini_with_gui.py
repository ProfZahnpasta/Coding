import tkinter
import customtkinter
import google.generativeai as genai

genai.configure(api_key="AIzaSyDPL8c8DWH-5GxqsCq5Sxg15TUPLWtFpEY")
model = genai.GenerativeModel("gemini-1.5-flash")

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

def ask_gemini(event=None):
    user_input = entry.get()
    response = model.generate_content(user_input)
    result_label.configure(text=response.text)

def on_mouse_wheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

window = customtkinter.CTk()
window.geometry("755x255")
window.title("Gemini")
window.resizable(False, True)

canvas = tkinter.Canvas(window, bg="lightgray")
scrollbar = tkinter.Scrollbar(window, orient="vertical", command=canvas.yview)
scrollable_frame = customtkinter.CTkFrame(canvas, bg_color="lightgray")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind_all("<MouseWheel>", on_mouse_wheel)

title = customtkinter.CTkLabel(scrollable_frame, text="Gemini Chat", width=720, height=50, font=("monospace", 30, 'bold'))
title.pack(padx=10, pady=10)

entry = customtkinter.CTkEntry(scrollable_frame, font=("monospace", 20, 'bold'), width=400, height=30)
entry.pack(pady=20)
entry.bind("<Return>", ask_gemini)

done_button = customtkinter.CTkButton(scrollable_frame, text="Done", command=ask_gemini, font=("monospace", 30, 'bold'))
done_button.pack()

result_label = customtkinter.CTkLabel(scrollable_frame, text="", font=("monospace", 20, 'bold'), wraplength=680)
result_label.pack(pady=20)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

window.mainloop()