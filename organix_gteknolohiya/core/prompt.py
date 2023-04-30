from core import FileOrganizer
from utils import recognize_speech, clc_print, print_with_delay

class Prompt:
    def __init__(self):
        self.organizer = FileOrganizer()

    def ask_task(self, *args):
        tasks = []

        clc_print(f"What do you want to do? Do you want to:")

        for index, item in enumerate(args):
            task = f"{item}"  
            tasks.append(task)  
                 
        print_with_delay("\n".join(tasks), 2) 

    def confirm_task(self, task):
        clc_print(f"Do you want to {task} files in the folder? Yes or No?")
        response = recognize_speech()

        if response == "yes":
            task_name = f"auto_{task}"
            task_to_call = getattr(self.organizer, task_name)
            task_to_call()  
        elif response == "no":
            return False
        else:
            clc_print("Invalid response. Please try again.")

                

        