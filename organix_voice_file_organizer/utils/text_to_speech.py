from gtts import gTTS
import os
from pygame import mixer
from pygame import time

def text_to_speech(message):
    tts_file = gTTS(text=message, lang='en', slow=False)
    tts_file.save("speech.mp3")
    
    mixer.init()
    mixer.music.load("speech.mp3")
    mixer.music.play()
    
    while mixer.music.get_busy():
        time.Clock().tick(10)
        
    mixer.quit()
    os.remove("speech.mp3")
