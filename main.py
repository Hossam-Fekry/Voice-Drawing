# Importing modules
import speech_recognition as sr
import sys
from turtle import *
def code(Filling_color_d, Pen_color_d, pen_icon_d, pen_hide, background_color_d, drawing_speed_d, pen_thickness_d, side_l):
    print(Filling_color_d, Pen_color_d, pen_icon_d, pen_hide, background_color_d, drawing_speed_d, pen_thickness_d, side_l)
    def clear0():
        clear()
    # Set the user settings
    fillcolor(Filling_color_d)
    pencolor(Pen_color_d)
    shape(pen_icon_d)
    if pen_hide:
        hideturtle()
    else:
        showturtle()
    bgcolor(background_color_d)
    speed(drawing_speed_d.lower())
    pensize(pen_thickness_d)
    side = side_l

    title("Voice Drawing")
    # The dictionary
    Shapes = {
        "مربع": "Square",
        "مستطيل": "Rectangle",
        "مثلث": "Triangle",
        "دائره": "Circle",
        "خماسي الاضلاع": "Pentagon",
        "سداسي الاضلاع": "Hexagon",
        "سباعي الاضلاع": "Heptagon",
        "ثماني الاضلاع": "Octagon",
        "نجمه": "Star",
        "قلب": "Heart",
}

    # Shape functions
    def Triangle():
        clear()
        begin_fill()
        for i in range(3):
            forward(side)
            left(120)
        end_fill()

    def Square():
        clear()
        begin_fill()
        for i in range(4):
            forward(side)
            left(90)
        end_fill()

    def Rectangle():
        clear()
        begin_fill()
        for i in range(2):
            forward(side)
            left(90)
            forward(side / 2)
            left(90)
        end_fill()

    def Circle():
        clear()
        begin_fill()
        circle(side)
        end_fill()
    
    def Pentagon():
        clear()
        begin_fill()
        for i in range(5):
            forward(side)
            left(72)
        end_fill()
    
    def Hexagon():
        clear()
        begin_fill()
        for i in range(6):
            forward(side)
            left(60)
        end_fill()
    
    def Heptagon():
        clear()
        begin_fill()
        for i in range(7):
            forward(side)
            left(51.43)
        end_fill()
    
    def Octagon():
        clear()
        begin_fill()
        for i in range(8):
            forward(side)
            left(45)
        end_fill()
    
    def Star():
        clear()
        begin_fill()
        for i in range(5):
            forward(side)
            left(144)
        end_fill()
    
    def Heart():
        clear()
        begin_fill()
        left(140)
        forward(113)
        circle(-57, 200)
        left(120)
        circle(-57, 200)
        forward(113)
        end_fill()
    # Setup for speech recognition
    sys.stdout.reconfigure(encoding='utf-8')
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak something:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="ar-EG")
        print("Speech recognized:")

        if text in Shapes:
            print("The Shape is: " + Shapes[text])
            if Shapes[text] == "Square":
                Square()
            elif Shapes[text] == "Rectangle":
                Rectangle()
            elif Shapes[text] == "Triangle":
                Triangle()
            elif Shapes[text] == "Circle":
                Circle()
            elif Shapes[text] == "Pentagon":
                Pentagon()
            elif Shapes[text] == "Hexagon":
                Hexagon()
            elif Shapes[text] == "Heptagon":
                Heptagon()
            elif Shapes[text] == "Octagon":
                Octagon()
            elif Shapes[text] == "Star":
                Star()
            elif Shapes[text] == "Heart":
                Heart()
            else:
                print("Unknown Shape")

    except sr.UnknownValueError:
        print("Could not understand the audio")
    except sr.RequestError:
        print("Connection error with Google Speech Recognition service")

    # ✅ Keep turtle window open
    done()
