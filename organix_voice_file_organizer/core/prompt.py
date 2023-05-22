from core import FileOrganizer
from utils import recognize_speech, clc_print, get_folder_path

class Prompt:
    """
    A class used to interact with the user for organizing files.

    Attributes
    ----------
    organizer : FileOrganizer
        an instance of the FileOrganizer class for managing files

    Methods
    -------
    ask_task(*args)
        Prompts the user with tasks for organizing files.
    confirm_task(task)
        Asks the user for confirmation to proceed with the given task.
    ask_name()
        Asks the user for a new file name and confirms it.
    """    
    def __init__(self):
        """
        Constructs all the necessary attributes for the Prompt object.

        Attributes
        ----------
        organizer : FileOrganizer
            an instance of the FileOrganizer class
        """
        self.organizer = FileOrganizer()

    def ask_task(self, *args):
        """
        Prompts the user with tasks for organizing files.

        Parameters
        ----------
        *args : str
            Variable length argument list of tasks.
        """        
        tasks = []

        clc_print("Declutter mode on! What to do?")

        for index, item in enumerate(args):
            task = f"{item}"  
            tasks.append(task)  
                 
        print("\n".join(tasks)) 

    def confirm_task(self, task):
        """
        Asks the user for confirmation to proceed with the given task.

        Parameters
        ----------
        task : str
            The task to be confirmed.
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

    def confirm_change_path(self, task, action):
        """
        Asks the user for confirmation to proceed with the given task.

        Parameters
        ----------
        task : str
            The task to be confirmed.
        """        
        clc_print(f"Do you want to {action}? Yes or No?")
        response = recognize_speech()

        if "yes" in response:
             folder_path = get_folder_path()
             self.organizer.change_folder_path(folder_path)
        elif "no" in response:
            return False
        else:
            clc_print("Invalid response. Please try again.")        


                

        