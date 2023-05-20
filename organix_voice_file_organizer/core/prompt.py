from core import FileOrganizer
from utils import recognize_speech, clc_print, print_with_delay

class Prompt:
    def __init__(self):
        self.organizer = FileOrganizer()

    def ask_task(self, *args):
        tasks = []

        clc_print("Declutter mode on! What to do?")

        for index, item in enumerate(args):
            task = f"{item}"  
            tasks.append(task)  
                 
        print_with_delay("\n".join(tasks), 2) 

    def confirm_task(self, task):
        clc_print(f"Do you want to {task} files in the folder? Yes or No?")
        response = recognize_speech()

        if "yes" in response:
            task_name = f"auto_{task}"
            task_to_call = getattr(self.organizer, task_name)
            task_to_call()  
        elif "no" in response:
            return False
        else:
            clc_print("Invalid response. Please try again.")

    def ask_name():
        while True:
            clc_print("What would you like the files to be renamed as?")
            response = recognize_speech().title()
            file_name = response

            clc_print(f"The filename you mentioned is {file_name}. Are you sure this is what you want to rename the files as? Yes or No?")
            response = recognize_speech()

            if response == "yes":
                return file_name
            elif response == "no":
                clc_print("Going back to the last question...")
            else:
                clc_print("Invalid option! Try again!")

                

        