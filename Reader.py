import time
import os
from tkinter import filedialog, Tk
import Engine


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


class Reader:
    """The main class of the program
    
    Attrs:
        engine (Engine): The TTS engine.
        script (list): The script broken into lines
        commands (list): List of commands
        cmd (str): The current command to be run.
        running (bool): Whether the script should be allowed to run or not.
        paused (bool): Whether to pause the reading or not
        repeat_line (bool): Whether to repeat the current line or not

    Methods:
        setup(): Used to set up everything the program needs
        run(): Used to run the main program
        is_command(msg:str): Used to check if a line of the script is a command.
        exe_command(msg:str): Used to execute a command."""

    def __init__(self) -> None:
        self.script = None
        self.engine = Engine.Engine()
        self.commands = ["wait", "input"]
        self.cmd = None
        self.file_path = ""
        self.running = True
        self.paused = False
        self.repeat_line = False

    def run(self):
        """Used to run the program."""
        self.setup()

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

    def setup(self):
        """Used to setup everything the program needs."""
        root = Tk()

        self.file_path = filedialog.askopenfilename(initialdir="Files/", title="Select txt file for me to read.", filetypes=(("text", "*.txt"),))
        root.destroy()

        if not self.file_path:
            raise ReaderException("No file was selected")

        with open(self.file_path) as fp:
            script = fp.readlines()

        self.script = [line for line in script if not line.startswith("#")]

        if not self.script:
            raise ReaderException("Script file is empty.")

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
            time.sleep(secs)
        if self.cmd == "input":
            input("Press enter to continue")


if __name__ == "__main__":
    main = Reader()
    main.run()

