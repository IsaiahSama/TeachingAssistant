"""File which will contain helper functions"""

from typing import Callable
from pyinputplus import inputMenu, inputYesNo
from threading import Thread

import Reader
import Engine
import keyboard

engine = Engine.Engine()

def Print(*message):
    """Modifies the output for print statements"""
    
    print("HELPER.PY:", *message)

def say_and_print_message(message:str):
    """Used to say and display a message to the screen
    
    Args:
        message (str): The message to be said and displayed"""
    engine.say_and_print(message)

def say_message(message:str):
    """Used to say a message using tts
    
    Args:
        message (str): The message to be spoken outloud"""

    engine.speak(message)

def prompt_for_choice(prompt, options:dict):
    """Allows the user to select an option from a given choice set.
    
    Args:
        prompt (str): The prompt to be displayed to the screen
        options (dict): A dictionary matching each choice to their value
        
    Returns:
        str - The chosen key"""

    Print("Select the number of the choice you want to do.")
    return inputMenu(list(options.keys()), prompt, numbered=True)

def prompt_for_yes_no():
    """Prompts the user for a yes or no response."""

    return inputYesNo()

def enter_to_continue(prompt="Press Enter to continue\n"):
    """Function that prompts the user to press enter to continue.
    
    Args:
        prompt (str): An option display message. Defaults to 'Press enter to continue'"""

    input(prompt)

def create_thread(func:Callable, daemon=True, args=tuple()):
    """Creates a threaded function and returns the thread object
    
    Args:
        func (function): The function to be threaded
        daemon (bool): Whether the thread should be daemon or not
        
    Returns:
        Thread - The threaded function"""
    
    thread = Thread(target=func, args=args, daemon=daemon)
    thread.start()
    return thread

def ask_and_quit():
    """Used to exit from the program after a prompt"""

    input("Press enter to exit\n")
    raise SystemExit

def toggle_pause(reader:Reader.Reader):
    """Used to toggle the pause state of a Reader object
    
    Args:
        reader (Reader.Reader): The reader to be acted upon"""
    reader.pause = not reader.pause
    Print("Reader has been", "paused" if reader.pause else "unpaused")
    return None