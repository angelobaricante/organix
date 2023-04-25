from .recognize_speech import recognize_speech
from .clc_print import clc_print

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