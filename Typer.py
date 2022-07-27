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
        paused (bool): Whether the typer is paused or not
        running (bool): Whether the typer is running or not

    Methods:
        get_file -> str: used to get the file containing the script to be typed
        load_script -> None: used to load the script to be typed from the file
        is_command -> bool: Checks if the current line contains a command for the Typer
        exe_command -> None: Executes a command for the Typer
        type_it -> None: Used to type the script line by line to the current active window.
        
    """

    def __init__(self) -> None:
        self.script_text = None
        self.commands = ["wait", "typespeed", "input", "presskey"]
        self.wait_time = 0.2
        self.paused = False
        self.running = True

    def get_file(self) -> str:
        """Method used to get the file containing the script the be typed
        
        Returns:
            str - The filename"""
        root = Tk()

        filename = filedialog.askopenfilename(initialdir="Files/", title="Select Your File", filetypes=(("Text", "*.txt"),))
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

    def is_num(self, val:str):
        """Used to check whether a given value is a floating point number.
        
        Args:
            val (str): The value to check"""
        try:
            val = float(val)
        except ValueError:
            Print(val, "is not a number.")
            return False
        return True

    def exe_command(self, msg:str) -> bool:
        """Used to execute a given command.
        
        Args:
            msg (str): The string containing the command.
        
        Returns:
            Bool"""
        
        # Parsing time.
        text = msg.split(" ")[1:]
        if self.cmd == "wait":
            val = text[-1].strip()
            if self.is_num(val):
                Print("Waiting", val, "seconds")
                sleep(float(val))

        if self.cmd == "typespeed":
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

        if self.cmd == "presskey":
            key = msg.split(" ")[1:].strip()
            try:
                keyboard.press_and_release(key)
            except Exception as err:
                Print(err)
            
        if self.cmd == "rate":
            new_rate = text[-1].strip()
            if self.is_num(new_rate):
                self.engine.rate = new_rate
                Print("The new engine rate is", self.engine.rate)
        
        if self.cmd == "voice":
            new_voice = text[-1].strip()
            if self.is_num(new_voice):
                if new_voice in [0, 1]:
                    self.engine.voice = int(new_voice)
                else:
                    Print("Values for new voices are 0 and 1")

    def type_it(self):
        """Method responsible for actually typing to the current window."""
        self.load_script()

        Print("Starting in 5 seconds")
        sleep(5)

        for line in self.script_text:
            while self.paused: sleep(0.2)
            if not self.running: return
            line = line.strip("\n")
            if self.is_command(line):
                self.exe_command(line)
            else:
                for character in line.strip():
                    while self.paused: sleep(0.2)
                    if not self.running: return
                    keyboard.write(character)
                    sleep(self.wait_time)
                    
                keyboard.press_and_release("enter")
                sleep(2)


if __name__ == "__main__":
    main = Typer()
    main.type_it()