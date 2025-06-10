# Importing modules
import speech_recognition as sr
import sys
from turtle import *
# The dictionary
Shapes = {
    "مربع": "Square",
    "مستطيل": "Rectangle",
    "مثلث": "Triangle",
    "دائره": "Circle"
}

# Shape functions
def Triangle():
    hideturtle()
    for i in range(3):
        forward(100)
        left(120)

def Square():
    hideturtle()
    for i in range(4):
        forward(100)
        left(90)

def Rectangle():
    hideturtle()
    for i in range(2):
        forward(100)
        left(90)
        forward(200)
        left(90)

def Circle():
    hideturtle()
    circle(100)

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
