from .clear_console import clear_console
from .text_to_speech import text_to_speech

def clc_print(message):
    clear_console()
    print(message)  
    text_to_speech(message)
