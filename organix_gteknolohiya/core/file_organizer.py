import os
import shutil
import glob

from utils import ask_name, get_folder_path, print_with_delay
class FileOrganizer:
    file_types = {
        "audio": [".mp3", ".wav", ".flac", ".m4a", ".aac", ".ogg", ".wma", ".aiff", ".amr", ".m4b", ".m4p", ".midi", ".opus"],
        "documents": [".docx", ".pdf", ".odt", ".doc", ".xls", ".xlsx", ".ods", ".ppt", ".pptx", ".odp", ".rtf", ".txt", ".md", ".csv", ".tex", ".epub", ".mobi", ".azw3"],
        "images": [".jpg", ".png", ".gif", ".bmp", ".svg", ".tiff", ".ico", ".webp", ".heif", ".psd", ".ai", ".xcf", ".indd", ".raw", ".cr2", ".nef", ".orf", ".sr2", ".kdc"],
        "videos": [".mp4", ".avi", ".mov", ".wmv", ".mkv", ".flv", ".webm", ".m4v", ".vob", ".ogv", ".mpeg", ".mpg", ".mts", ".m2ts", ".m2v", ".3gp", ".swf"],
        "archives": [".zip", ".rar", ".tar", ".gz", ".7z", ".bz2", ".xz", ".iso", ".cab", ".z", ".lz", ".lzma", ".lzh", ".s7z", ".apk"],
        "code": [".py", ".c", ".cpp", ".java", ".html", ".css", ".js", ".php", ".go", ".rb", ".swift", ".cs", ".sh", ".bat", ".pl", ".r", ".rs", ".m", ".kt", ".ts", ".sql", ".lua", ".pas", ".asm", ".s", ".vbs", ".vb", ".json", ".xml", ".yml", ".yaml", ".ini", ".conf", ".config", ".reg", ".properties", ".xhtml", ".dtd", ".asc", ".scss", ".sass", ".less", ".h", ".hpp", ".hxx", ".hh", ".scala", ".sbt", ".hs", ".elm", ".clj", ".cljs", ".edn", ".groovy", ".gradle", ".mjs", ".fs", ".fsx", ".fsi", ".v", ".sv"],
        "executables": [".exe", ".msi", ".apk", ".app", ".bat", ".bin", ".cgi", ".com", ".gadget", ".jar", ".pif", ".vb", ".wsf"],
        "fonts": [".ttf", ".otf", ".woff", ".woff2", ".eot", ".fon", ".pfa", ".pfb", ".sfd"],
        "presentations": [".ppt", ".pptx", ".key", ".odp"],
        "spreadsheets": [".xls", ".xlsx", ".ods", ".csv"],
        "text": [".doc", ".rtf", ".md", ".txt", ".log", ".tex", ".me", ".1st", ".ans", ".asc", ".ascii", ".diz", ".nfo", ".now", ".srt", ".sub"],
        "web": [".url", ".htm", ".html", ".xhtml", ".php", ".asp", ".aspx", ".jsp", ".jspx", ".jsf", ".jspx", ".cgi", ".pl", ".shtml", ".mhtml", ".mht", ".dhtml"],
        "torrents": [".torrent"],
        "ebooks": [".epub", ".mobi", ".azw", ".azw3", ".ibooks"],
        "3d_models": [".obj", ".fbx", ".dae", ".3ds", ".blend", ".stl", ".step", ".iges", ".ply", ".x3d"],
        "vector_graphics": [".svg", ".ai", ".eps", ".cdr"],
        "design_files": [".psd", ".xd", ".sketch", ".fig", ".affinity", ".dwg"],
        "database_files": [".db", ".sql", ".sqlite", ".sqlite3", ".dbf", ".mdb", ".accdb", ".myd", ".myi", ".frm", ".ibd", ".mdf", ".ndf", ".ldf", ".bak"],
        "gis_files": [".shp", ".shx", ".dbf", ".prj", ".sbn", ".sbx", ".cpg", ".gpx", ".kml", ".kmz", ".geojson", ".gdb", ".tab", ".mapinfo", ".mif", ".mff", ".tif", ".tiff", ".tfw"],
        "disk_images": [".iso", ".img", ".vdi", ".vhd", ".vhdx", ".vmdk"],
        "compressed_files": [".lzh", ".lha", ".sit", ".sitx", ".sea", ".dmg", ".pkg", ".rpm", ".deb", ".arj", ".zoo", ".cpio", ".shar", ".rsrc"],
        "virtualization_files": [".vmx", ".vbox", ".ovf", ".ova", ".vagrant", ".vagrantfile"]
    }

    def __init__(self):
        """
        Initializes a new instance of the FileOrganizer class.
    
        The constructor gets the folder path from the user, and stores it as an instance variable 
        named folder_path.
        """
        self.folder_path = get_folder_path()

    def has_files(self):
        """
        Check if the folder has any files.

        Returns:
            bool: True if there is at least one file in the folder, False otherwise.
        """
        return any(os.path.isfile(os.path.join(self.folder_path, file_name)) for file_name in os.listdir(self.folder_path))

    def find_files_by_extension(self, extensions):
        """
        Finds all files in the folder with the given extensions.

        Args:
            extensions (list): A list of file extensions to search for. Each extension should be a string 
            starting with a period (e.g. '.txt', '.pdf').

        Returns:
            list: A list of file names (strings) with the given extensions.
        """
        return [f for f in os.listdir(self.folder_path) if os.path.splitext(f)[1].lower() in extensions]

    def auto_organize(self):
        """
        Automatically organizes files in the designated folder based on their file type.

        If there are no files in the folder, a message is printed stating there are no files to organize.

        For each file in the folder, the file type is determined by its file extension. The file is then moved
        to a destination folder based on its file type. If the destination folder does not exist, it is created.
        If a file with the same name already exists in the destination folder, the file name is modified to
        avoid overwriting the existing file.

        If a file type cannot be determined based on its file extension, a message is printed stating that
        a matching file type could not be found.

        After all files have been processed, a message is printed stating that all files have been organized
        successfully.
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
                        print_with_delay(f"Moved {file_name} to {destination_file_path}", 0.2)
                        break
                else:
                    print_with_delay(f"Could not find a matching file type for {file_name}", 2)

        print_with_delay("\nAll files have been organized successfully.", 3)

    def auto_rename(self):
        """
        Renames all files in the folder with a given name and adds a numbering suffix.
        """
        if not self.has_files():
            print_with_delay("\nThere's no file to rename", 2)
            return

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
        """
        Automatically deletes all the empty folders in the given folder_path.

        Returns:
            None
        """
        if not self.has_files():
            print_with_delay("\nThere's no file to delete.", 2)
            return

        files_to_delete = self.find_files_to_delete()
        self.delete_files(files_to_delete)

    def find_files_to_delete(self):
        """
        Finds all files in the current folder that contain "temp file" in their name.
    
        Returns:
            A list of file names to be deleted.
        """
        return [f for f in os.listdir(self.folder_path) if "temp file" in f.lower()]

    def delete_files(self, files_to_delete):
        """
        Deletes the specified files in the folder.

        Args:
            files_to_delete (list): A list of file names to be deleted.

        Returns:
            None
        """
        files_deleted = 0

        for file_name in files_to_delete:
            os.remove(os.path.join(self.folder_path, file_name))
            files_deleted += 1
            print_with_delay(f"{file_name} deleted successfully.", 0.2)

        print_with_delay(f"\n{files_deleted} files deleted.", 0.2)
        print_with_delay("\nAll files have been deleted successfully.", 3)

