from modules import FileOrganizer
from utils import recognize_speech

class Prompt:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.organizer = FileOrganizer(self.folder_path)

    def ask_task(self, *args):
        tasks = []  # create an empty list to store the options
        print(f"What do you want to do? Do you want to:")

        for index, item in enumerate(args):
            task = f"{index + 1}. {item}"  # format the item as an task
            tasks.append(task)  # add the option to the list of options
        
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

                


      
# prompt = Prompt(get_folder_path())
# # organizer = FileOrganizer(get_folder_path())

# #1. Ask what task to do
# program_on = True

# while program_on == True:
#     todo = recognize_speech(prompt.ask_task("organize", "rename", "delete"))

#     while True:
#         if todo == "organize":
#             prompt.confirm_task("organize")
#         elif todo == "rename":
#             prompt.confirm_task("rename")    
#         elif todo == "delete":
#             prompt.confirm_task("delete")
#         else:
#             print("Invalid response. Please try again.")
#             break         
           
        