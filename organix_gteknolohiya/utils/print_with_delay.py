import time
from .text_to_speech import text_to_speech

def print_with_delay(message, delay_seconds):
    """
    Prints a message to the console and then waits for a specified delay before
    using text-to-speech to read the message aloud.

    Args:
        message (str): The message to print and read aloud.
        delay_seconds (float): The number of seconds to wait before reading the
                               message aloud.

    Returns:
        None
    """
    print(message)
    time.sleep(delay_seconds)
    text_to_speech(message)
