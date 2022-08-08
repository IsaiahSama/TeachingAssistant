"""This file will handle the management of students with the program.


Format for YAML file:

student_name:
    NAME: str
    POINTS: int"""

import yaml
import helper
from os import path 

filename = "./students.yaml"

def Print(*message):
    """Used to output a message from the Students file"""

    print("STUDENTS:", *message)

class Students:
    """Class used to manage the students of a given class
    
    Attrs:
        students (dict): Dictionary of students loaded from the yaml file
        running (bool): Whether to keep prompting the user for the main menu or not
    
    Methods:
        add_students(): Used to add students from a text file.
        prompt_for_name(): Used to prompt for a student's name
        check_points(): Used to check points.
        points_for(): Displays the points a given student has
        min_max_points(): Displays the people with the highest and lowest point values
        reward_points(): Used to give points to a student.
        save(): Used to save the local dictionary to the yaml file
        menu(): Provides the menu interface for the user to interact with the student class
        return_to_caller(): Sends the user back to Assistant.py. This class is not threaded.
        """

    students = {}
    running = True
        
    def __init__(self) -> None:
        if not path.exists(filename):
            with open(filename, "w"):
                Print("Performed first time setup")
                pass
        else:
            with open(filename) as fp:
                self.students = yaml.safe_load(fp)
                Print("Loaded students")

    def menu(self):
        """The menu interface the user will use while using the student class"""
        self.running = True

        options = {
            "Add students": self.add_students,
            "Check points": self.check_points,
            "Reward Points": self.reward_points,
            "Return to Assistant": self.return_to_caller}

        while self.running:
            Print("Select the task you want to do from below.")
            options[helper.prompt_for_menu("\n", options)]()
    
    def add_students(self) -> None:
        """Method used to add students to the yaml file from a text file. Student names must be separated by new lines"""

        print("Select the text file containing the students' names.")
        print("Be sure that each student's name is separated by a new line")

        filepath = helper.get_file()
        if not filepath:
            Print("No file was selected")
            return False

        with open(filepath) as fp:
            student_names = fp.readlines()

        if not student_names:
            Print("No student names were found.")
            return False

        for name in student_names:
            self.students.setdefault(name, {"NAME": name, "POINTS": 100})

    def prompt_for_name(self) -> str:
        """Requests the user to enter a valid student's name
        
        Returns:
            str - The name"""
        
        prompt = "Select the student's name from the list below\n"
        return helper.prompt_for_choice(prompt, list(self.students.keys()))

    def check_points(self) -> None:
        """Provides a menu for checking various point related information"""

        menu = {"CHECK POINTS FOR...": self.points_for, "HIGHEST AND LOWEST POINTS": self.min_max_points}
        prompt = "What would you like to do with points? Select from the below menu."
        
        choice = helper.prompt_for_menu(prompt, menu)
        menu[choice]()

    def points_for(self):
        """Displays the amount of points a given student has."""
        name = self.prompt_for_name()

        print(name, "has", self.students[name]["POINTS"], "points.")


    def min_max_points(self):
        """Displays the students with the highest and lowest point values"""

        highest_point = max(self.students.items(), key=lambda x: x[1]["POINTS"])[1]["POINTS"]
        lowest_point = min(self.students.items(), key=lambda x: x[1]["POINTS"])[1]["POINTS"]

        high_achievers = [name for name in self.students.keys() if self.students[name]["POINTS"] == highest_point]
        low_achievers = []
        if highest_point != lowest_point:
            low_achievers = [name for name in self.students.keys() if self.students[name]["POINTS"] == lowest_point]

        print("HIGH ACHIEVERS with", highest_point, "points are:", '\n'.join(high_achievers))
        print("LOW ACHIEVERS with", lowest_point, "points are:", '\n'.join(low_achievers if low_achievers else ["NO", "ONE"]))
            

    def reward_points(self):
        """Used to grant points to a student. Use negative numbers to deduct points"""        
        student_name = self.prompt_for_name()

        prompt = "How many points are you giving to " + student_name + "?"
        amount = helper.prompt_for_int(prompt)

        self.students[student_name]["POINTS"] += amount

        print("Gave", student_name, amount, "points.")
        self.save()

    def save(self):
        """Method used to update the yaml file with the current data"""
        with open(filename, "w") as fp:
            yaml.safe_dump(self.students, fp, indent=4)
            Print("Saved students")

    def return_to_caller(self):
        self.running = False