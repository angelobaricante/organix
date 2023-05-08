from gtts import gTTS
import os
from pygame import mixer
from pygame import time

def text_to_speech(message):
    """
    Converts the given text to speech and plays it using the system's audio player.

    Parameters:
    message (str): The text to be converted to speech.

    Returns:
    None

    This function uses the gTTS library to generate an MP3 file containing the speech for the given text message.
    It then uses the mixer module from the pygame library to play the MP3 file. After the speech is played, the
    MP3 file is deleted from the system.
    """
    tts_file = gTTS(text=message, lang='en', slow=False)
    tts_file.save("speech.mp3")
    
    mixer.init()
    mixer.music.load("speech.mp3")
    mixer.music.play()
    
    while mixer.music.get_busy():
        time.Clock().tick(10)
        
    mixer.quit()
    os.remove("speech.mp3")
