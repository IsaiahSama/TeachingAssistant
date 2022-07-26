"""File responsible for handling the text to speech engine"""

import pyttsx3

FEMALE_VOICE = 1
MALE_VOICE = 0

class Engine:
    """Class responsible for the setup and handling of the Text To Speech
    
    Attrs:
        messages (list): List of messages to be read
    Methods:
        setup_engine(): Used to setup the Text To Speech.
        say_and_print(*args): Prints a message to the screen, and says it as well.
        speak(message:str): Stores messages to be output in a queue."""

    messages = []

    def __init__(self) -> None:
        pass

    def setup_engine(self):
        """Sets up the pyttsx3 engine for usage.
        
        Returns the engine"""
        engine = pyttsx3.init()
        
        voices = engine.getProperty('voices')
        engine.setProperty('rate', 200)
        engine.setProperty('voice',voices[MALE_VOICE].id)
        engine.setProperty('volume', 1.0)

        return engine        

    def say_and_print(self, message:str):
        """Used to display a message to the screen, and read it out loud as well.
        
        Args:
            message (str): The message to be displayed and read."""

        print(message)
        self.speak(message)

    def speak(self, message:str):
        """Reads a message from the queue
        
        Args:
            message (str): The message to be read."""

        engine = self.setup_engine()
        engine.say(message)
        engine.runAndWait()
        engine.stop()