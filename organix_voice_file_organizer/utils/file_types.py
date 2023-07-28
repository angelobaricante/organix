"""
file_types: A dictionary mapping different categories of file types to their corresponding file extensions.

Each key in the dictionary represents a specific category of file types (e.g. 'audio', 'documents', 'images' etc.)
and the value for each key is a list of file extensions related to that category.

Example:
{
    "audio": [".mp3", ".wav", ".flac", ...],
    "documents": [".docx", ".pdf", ".odt", ...],
    ...
}
"""

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
    "virtualization_files": [".vmx", ".vbox", ".ovf", ".ova", ".vagrant", ".vagrantfile"],
    "metatrader_files": [".ex4", ".ex5", ".mql4", ".mql5", ".set"]
}