from gtts import gTTS
import os
from pygame import mixer
from pygame import time

def text_to_speech(message):
    """
    Converts a text message to speech and plays it.

    This function uses Google Text-to-Speech (gTTS) to convert the provided message 
    into speech. The speech is saved as an MP3 file, which is then loaded and played 
    using Pygame's mixer module. After the speech is played, the MP3 file is deleted.

    Args:
        message (str): The text message to be converted into speech.

    Note: 
        This function requires gTTS and pygame to be installed and correctly imported. 
        Also, it temporarily creates an MP3 file named "speech.mp3" in the current working directory.
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
