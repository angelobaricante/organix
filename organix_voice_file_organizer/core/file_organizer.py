import os
import shutil
import glob

from utils import file_types, get_folder_path, print_with_delay, clc_print, recognize_speech
class FileOrganizer:
    """
    A class to handle file organization tasks such as automatic file organization, renaming, and deletion.
    """

    def __init__(self):
        """
        Initializes the FileOrganizer instance. Sets the directory for file operations.
        """
        self.file_types = file_types
        self.folder_path = get_folder_path()

    def has_files(self):
        """
        Checks if the target directory has any files.

        Returns:
            bool: True if directory has any files, False otherwise.
        """
        return any(os.path.isfile(os.path.join(self.folder_path, file_name)) for file_name in os.listdir(self.folder_path))

    def find_files_by_extension(self, extensions):
        """
        Finds files in the target directory matching provided file extensions.

        Args:
            extensions (list): List of file extensions to search for.

        Returns:
            list: List of filenames that match the provided extensions.
        """
        return [f for f in os.listdir(self.folder_path) if os.path.splitext(f)[1].lower() in extensions]
    
    def ask_name():
        """
        Prompts the user to provide a new name for renaming files.
        Continues asking until a valid response is given.

        Returns:
            str: New name for files.
        """        
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

    def auto_organize(self):
        """
        Automatically organizes files in the target directory by file type.
        Each file is moved to a folder named after its file type.
        If the folder doesn't exist, it is created.
        """        
        if not self.has_files():
            print_with_delay("\nThere's no file to organize.", 2)
            return

        for file_name in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, file_name)
            if os.path.isfile(file_path):
                file_extension = os.path.splitext(file_name)[1].lower()
                for file_type, extensions in self.file_types.items():
                    if file_extension in extensions:
                        destination_folder = os.path.join(self.folder_path, file_type)

                        if not os.path.exists(destination_folder):
                            os.makedirs(destination_folder)

                        destination_file_path = os.path.join(destination_folder, file_name)
                        suffix = 1
                        while os.path.exists(destination_file_path):
                            destination_file_path = os.path.join(destination_folder, f"{os.path.splitext(file_name)[0]} ({suffix}){file_extension}")
                            suffix += 1

                        shutil.move(file_path, destination_file_path)
                        print(f"Moved {file_name} to {destination_file_path}", 0.2)
                        break
                else:
                    print(f"Could not find a matching file type for {file_name}")

        print_with_delay("\nAll files have been organized successfully.", 3)

    def auto_rename(self):
        """
        Automatically renames all files in the target directory based on user input.
        Each file is renamed to the provided name followed by a unique number.
        """        
        if not self.has_files():
            print_with_delay("\nThere's no file to rename", 2)
            return

        file_name = self.ask_name()
        files = glob.glob(os.path.join(self.folder_path, "*"))
        files = sorted(files, key=os.path.getmtime)

        for i, file in enumerate(files):
            try:
                ext = os.path.splitext(file)[1]
                new_file_name = f"{file_name} - {i+1}{ext}"
                os.rename(file, os.path.join(self.folder_path, new_file_name))
                print(f"{file} have been renamed successfully", 0.2)
            except OSError:
                print_with_delay("Invalid operation!", 2)

        print_with_delay("\nAll files have been renamed successfully.", 3)

    def auto_delete(self):
        """
        Automatically deletes all temporary files in the target directory.
        A temporary file is defined as any file with "temp file" in its name.
        """        
        if not self.has_files():
            print_with_delay("\nThere's no file to delete.", 2)
            return

        files_to_delete = self.find_files_to_delete()
        self.delete_files(files_to_delete)

    def find_files_to_delete(self):
        """
        Finds all temporary files in the target directory.

        Returns:
            list: List of temporary files to delete.
        """        
        return [f for f in os.listdir(self.folder_path) if "temp file" in f.lower()]

    def delete_files(self, files_to_delete):
        """
        Deletes a list of files in the target directory.

        Args:
            files_to_delete (list): List of filenames to delete.
        """        
        files_deleted = 0

        for file_name in files_to_delete:
            os.remove(os.path.join(self.folder_path, file_name))
            files_deleted += 1
            print(f"{file_name} deleted successfully.", 0.2)

        print(f"\n{files_deleted} files deleted.", 0.2)
        print_with_delay("\nAll files have been deleted successfully.", 3)

