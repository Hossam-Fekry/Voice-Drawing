# Voice-Drawing

Voice-Drawing is a Python application that listens to your voice (in Arabic) and draws the shape you say using the Turtle graphics library.

## Features

- 🎤 Recognizes spoken Arabic words for shapes
- 🟦 Draws Square, Rectangle, Triangle, or Circle based on your command
- 🐢 Uses Python's Turtle graphics for drawing
- 🗣️ Utilizes Google Speech Recognition for accurate voice input

## Supported Shapes

| Arabic   | English   |
|----------|-----------|
| مربع     | Square    |
| مستطيل   | Rectangle |
| مثلث     | Triangle  |
| دائره    | Circle    |

## Requirements

- Python 3.x
- [speech_recognition](https://pypi.org/project/SpeechRecognition/)
- [PyAudio](https://pypi.org/project/PyAudio/) (for microphone input)
- [turtle](https://docs.python.org/3/library/turtle.html) (usually included with Python)


## File Structure

- `main.py`: it has all the tuetle and lesting code we use it as a module to use it in the gui file
- `mic_reading_test.py`: a file to test the microphone
- `gui`: is the file where we wrot the gui code with custom tkinter
- `test`: we use it to test the code
- `README.md`: there we use markdown for documintation

## Installation

1. Clone this repository or download the source files.
2. Install the required packages:
   ```sh
   pip install SpeechRecognition PyAudio
   ```

## Usage

1. Run the main application:
   ```sh
   python main.py
   ```
2. Speak the name of a shape in Arabic (e.g., "مربع", "مستطيل", "مثلث", "دائره").
3. The corresponding shape will be drawn in a Turtle graphics window.

## Testing Microphone

To test if your microphone and speech recognition are working, run:
```sh
python mic_reading_test.py
```

## Notes

- Make sure your microphone is connected and working.
- An internet connection is required for Google Speech Recognition.

## License

This project is for educational purposes.