import helper
from ScriptReading import Speak
from time import sleep

class Main:
    def __init__(self) -> None:
        pass

    def run(self):
        """The main control loop for the Assistant"""
        while True:
            self.menu()
            helper.enter_to_continue()

    def menu(self):
        prompt = "Here is what I have to offer. Select from the options below."
        menu_options[helper.prompt_for_choice(prompt, menu_options)]()


if __name__ == "__main__":
    main = Main()

    menu_options = {
        "Read Script": main.read_script,
        "Type code": main.type_code
    }

    main.run()