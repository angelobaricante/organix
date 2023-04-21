import os
import glob
import pygame
from recognize_speech import recognize_speech


def rename_files (folder_path, filename):
    # glob.glob function lists files or folders that matches the path specified; asterisk means all
    files = glob.glob(os.path.join(folder_path, "*"))
    # files will now be sorted by modification time
    files = sorted(files, key=os.path.getmtime)
    # for each file in the directory, it will perform these actions:
    for i, file in enumerate(files):
        try:
            # program will get file extension and assign it; root = [0], extension = [1]
            ext = os.path.splitext(file)[1]
            # program will make a new filename with an incrementing index while making sure the extension is retained
            new_filename = f"{filename} - {i+1}{ext}"
            # program will rename the file to the new filename
            os.rename(file, os.path.join(folder_path, new_filename))
        except OSError:
            print("Invalid operation!")

def rename_files_recognizer():
    while True:
            print("Do you want to rename the files in this folder? Yes/No")
            text = recognize_speech()
            if text == "yes":
                while True:
                    print("What would you like the files to be renamed as?")
                    text = recognize_speech().title()
                    filename = text
                    print(f"The filename you mentioned is {filename}. Are you sure this is what you want to rename the files as? Yes/No: ")
                    text = recognize_speech()
                    if text == "yes":
                        rename_files (folder_path, filename)
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

# Please reassign folder path below to the select directory function's choosing
folder_path = r"C:\Users\acer\Desktop\Test"

rename_files_recognizer()

