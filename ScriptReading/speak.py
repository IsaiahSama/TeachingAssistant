import time
import os
from tkinter import filedialog, Tk
import engine


# FILE_PATH = "./Script.txt"


def ask_and_quit():
    input("Press enter to exit")
    raise SystemExit


class Main:
    """The main class of the program
    
    Attrs:
        engine (Engine): The TTS engine.
        script (list): The script broken into lines
        commands (list): List of commands
        cmd (str): The current command to be run.

    Methods:
        setup(): Used to set up everything the program needs
        run(): Used to run the main program
        is_command(msg:str): Used to check if a line of the script is a command.
        exe_command(msg:str): Used to execute a command."""

    def __init__(self) -> None:
        self.script = None
        self.engine = engine.Engine()
        self.commands = ["wait"]
        self.cmd = None
        self.file_path = ""

    def run(self):
        """Used to run the program."""
        self.setup()

        for line in self.script:
            try:
                if self.is_command(line):
                    self.exe_command(line)
                else:
                    self.engine.say_and_print(line)
            except KeyboardInterrupt:
                raise SystemExit

    def setup(self):
        """Used to setup everything the program needs."""
        root = Tk()

        self.file_path = filedialog.askopenfilename(initialdir="./Scripts", title="Select txt file for me to read.", filetypes=(("text", "*.txt"),))
        root.destroy()

        if not self.file_path:
            print("No file was selected")
            ask_and_quit()

        with open(self.file_path) as fp:
            script = fp.readlines()

        self.script = [line for line in script if not line.startswith("#")]

        if not self.script:
            print("Script file is empty.")
            ask_and_quit()

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
                print(val, "is not a number, so no waiting will be done.")
                return False
            secs = float(val)
            print("Waiting", secs, "seconds")
            time.sleep(secs)


if __name__ == "__main__":
    main = Main()
    main.run()

