import time
from .text_to_speech import text_to_speech

def print_with_delay(message, delay_seconds):
    """
    Prints a message to the console, waits for a specified delay, and then speaks the message using text-to-speech.

    This function first prints the given message to the console, then waits for a delay (specified in seconds),
    and finally calls the `text_to_speech` function to vocalize the message.

    Args:
        message (str): The message to be printed and spoken.
        delay_seconds (float): The delay in seconds before the message is spoken.

    Note: 
        The `text_to_speech` function should be present in the same module or be properly imported.
    """
    print(message)
    time.sleep(delay_seconds)
    text_to_speech(message)
