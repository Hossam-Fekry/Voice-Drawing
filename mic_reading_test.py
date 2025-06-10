import speech_recognition as sr
import sys

# Ensure console can print UTF-8
sys.stdout.reconfigure(encoding='utf-8')

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak something:")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio, language="ar-EG")
    print("Speech recognized:")
    print(text)
except sr.UnknownValueError:
    print("Could not understand the audio")
except sr.RequestError:
    print("Connection error with Google Speech Recognition service")
