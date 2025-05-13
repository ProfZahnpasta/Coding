import customtkinter as ctk

ctk.set_appearance_mode("dark")  # optional
ctk.set_default_color_theme("blue")  # optional

root = ctk.CTk()
root.overrideredirect(True)  # removes window borders

entry = ctk.CTkEntry(root, width=200, height=30)
entry.pack(padx=10, pady=10)

root.mainloop()
