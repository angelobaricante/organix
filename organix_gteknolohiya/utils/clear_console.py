import os

def clear_console():
    """
    Clears the console screen.

    This function uses the 'os' module to check the operating system and clear the console screen accordingly.

    """
    os.system('cls' if os.name == 'nt' else 'clear')

# Call the function to clear the console
clear_console()
