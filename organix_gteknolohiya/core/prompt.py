from core import FileOrganizer
from utils import recognize_speech, clc_print, print_with_delay

class Prompt:
    def __init__(self):
        """
        Initializes a new Prompt object and creates an instance of the FileOrganizer class.
        """
        self.organizer = FileOrganizer()

    def ask_task(self, *args):
        """
        Asks the user what task they want to perform and lists out the available options.

        Args:
        *args: Accepts any number of arguments for the available tasks.

        Returns:
        None
        """
        tasks = []

        clc_print(f"What do you want to do? Do you want to:")

        for index, item in enumerate(args):
            task = f"{item}"  
            tasks.append(task)  
                 
        print_with_delay("\n".join(tasks), 2) 

    def confirm_task(self, task):
        """
        Confirms if the user wants to perform a task on files in the folder, based on the recognized speech response.
        
        Args:
        task (str): The name of the task to be performed on the files in the folder.
        
        Returns:
        bool: Returns False if user responds "no".
        
        """
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

                

        