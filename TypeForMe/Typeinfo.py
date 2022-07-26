"""Script used to take control of the keyboard and type output to the screen"""
import keyboard

from time import sleep
from tkinter import Tk, filedialog

def Print(*message):
    """Custom output from the print function.
    
    Args:
        *args - The args to be output"""

    print(*message)

class TypeInfoException(Exception):
    """An exception raised by the Typeinfo module"""

    def __init__(self, *text):
        message = "TypeInfoException: " + " ".join(text)
        super().__init__(message)

class Typer:
    """Class used to manage the typing of scripts and the like.
    
    Attrs:
        script_text (list): The lines of the script
        commands (list): A list of commands that can be used to control the Typer
    
    Methods:
        get_file -> str: used to get the file containing the script to be typed
        load_script -> None: used to load the script to be typed from the file
        is_command -> bool: Checks if the current line contains a command for the Typer
        exe_command -> None: Executes a command for the Typer
        type_it -> None: Used to type the script line by line to the current active window.
        
    """

    def __init__(self) -> None:
        self.script_text = None

    def get_file(self) -> str:
        """Method used to get the file containing the script the be typed
        
        Returns:
            str - The filename"""
        root = Tk()

        filename = filedialog.askopenfilename(("Text", "*.txt"),)
        root.destroy()

        return filename

    def load_script(self):
        filename = self.get_file()
        if not filename:
            Print("No file was loaded")
            raise TypeInfoException("No filename was provided!")

        with open(filename) as fp:
            self.script_text = fp.readlines()

        if not self.script_text:
            raise TypeInfoException("Script file was empty!")

    def is_command(self, msg:str) -> bool:
        """Used to detect whether a given line of text is a command or not
        
        Args:
            msg (str): The message to check."""
        
        text = msg.split(" ")
        for cmd in self.commands:
            if text[0] == cmd:
                self.cmd = cmd
                return True
        return None

    def exe_command(self, msg:str) -> bool:
        """Used to execute a given command.
        
        Args:
            msg (str): The string containing the command.
        
        Returns:
            Bool"""
        
        # Parsing time.
        if self.cmd == "wait":
            text = msg.split("wait")[1:]
            val = text[-1].strip()
            if not val.isnumeric():
                Print(val, "is not a number, so no waiting will be done.")
                return False
            secs = float(val)
            Print("Waiting", secs, "seconds")
            sleep(secs)

    def type_it(self):
        """Method responsible for actually typing to the current window."""
        
        Print("Starting in 5 seconds")
        sleep(5)

if __name__ == "__main__":
    main = Typer()
