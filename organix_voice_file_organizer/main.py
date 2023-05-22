from core import Prompt, FileOrganizer
from utils import recognize_speech, clc_print, print_with_delay

"""
This is the main module of the OrganiX application, a voice-activated file management system.

The application listens for user commands to organize, rename, see to-do list, delete files, or to exit the program.
The recognized speech is analyzed, and the appropriate action is taken based on the user's response.
Invalid responses are met with a request for the user to try again.

The module uses the `Prompt` class from the core module and the `recognize_speech`, `clc_print`, and 
`print_with_delay` functions from the utils module.

Functions:
    - main(): The entry point for the application.
"""

def main():
    """
    Main function of the OrganiX application.

    Creates a `Prompt` object and enters a loop where it continuously asks the user for tasks to perform.
    The tasks include organizing, renaming, deleting files, or exiting the program.
    The user's speech is recognized and the application performs the requested task.
    The loop continues until the user asks to exit the program.
    """
    prompt = Prompt()

    program_on = True

    while program_on == True:
        prompt.ask_task("1. Organize", "2. Rename", "3. Delete", "4. Change folder path", "5. Exit")
        print_with_delay("\nPlease pick an option from the list.", 0.2)
        response = recognize_speech()  

        while True:
            if "organize" in response or "one" in response:
                prompt.confirm_task("organize")
                break
            elif "rename" in response or "two" in response:
                prompt.confirm_task("rename")    
                break        
            elif "delete" in response or "three" in response:
                prompt.confirm_task("delete")
                break
            elif "change folder path" in response or "four" in response:
                prompt.confirm_change_path("folder_path", "change the folder path")
                break
            elif "exit" in response or "five" in response:
                program_on = False
                clc_print("Goodbye from OrganiX! Happy organizing!")
                break
            else:
                print_with_delay("Invalid response. Please try again.", 2)
                break

if __name__ == "__main__":
    main()
