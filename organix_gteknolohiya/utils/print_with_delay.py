import time
from .text_to_speech import text_to_speech

def print_with_delay(message, delay_seconds):
    print(message)
    time.sleep(delay_seconds)
    text_to_speech(message)
