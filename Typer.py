"""Script used to take control of the keyboard and type output to the screen"""
import keyboard

import Aider
import helper

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


class Typer(Aider.Aid):
    """Class used to manage all automated typing. Inherits from Aid.Aid
    
    Attrs:
        script (list): The lines of the script
        commands (list): A list of commands that can be used to control the Typer
        wait_time (float): The time to wait inbetween typing each character.
        paused (bool): Whether the typer is paused or not
        running (bool): Whether the typer is running or not

    Methods:
        exe_command -> None: Executes a command for the Typer
        run -> None: Used to type the script line by line to the current active window.

    """

    def __init__(self) -> None:
        super().__init__("Typer")
        self.commands += ["typespeed", "presskey"]
        self.wait_time = 0.2

    def exe_command(self, command: str) -> bool:
        # I.E, If the default handler didn't handle the command, then it's a unique command
        if not super().exe_command(command):
            text = command.split(" ")[1:]

            if self.current_cmd == "typespeed":
                value = text[-1].strip()
                if helper.is_num(value):
                    self.Print("Set typing speed to have a delay of", value)
                    self.wait_time = float(value)

            if self.current_cmd == "presskey":
                key = text[-1].strip()
                try:
                    keyboard.press_and_release(key)
                except Exception as err:
                    Print(err)

    def run(self):
        Print("Starting in 5 seconds")
        sleep(5)

        for line in self.script:
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
    main.run()