import speech_recognition as sr
from .print_with_delay import print_with_delay
from speech_recognition.exceptions import WaitTimeoutError

def recognize_speech():
    """
    Uses the SpeechRecognition library to recognize speech input from the user's
    microphone.

    Returns:
        A string containing the recognized text.
    """
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("\nSpeak now...")

        while True:
            try:
                audio = r.listen(source, timeout=2, phrase_time_limit=3)
            except WaitTimeoutError:
                print("No speech detected. Please try again.")
                continue

            try:
                text = r.recognize_google(audio, language='en-US')
                print_with_delay(f"\nYou said: {text}", 0.5)
                return text
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service: {e}")
    
