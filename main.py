
from components import Prompt
from components import recognize_speech

def handle_task(task, prompt):
    """Executes the corresponding task based on user input"""
    if task == "organize": 
        prompt.auto_organize_prompt()
    elif task == "rename":
        prompt.auto_rename_prompt()
    elif task == "delete":
        prompt.auto_delete_prompt()
    else:
        print("I don't know what you said. Please try again.")

def main():
    # Ask the user what folder directory they want to use
    folder_path = input("Enter the directory you want to use:")

    # Ask the user what task they want to do
    prompt = Prompt(folder_path)

    # Handle user input and execute corresponding task
    while True:
        task = recognize_speech("Hi! I'm Organix. What do you like to do? :")
        handle_task(task, prompt)

if __name__ == "__main__":
    main()
