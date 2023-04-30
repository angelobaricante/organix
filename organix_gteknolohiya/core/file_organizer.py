import os
import shutil
import glob

from utils import ask_name, get_folder_path, print_with_delay

class FileOrganizer:
    def __init__(self):
        self.folder_path = get_folder_path()

    def auto_organize(self):
        file_types = {
            "audio": [".mp3", ".wav", ".flac", ".m4a", ".aac", ".ogg"],
            "documents": [".docx", ".pdf", ".odt"],
            "images": [".jpg", ".png", ".gif", ".bmp", ".svg"],
            "videos": [".mp4", ".avi", ".mov", ".wmv", ".mkv"],
            "archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
            "code": [".py", ".c", ".cpp", ".java", ".html", ".css", ".js"],
            "executables": [".exe", ".msi", ".apk", ".app"],
            "fonts": [".ttf", ".otf"],
            "presentations": [".ppt", ".pptx", ".key"],
            "spreadsheets": [".xls", ".xlsx", ".ods"],
            "text": [".doc", ".rtf", ".md", ".txt"],
            "web": [".url", ".htm", ".mht"],
            "torrents": [".torrent"]
        }

        # Check if there are any files in the folder
        if not any(os.path.isfile(os.path.join(self.folder_path, file_name)) for file_name in os.listdir(self.folder_path)):
            print_with_delay("\nThere's no file to organize.", 2)
            return  # Return early if no files found

        for folder_name in file_types:
            folder_path = os.path.join(self.folder_path, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

        for file_name in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, file_name)
            if os.path.isfile(file_path):
                file_extension = os.path.splitext(file_name)[1].lower()
                for file_type, extensions in file_types.items():
                    if file_extension in extensions:
                        destination_folder = os.path.join(self.folder_path, file_type)

                        shutil.move(file_path, destination_folder)
                        print_with_delay(f"Moved {file_name} to {destination_folder}", 0.2)
                        break
                else:
                    print_with_delay(f"Could not find a matching file type for {file_name}", 2)

        print_with_delay("\nAll files have been organized successfully.", 3)

        


    def auto_rename(self):
        # Check if there are any files in the folder
        if not any(os.path.isfile(os.path.join(self.folder_path, file_name)) for file_name in os.listdir(self.folder_path)):
            print_with_delay("\nThere's no file to rename", 2)
            return  # Return early if no files found

        file_name = ask_name()
        files = glob.glob(os.path.join(self.folder_path, "*"))
        files = sorted(files, key=os.path.getmtime)

        for i, file in enumerate(files):
            try:
                ext = os.path.splitext(file)[1]
                new_file_name = f"{file_name} - {i+1}{ext}"
                os.rename(file, os.path.join(self.folder_path, new_file_name))
                print_with_delay(f"{file} have been renamed successfully", 0.2)
            except OSError:
                print_with_delay("Invalid operation!", 2)

        print_with_delay("\nAll files have been renamed successfully.", 3)


    def auto_delete(self):
        # Check if there are any files in the folder
        if not any(os.path.isfile(os.path.join(self.folder_path, file_name)) for file_name in os.listdir(self.folder_path)):
            print_with_delay("There's no file to delete", 2)
            return  # Return early if no files found

        files_deleted = 0

        for file_name in os.listdir(self.folder_path):
            if "temp file" in file_name.lower():
                os.remove(os.path.join(self.folder_path, file_name))
                files_deleted += 1
                print_with_delay(f"{file_name} deleted successfully.", 0.2)

        print_with_delay(f"\n{files_deleted} files deleted.", 0.2)

        print_with_delay("\nAll files have been renamed successfully.", 3)

