"""File which will contain helper functions"""

from typing import Callable
from pyinputplus import inputMenu, inputYesNo
from threading import Thread

import Typer
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

def repeat_line(reader:Reader.Reader):
    """Used to tell the reader to repeat a line with a 5 second delay
    
    Args:
        reader (Reader.Reader): The reader object to be acted upon"""

    reader.repeat_line = True
    Print("Repeating current line")


def toggle_pause(obj: Reader.Reader | Typer.Typer):
    """Used to toggle the pause of an object."""
    obj.paused = not obj.paused
    Print(str(obj), "has been", "paused" if obj.paused else "unpaused")
    return None

def toggle_reader_pause(reader:Reader.Reader):
    """Used to toggle the pause state of a Reader object
    
    Args:
        reader (Reader.Reader): The reader to be acted upon"""
    toggle_pause(reader)

def toggle_typer_pause(typer:Typer.Typer):
    """Used to toggle the pause state of a Typer object
    
    Args:
        typer (Typer.Typer): The typer to be acted upon"""
    toggle_pause(typer)

def obj_shut_down(obj:Typer.Typer | Reader.Reader):
    """Used to set an objects running state to False.
    
    Args:
        obj (Typer.Typer | Reader.Reader): The object with a running attribute to be set to false"""
    
    obj.running = False
    Print(str(obj), "has been stopped.")


def typer_shut_down(typer:Typer.Typer):
    """Used to stop the current typer from typing.
    
    Args:
        typer (Typer.Typer): The typer to stop"""
    obj_shut_down(typer)

def reader_shut_down(reader:Reader.Reader):
    """Used to stop the current reader from reading
    
    Args:
        reader (Reader.Reader): The reader to stop"""
    obj_shut_down(reader)