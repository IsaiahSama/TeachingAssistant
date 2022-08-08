"""File which will contain helper functions"""

from typing import Callable
from pyinputplus import inputMenu, inputYesNo, inputChoice, inputInt
from threading import Thread
from tkinter import Tk, filedialog

import Engine

engine = Engine.Engine()

def Print(*message):
    """Modifies the output for print statements"""
    
    print("HELPER.PY:", *message)

def is_num(val:str):
    """Used to check whether a given value is a floating point number.
    
    Args:
        val (str): The value to check"""
    try:
        val = float(val)
    except ValueError:
        Print(val, "is not a number.")
        return False
    return True

def get_file() -> str:
        """Method used to get a given file using a gui
        
        Returns:
            str - The filename"""
        root = Tk()

        filename = filedialog.askopenfilename(initialdir="Files/", title="Select Your File", filetypes=(("Text", "*.txt"),))
        root.destroy()

        return filename

def load_script():
        filename = get_file()
        if not filename: raise Exception("No filename was provided!")

        with open(filename) as fp:
            lines= fp.readlines()

        if not lines:
            raise Exception ("Script file was empty!")
        return lines

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

def prompt_for_menu(prompt, options:dict):
    """Allows the user to select an option from a given menu.
    
    Args:
        prompt (str): The prompt to be displayed to the screen
        options (dict): A dictionary matching each choice to their callback function value.
        
    Returns:
        str - The chosen key"""

    Print("Select the number of the choice you want to do.")
    return inputMenu(list(options.keys()), prompt, numbered=True)

def prompt_for_choice(prompt, options:list):
    """Allows the user to select an option from a given list:
    
    Args:
        prompt (str): The prompt to be displayed to the screen.
        options (list): The list of valid options
        
    Returns:
        str - The item tat was chosen"""

    print("Select your option from below.")
    return inputChoice(options, prompt)

def prompt_for_yes_no():
    """Prompts the user for a yes or no response."""

    return inputYesNo()

def prompt_for_int(prompt:str, min=-10, max=10) -> int:
    """Prompts the user to enter a number
    
    Args:
        prompt(str): Message to be the prompt for the user
        min (int): The minimum number that can be entered. Defaults to -10
        max (int): The maximum number that can be entered. Defaults to 10
        
    Returns:
        int"""

    return inputInt(prompt, 5, min=min, max=max)

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

def repeat_line(reader):
    """Used to tell the reader to repeat a line with a 5 second delay
    
    Args:
        reader (Reader.Reader): The reader object to be acted upon"""

    reader.repeat_line = True
    Print("Repeating current line")


def toggle_pause(obj):
    """Used to toggle the pause of an object."""
    obj.paused = not obj.paused
    Print(str(obj), "has been", "paused" if obj.paused else "unpaused")
    return None

def toggle_reader_pause(reader):
    """Used to toggle the pause state of a Reader object
    
    Args:
        reader (Reader.Reader): The reader to be acted upon"""
    toggle_pause(reader)

def toggle_typer_pause(typer):
    """Used to toggle the pause state of a Typer object
    
    Args:
        typer (Typer.Typer): The typer to be acted upon"""
    toggle_pause(typer)

def obj_shut_down(obj):
    """Used to set an objects running state to False.
    
    Args:
        obj (Typer.Typer | Reader.Reader): The object with a running attribute to be set to false"""
    
    obj.running = False
    Print(str(obj), "has been stopped.")


def typer_shut_down(typer):
    """Used to stop the current typer from typing.
    
    Args:
        typer (Typer.Typer): The typer to stop"""
    obj_shut_down(typer)

def reader_shut_down(reader):
    """Used to stop the current reader from reading
    
    Args:
        reader (Reader.Reader): The reader to stop"""
    obj_shut_down(reader)