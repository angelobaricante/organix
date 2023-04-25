from modules import FileOrganizer
from utils import recognize_speech
class Prompt:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.organizer = FileOrganizer(self.folder_path)

    def ask_task(self, *args):
        tasks = []  
        print(f"What do you want to do? Do you want to:")

        for index, item in enumerate(args):
            task = f"{index + 1}. {item}"  
            tasks.append(task)  
        
        print("\n".join(tasks)) 

    def confirm_task(self, task):
        response = recognize_speech(f"Do you want to {task} files in the folder? Yes or No?")

        if response == "yes":
            task_name = f"auto_{task}"
            task_to_call = getattr(self.organizer, task_name)
            task_to_call()
        elif response == "no":
            return False
        else:
            print("Invalid response. Please try again.")

                

        