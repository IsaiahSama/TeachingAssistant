"""This file contains the base class from which the Reader and Typer classes are derived"""

import Engine
import helper

from time import sleep

class Aid:
    """Base class for Reader and Typer classes.
    
    Attrs:
        class_name (str): The name of the class inheriting from the Base class
        engine (Engine.Engine): The tts engine to be used
        commands (list): The list of commands available
        cmd (None | str): The current command to be executed
        running (bool): Whether the script should continue doing its task
        paused (bool): Whether the script should be paused or not
        script (list[str]): A list of strings containing text read from a file

    Methods:
        setup -> None: Can be overriden to provide custom setup features
        is_command(msg:str) -> bool: Checks if the current line contains a command for the Typer
        exe_command(msg:str) -> None: Executes a command for the Typer
        run -> None: To be overriden. Runs the main loop for the Class
        Print(*args) -> None: Outputs a message with modified formatting
    """

    def __init__(self, class_name:str="AID") -> None:
        self.class_name = class_name
        self.engine = Engine.Engine()
        self.commands = ["wait", "input", "rate", "voice"]
        self.current_cmd = None
        self.running = True
        self.paused = False 
        self.script = helper.load_script()

    def Print(self, *message):
        """Modifies output from print statement
        
        Args:
            *message - The message to be output"""

        print(self.class_name, *message)

    def setup(self) -> None:
        """Base function to be overriden to provide custom setup features"""
        pass

    def run(self) -> None:
        """Base function to be overriden to provide the run loop"""
        pass

    def is_command(self, msg:str) -> bool:
        """Used to detect whether a given line of text is a command or not
        
        Args:
            msg (str): The line of text to check
            
        Returns:
            bool"""
        
        if msg.startswith("Command:"):
            text = msg.split(" ")
            command = text[0].split(":")[-1]
            for cmd in self.commands:
                if command == cmd:
                    self.current_cmd = cmd
                    return True
        return None

    def exe_command(self, command:str) -> bool:
        """Used to execute a given command
        
        Args:
            command (str): The command to be parsed
            
        Returns:
            Bool: True if the given command was handled by this function"""
        text = command.split(" ")[1:]
        
        if self.current_cmd == "wait":
            val = text[-1].strip()
            if helper.is_num(val):
                self.Print("Waiting", val, "seconds")
                sleep(float(val))
            return True

        if self.current_cmd == "input":
            input("Press enter to continue")
            sleep(5)

        if self.current_cmd == "rate":
            new_rate = text[-1].strip()
            if helper.is_num(new_rate):
                self.engine.rate = int(new_rate)
                self.Print("The new engine rate is", self.engine.rate)
            else:
                self.Print(new_rate, "is not a number")
        
        if self.current_cmd == "voice":
            new_voice = text[-1].strip()
            if helper.is_num(new_voice):
                if int(new_voice) in [0, 1]:
                    self.engine.voice = int(new_voice)
                    self.Print("The new voice is", self.engine.voice)
                else:
                    self.Print("Values for new voices are 0 and 1, not", new_voice)
