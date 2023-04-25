import speech_recognition as sr

def recognize_speech():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Speak now...")

        while True:
            audio = r.listen(source)

            try:
                text = r.recognize_google(audio, language='en-US')
                print(f"You said: {text}")
                return text
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service: {e}")



