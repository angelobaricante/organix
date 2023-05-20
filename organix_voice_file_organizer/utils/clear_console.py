import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Call the function to clear the console
clear_console()
