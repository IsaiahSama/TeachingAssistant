"""Script used to take control of the keyboard and type output to the screen"""

from xml.dom.minidom import TypeInfo
import keyboard
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
    """Class used to manage the typing of scripts and the like"""

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

if __name__ == "__main__":
    main = Typer()
