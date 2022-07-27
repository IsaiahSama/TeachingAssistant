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
        wait_time (float): The time to wait inbetween typing each character.
    Methods:
        get_file -> str: used to get the file containing the script to be typed
        load_script -> None: used to load the script to be typed from the file
        is_command -> bool: Checks if the current line contains a command for the Typer
        exe_command -> None: Executes a command for the Typer
        type_it -> None: Used to type the script line by line to the current active window.
        
    """

    def __init__(self) -> None:
        self.script_text = None
        self.commands = ["wait", "typespeed", "input"]
        self.wait_time = 0.2

    def get_file(self) -> str:
        """Method used to get the file containing the script the be typed
        
        Returns:
            str - The filename"""
        root = Tk()

        filename = filedialog.askopenfilename(initialdir="./ToType", title="Select Your File", filetypes=(("Text", "*.txt"),))
        root.destroy()

        return filename

    def load_script(self):
        filename = self.get_file()
        if not filename: raise TypeInfoException("No filename was provided!")

        with open(filename) as fp:
            self.script_text = fp.readlines()

        if not self.script_text:
            raise TypeInfoException("Script file was empty!")

    def is_command(self, msg:str) -> bool:
        """Used to detect whether a given line of text is a command or not
        
        Args:
            msg (str): The message to check."""
        
        if msg.startswith("Command:"):
            text = msg.split(" ")
            command = text[0].split(":")[-1]
            for cmd in self.commands:
                if command == cmd:
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
            try:
                val = float(val)
            except ValueError:
                Print(val, "is not a number, so no waiting will be done.")
                return False
                
            secs = float(val)
            Print("Waiting", secs, "seconds")
            sleep(secs)

        if self.cmd == "typespeed":
            text = msg.split(" ")[1:]
            new_speed = text[-1].strip()
            try:
                new_speed = float(new_speed)
            except ValueError:
                Print(new_speed, "is not a number, so speed remains unchanged")
                return False

            new_speed = float(new_speed)
            Print("Set typing speed to have a delay of", new_speed)
            self.wait_time = new_speed

        if self.cmd == "input":
            input("Press enter to continue")
            sleep(5)

    def type_it(self):
        """Method responsible for actually typing to the current window."""
        self.load_script()

        Print("Starting in 5 seconds")
        sleep(5)

        for line in self.script_text:
            try:
                if self.is_command(line):
                    self.exe_command(line)
                else:
                    for character in line:
                        keyboard.write(character)
                        sleep(self.wait_time)
                        
                    keyboard.press_and_release("enter")
                    sleep(2)
            except KeyboardInterrupt:
                Print("Stopping!")
                break


if __name__ == "__main__":
    main = Typer()
    main.type_it()