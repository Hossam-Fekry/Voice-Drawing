# importing the module
from customtkinter import *
import main
from PIL import Image, ImageTk
import tkinter as tk

# setting up the GUI
root = CTk()
root.geometry("364x546")
root.title("Voice Drawing")
set_appearance_mode("light")
set_default_color_theme("dark-blue")
root.iconbitmap("icon.ico")

# make the variables
Filling_color_d = StringVar()
Pen_color_d = StringVar()
Pen_icon_d = StringVar()
pen_thickness_d = IntVar()
area_of_shape_d = IntVar()
background_color_d = StringVar()
drawing_speed_d = StringVar()
side_l = IntVar()
pen_hide_d = BooleanVar()

# make the title
CTkLabel(root, text="Please choose your preferences", font=("Arial", 20, "bold")).pack(pady=20)

# functions called when selecting options
def on_filling_color_selected(value):
    print("Filling color selected:", value)

def on_pen_color_selected(value):
    print("Pen color selected:", value)

def on_pen_icon_selected(value):
    print("Pen icon selected:", value)

def on_pen_thickness_selected(value):
    print("Pen thickness selected:", value)

def on_background_color_selected(value):
    print("Background color selected:", value)

def on_drawing_speed_selected(value):
    print("Drawing speed selected:", value)

# function called when the Start button is clicked
def start_app():
    Filling_color_val = Filling_color.get().lower()
    Pen_color_val = pen_color.get().lower()
    pen_icon_val = pen_icon.get()
    pen_hide_val = pen_hide_d.get()
    background_color_val = background_color.get().lower()
    drawing_speed_val = drawing_speed.get().lower()
    pen_thickness_val = int(pen_thickness.get())
    side_length_val = int(side_l.get())

    # Print selected values (for debugging)
    print("Selected Values:")
    print("Filling color:", Filling_color_val)
    print("Pen color:", Pen_color_val)
    print("Pen icon:", pen_icon_val)
    print("Hide pen:", pen_hide_val)
    print("Background color:", background_color_val)
    print("Drawing speed:", drawing_speed_val)
    print("Pen thickness:", pen_thickness_val)
    print("Side length:", side_length_val)

    # Call main logic
    main.code(Filling_color_val, Pen_color_val, pen_icon_val, pen_hide_val, background_color_val, drawing_speed_val, int(pen_thickness_val), side_length_val)

# GUI widgets:

# Filling Color
CTkLabel(root, text="Filling Color", font=("Arial", 15, "bold"), text_color="#444444").place(x=20, y=100)
Filling_color = CTkOptionMenu(root, values=["Red", "Green", "Blue", "Yellow", "Black"], command=on_filling_color_selected)
Filling_color.set("Select Here")
Filling_color.place(x=150, y=100)

# Pen Color
CTkLabel(root, text="Pen Color", font=("Arial", 15, "bold")).place(x=20, y=150)
pen_color = CTkOptionMenu(root, values=["Red", "Green", "Blue", "Yellow", "Black"], command=on_pen_color_selected)
pen_color.set("Select Here")
pen_color.place(x=150, y=150)

# Pen Icon
CTkLabel(root, text="Pen Icon", font=("Arial", 15, "bold")).place(x=20, y=200)
pen_icon = CTkOptionMenu(root, values=["arrow", "turtle", "classic"], command=on_pen_icon_selected)
pen_icon.set("Select Here")
pen_icon.place(x=150, y=200)

# Pen Thickness
CTkLabel(root, text="Pen Thickness", font=("Arial", 15, "bold")).place(x=20, y=250)
pen_thickness = CTkOptionMenu(root, values=["1", "3", "5", "8", "10"], command=on_pen_thickness_selected)
pen_thickness.set("Select Here")
pen_thickness.place(x=150, y=250)

# Background Color
CTkLabel(root, text="Background Color", font=("Arial", 15, "bold")).place(x=20, y=300)
background_color = CTkOptionMenu(root, values=["Red", "Green", "Blue", "Yellow", "Black"], command=on_background_color_selected)
background_color.set("Select Here")
background_color.place(x=150, y=300)

# Drawing Speed
CTkLabel(root, text="Drawing Speed", font=("Arial", 15, "bold")).place(x=20, y=350)
drawing_speed = CTkOptionMenu(root, values=["Slow", "normal", "fast"], command=on_drawing_speed_selected)
drawing_speed.set("Select Here")
drawing_speed.place(x=150, y=350)

CTkLabel(root, text="Side length", font=("Arial", 20, "bold"), text_color="#444444").place(x=20, y=400)
side_l = CTkEntry(root, textvariable=area_of_shape_d, width=100, font=("Arial", 15, "bold"))
side_l.place(x=150, y=400)

# Hide Pen Switch
CTkLabel(root, text="Hide the Pen", font=("Arial", 15, "bold")).place(x=20, y=450)
pen_hide = CTkSwitch(master=root, text=" ", variable=pen_hide_d)
pen_hide.place(x=150, y=450)

# Start Button
Start_b = CTkButton(root, text="Start the App", command=start_app, fg_color="#4CAF50", hover_color="#3e8e41", font=("Arial", 15, "bold"), corner_radius=25)
Start_b.place(x=20, y=500)

Start_b = CTkButton(root, text="Clear Drawings", command=main.clear, fg_color="#FF0000", hover_color="#850000", font=("Arial", 15, "bold"), corner_radius=25)
Start_b.place(x=210, y=500)

# Main Loop
root.mainloop()
