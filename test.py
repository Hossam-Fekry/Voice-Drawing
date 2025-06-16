import customtkinter as ctk
from tkinter import messagebox

app = ctk.CTk()
app.geometry("300x200")

def show_box():
    response = messagebox.askyesno("Confirm", "Do you want to continue?")
    if response:
        print("User clicked Yes")
    else:
        print("User clicked No")

btn = ctk.CTkButton(app, text="Show Message", command=show_box)
btn.pack(pady=40)

app.mainloop()
