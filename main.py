# Importing modules
import speech_recognition as sr
import sys
from turtle import *
def code(Filling_color_d, Pen_color_d, pen_icon_d, pen_hide, background_color_d, drawing_speed_d, pen_thickness_d):
    print(Filling_color_d, Pen_color_d, pen_icon_d, pen_hide, background_color_d, drawing_speed_d, pen_thickness_d)
    
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

    title("Voice Drawing")
    # The dictionary
    Shapes = {
        "مربع": "Square",
        "مستطيل": "Rectangle",
        "مثلث": "Triangle",
        "دائره": "Circle"
    }

    # Shape functions
    def Triangle():
        clear()
        begin_fill()
        for i in range(3):
            forward(100)
            left(120)
        end_fill()

    def Square():
        clear()
        begin_fill()
        for i in range(4):
            forward(100)
            left(90)
        end_fill()

    def Rectangle():
        clear()
        begin_fill()
        for i in range(2):
            forward(100)
            left(90)
            forward(200)
            left(90)
        end_fill()

    def Circle():
        clear()
        begin_fill()
        circle(100)
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
            else:
                print("Unknown Shape")

    except sr.UnknownValueError:
        print("Could not understand the audio")
    except sr.RequestError:
        print("Connection error with Google Speech Recognition service")

    # ✅ Keep turtle window open
    done()
