"""File which will contain helper functions"""

from pyinputplus import inputMenu, inputYesNo
from threading import Thread
from ScriptReading import Engine

engine = Engine.Engine()

def Print(message:str):
    """Modifies the output for print statements"""
    
    print("HELPER.PY:", message)

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
    return inputMenu(list(options.keys), prompt, numbered=True)

def prompt_for_yes_no():
    """Prompts the user for a yes or no response."""

    return inputYesNo()

def enter_to_continue(prompt="Press Enter to continue"):
    """Function that prompts the user to press enter to continue.
    
    Args:
        prompt (str): An option display message. Defaults to 'Press enter to continue'"""

    input(prompt)

def create_thread(func:function, daemon=True, args=tuple()):
    """Creates a threaded function and returns the thread object
    
    Args:
        func (function): The function to be threaded
        daemon (bool): Whether the thread should be daemon or not
        
    Returns:
        Thread - The threaded function"""
    
    thread = Thread(target=func, args=args, daemon=daemon)
    thread.start()
    return thread