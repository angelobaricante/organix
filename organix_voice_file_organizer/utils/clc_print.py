import os

from .text_to_speech import text_to_speech

def clc_print(message):
    """
    Clears the console, prints a given message, and uses text-to-speech to read the message.

    Parameters
    ----------
    message : str
        The message to be printed and read.
    """    
    os.system('cls' if os.name == 'nt' else 'clear')

    print(message)  
    text_to_speech(message)
