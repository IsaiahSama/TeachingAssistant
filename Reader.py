from random import choice
import time

import Engine
import Aider

from tkinter import filedialog, Tk
from os import path

# FILE_PATH = "./Script.txt"


def ask_and_quit():
    input("Press enter to exit")
    raise SystemExit

def Print(*message:str):
    """Used to Print a message to the console. This will differentiate where each message comes from."""

    print("SPEAK.PY:", *message)


class ReaderException(Exception):
    """Exception raised by the Reader.py module"""

    def __init__(self, *text):
        message = "ReaderException: " + ' '.join(text)
        super().__init__(message)


class Reader(Aider.Aid):
    """Class responsible for handling the Reading activites of the script. Inherits from Aider
    
    Attrs:
        engine (Engine): The TTS engine.
        script (list): The script broken into lines
        commands (list): List of commands
        cmd (None | str): The current command to be run.
        running (bool): Whether the script should be allowed to run or not.
        paused (bool): Whether to pause the reading or not
        repeat_line (bool): Whether to repeat the current line or not

    Methods:
        run(): Used to run the main program
        is_command(msg:str): Used to check if a line of the script is a command.
        exe_command(msg:str): Used to execute a command."""

    def __init__(self):
        super().__init__("Reader")
        self.repeat_line = False
        self.commands += ["select"]

    def run(self):
        """Used to run the program."""
        self.script = [line for line in self.script if line.strip() != '']
        line_count = len(self.script)
        current_line = 0

        while current_line < line_count:
            line = self.script[current_line]
            if not self.running: raise SystemExit
            while self.paused: time.sleep(0.2)
            try:
                if self.is_command(line):
                    self.exe_command(line)
                else:
                    self.engine.say_and_print(line)
            except KeyboardInterrupt:
                self.running = False
                raise SystemExit
            
            if self.repeat_line:
                time.sleep(5)
                self.repeat_line = False
                continue
                
            current_line += 1
        self.running = False

    def is_command(self, msg:str) -> bool:
        """Used to detect whether a given line of text is a command or not.
        
        Args:
            msg (str): The eline to check
            
        Returns:
            bool"""

        text = msg.split(" ")
        for cmd in self.commands:
            if text[0] == cmd:
                self.current_cmd = cmd
                return True
        return None
    
    # No custom commands so no need to overwrite.
    def exe_command(self, command: str) -> bool:
        if not super().exe_command(command):
            text = command.split(" ")[1:]

            if self.current_cmd == "select":
                filename = text[-1].strip()
                if not path.exists(filename):
                    self.Print("No filename called", filename, "exists")
                    return False
                with open(filename) as fp:
                    options = fp.readlines()
                chosen = choice([option for option in options if option.strip() != ""])
                self.engine.say_and_print(chosen)



if __name__ == "__main__":
    main = Reader()
    main.run()

