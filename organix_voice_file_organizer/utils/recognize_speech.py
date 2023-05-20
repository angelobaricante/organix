import speech_recognition as sr
from .print_with_delay import print_with_delay
from speech_recognition.exceptions import WaitTimeoutError

def recognize_speech():
    """
    Listens for and recognizes speech using a microphone as the source.

    This function adjusts for ambient noise, then continuously listens for speech
    until it successfully recognizes a phrase. Recognized speech is sent to Google's
    Speech Recognition service for conversion into text. 

    If the speech is successfully converted into text, it prints and vocalizes the phrase,
    then returns the text. If speech isn't detected within the timeout, it prompts the user 
    to try again. If the Speech Recognition service returns an error, it reports the error 
    and continues listening.

    Returns:
        text (str): The recognized text from speech. None if no speech is detected, or an error occurs.

    Raises:
        WaitTimeoutError: If no speech is detected within the specified timeout.
        sr.UnknownValueError: If the Speech Recognition service could not understand the audio.
        sr.RequestError: If the request to the Speech Recognition service failed.
    """    
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("\nSpeak now...")

        while True:
            try:
                audio = r.listen(source, timeout=1, phrase_time_limit=2)
            except WaitTimeoutError:
                print("No speech detected. Please try again.")
                continue

            try:
                text = r.recognize_google(audio, language='en-US')
                print_with_delay(f"\nYou said: {text}", 0.5)
                return text
            except sr.UnknownValueError:
                print("...")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service: {e}")
