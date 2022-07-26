from xml.dom.minidom import TypeInfo
import helper
from ScriptReading import Reader
from TypeForMe import Typer
from time import sleep

class Main:
    """Class responsible for managing the main functionality of the program.
    
    Attrs:
        reader (Reader): An instance of the Reader class being used for reading.
        typer (Typer): An instance of the Typer class being used for typing

    """
    def __init__(self) -> None:
        self.reader = None
        self.typer = None

    def run(self):
        """The main control loop for the Assistant"""

        while True:
            self.menu()
            helper.enter_to_continue()

    def menu(self):
        """Displays the menu for the user to select their choice"""

        prompt = "\nHere is what I have to offer. Select from the options below.\n"
        menu_options[helper.prompt_for_choice(prompt, menu_options)]()

    def setup_read_script(self):
        """Performs setup for a script to be read"""

        if self.reader:
            print("A script is currently being read. Would you like to force stop it? Yes or No?\n:")
            if helper.prompt_for_yes_no() == "yes":
                self.reader.running = False
                self.reader = None
            return True

        self.reader = Reader.Reader()
        helper.create_thread(self.reader.run)

    def type_code(self):
        self.typer = Typer.Typer()
        try:
            self.typer.type_it()
        except Typer.TypeInfoException as err:
            print(err)

if __name__ == "__main__":
    main = Main()

    menu_options = {
        "Read Script": main.setup_read_script,
        "Type code": main.type_code,
        "Quit": helper.ask_and_quit
    }

    main.run()