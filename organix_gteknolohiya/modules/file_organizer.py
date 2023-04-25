import os
import shutil
import glob

from utils import ask_name

class FileOrganizer:
    def __init__(self, folder_path):
        self.folder_path = folder_path
    
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

        for folder_name in file_types:
            folder_path = os.path.join(self.folder_path, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

        for filename in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, filename)
            if os.path.isfile(file_path):
                file_extension = os.path.splitext(filename)[1].lower()
                for file_type, extensions in file_types.items():
                    if file_extension in extensions:
                        destination_folder = os.path.join(self.folder_path, file_type)

                        shutil.move(file_path, destination_folder)
                        print(f"Moved {filename} to {destination_folder}")
                        break
                else:
                    print(f"Could not find a matching file type for {filename}")

    def auto_rename(self):
        file_name = ask_name()

        files = glob.glob(os.path.join(self.folder_path, "*"))
        files = sorted(files, key=os.path.getmtime)

        for i, file in enumerate(files):
            try:
                ext = os.path.splitext(file)[1]
                new_file_name = f"{file_name} - {i+1}{ext}"
                os.rename(file, os.path.join(self.folder_path, new_file_name))
            except OSError:
                print("Invalid operation!")

    def auto_delete(self):
        files_deleted = 0

        for filename in os.listdir(self.folder_path):
            if "temp file" in filename.lower():
                os.remove(os.path.join(self.folder_path, filename))
                files_deleted += 1
                print(f"{filename} deleted successfully.")

        print(f"{files_deleted} files deleted.")
