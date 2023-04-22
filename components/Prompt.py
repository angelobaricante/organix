from components import FileOrganizer
from components.recognize_speech import recognize_speech


class Prompt:
    def __init__(self, folder_path):
        self.folder_path = folder_path   
        self.organizer = FileOrganizer(self.folder_path)

    def auto_organize_prompt(self):
        self.organizer.auto_organize()

    def auto_rename_prompt(self):
        while True:
            text = recognize_speech("Do you want to rename the files in this folder? Yes/No")
            if text == "yes":
                while True:
                    text = recognize_speech("What would you like the files to be renamed as?").title()
                    file_name = text
                    text = recognize_speech(f"The filename you mentioned is {file_name}. Are you sure this is what you want to rename the files as? Yes/No: ")
                    if text == "yes":
                        self.organizer.auto_rename(file_name)
                        print("File rename is successful!")
                        return 
                    elif text == "no":
                        print("Going back to the last question...")
                    else:
                        print("Invalid option! Try again!")
            elif text == "no":
                # babalik dun sa tatlong option, please insert a while loop
                pass
            else:
                print("Invalid option! Try again!")

    def auto_delete_prompt(self):
        self.organizer.auto_delete()
