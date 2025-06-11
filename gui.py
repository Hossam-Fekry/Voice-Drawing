#importing the moudule
from customtkinter import *
import main

# settig up the gui
root = CTk()
root.geometry("364x446")
root.title("Voice Drawing")
root.resizable(False, False)
set_appearance_mode("light")
set_default_color_theme("dark-blue")

#make the variables
Filling_color_d = StringVar()
Pen_color_d = StringVar()
Pen_icon_d = StringVar()
pen_hide = BooleanVar()

# make the title
CTkLabel(root, text="Please choose your preferences", font=("Arial", 20,"bold")).pack(pady=20)
# make the function to be called when the option is selected

def on_filling_color_selected(value):
    global Filling_color_d
    Filling_color_d = Filling_color.get()
    print("Filling color selected:", Filling_color_d)

def on_pen_color_selected(value):
    global Pen_color_d
    Pen_color_d = pen_color.get()
    print("pen color selected:", Pen_color_d)

def on_pen_icon_selected(value):
    global pen_icon_d
    pen_icon_d = pen_icon.get()
    print("pen icon selected:", pen_icon_d)

def start_app():
    global Filling_color_d, Pen_color_d, pen_icon_d, pen_hide
    Filling_color_d = Filling_color.get()
    Pen_color_d = pen_color.get()
    pen_icon_d = pen_icon.get()
    pen_hide = pen_hide.get()
    main.code(Filling_color_d, Pen_color_d, pen_icon_d, pen_hide)  # Call the code function with the selected values

# make the settings and labels

#make the Filling Setting

CTkLabel(root, text="Filling Color", font=("Arial", 15,"bold"), text_color="#444444").place(x=20, y=100)
Filling_color = CTkOptionMenu(root, values=["Red", "Green", "Blue", "Yellow", "Black"], command=on_filling_color_selected)
Filling_color.set("Select Here")  # Set default value
Filling_color.place(x=150, y=100)

#make the Pen color Setting

CTkLabel(root, text="Pen Color", font=("Arial", 15,"bold")).place(x=20, y=150)
pen_color = CTkOptionMenu(root, values=["Red", "Green", "Blue", "Yellow", "Black"], command=on_pen_color_selected)
pen_color.set("Select Here")  # Set default value
pen_color.place(x=150, y=150)

#make the  Setting

CTkLabel(root, text="pen icon", font=("Arial", 15,"bold")).place(x=20, y=200)
pen_icon = CTkOptionMenu(root, values=["arrow", "turtle", "classic"], command=on_pen_icon_selected)
pen_icon.set("Select Here")  # Set default value
pen_icon.place(x=150, y=200)


# make the hide pen switch
CTkLabel(root, text="hide the pen", font=("Arial", 15,"bold")).place(x=20, y=250)

# Create the hiding switch


pen_hide = CTkSwitch(
    master=root,
    text=" ",
    variable=pen_hide,
)
pen_hide.place(x=150, y=250)

Start_b = CTkButton(root, text="Start the App",command=start_app, fg_color="#4CAF50", hover_color="#3e8e41", font=("Arial", 15, "bold"),corner_radius=25)
Start_b.place(x=120, y=350)
root.mainloop()