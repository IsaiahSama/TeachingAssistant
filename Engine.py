"""File responsible for handling the text to speech engine"""

import pyttsx3
import pyglet
from gtts import gTTS
from os import path, remove
from time import sleep

FEMALE_VOICE = 1
MALE_VOICE = 0

class Engine:
    """Class responsible for the setup and handling of the Text To Speech
    
    Attrs:
        messages (list): List of messages to be read
        rate (int): The speaking rate of the tts
        voice (int): The type of voice for the tts. 0 for MALE_VOICE, 1 for FEMALE_VOICE
        filename (str): The name of the temporary file
    Methods:
        setup_engine(): Used to setup the Text To Speech.
        say_and_print(*args): Prints a message to the screen, and says it as well.
        speak(message:str): Stores messages to be output in a queue.
        speak_female_voice(message:str): Uses gTTS to speak in a female voice."""

    messages = []

    def __init__(self) -> None:
        self.rate = 120
        self.voice = MALE_VOICE
        self.filename = "output.mp3"

    def setup_engine(self):
        """Sets up the pyttsx3 engine for usage.
        
        Returns the engine"""
        engine = pyttsx3.init()
        
        voices = engine.getProperty('voices')
        engine.setProperty('rate', self.rate)
        engine.setProperty('voice',voices[self.voice].id)
        engine.setProperty('volume', 1.0)

        return engine        

    def say_and_print(self, message:str):
        """Used to display a message to the screen, and read it out loud as well.
        
        Args:
            message (str): The message to be displayed and read."""

        print("ENGINE.PY:", message)
        self.speak(message)

    def speak_female_voice(self, message:str):
        """Used to speak using the female voice from gTTs instead of from Pyttsx3
        
        Args:
            message (str): The message to be read"""
        
        tts = gTTS(message, lang='en')
        tts.save(self.filename)
        speech = pyglet.media.load(self.filename, streaming=False)
        speech.play()

        sleep(speech.duration)
        if path.exists(self.filename): remove(self.filename)

    def speak(self, message:str):
        """Reads a message from the queue
        
        Args:
            message (str): The message to be read."""
        if self.voice == FEMALE_VOICE: self.speak_female_voice(message)
        else:
            engine = self.setup_engine()
            engine.say(message)
            engine.runAndWait()
            engine.stop()