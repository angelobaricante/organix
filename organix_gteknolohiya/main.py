from modules import Prompt
from utils import get_folder_path, recognize_speech

def main():
    prompt = Prompt(get_folder_path())
    # organizer = FileOrganizer(get_folder_path())

    #1. Ask what task to do
    program_on = True

    while program_on == True:
        todo = recognize_speech(prompt.ask_task("organize", "rename", "delete"))

        while True:
            if todo == "organize":
                prompt.confirm_task("organize")
            elif todo == "rename":
                prompt.confirm_task("rename")    
            elif todo == "delete":
                prompt.confirm_task("delete")
            else:
                print("Invalid response. Please try again.")
                break        

if __name__ == "__main__":
    main()
