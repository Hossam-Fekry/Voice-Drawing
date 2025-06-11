import customtkinter as ctk

# Initialize the customtkinter theme
ctk.set_appearance_mode("light")  # or "dark"
ctk.set_default_color_theme("blue")  # themes: blue, green, dark-blue

# Create the main window
root = ctk.CTk()
root.title("Toggle Switch Example")
root.geometry("300x150")

# Define a callback function for the switch
def switch_callback():
    if switch_var.get():
        print("Switch is ON")
    else:
        print("Switch is OFF")

# Create a variable to track the switch state
switch_var = ctk.BooleanVar(value=False)

# Create the CTkSwitch
switch = ctk.CTkSwitch(
    master=root,
    text="Hide the pen",
    variable=switch_var,
    command=switch_callback
)
switch.pack(pady=30)

# Run the app
root.mainloop()
    