import speech_recognition as sr

def recognize_speech(message):
    # initialize the recognizer
    r = sr.Recognizer()
    
    # set the microphone as audio source
    with sr.Microphone() as source:
        # adjust for ambient noise
        r.adjust_for_ambient_noise(source)
        print(message)
        print("Speak now...")
        # continuously listen for audio and recognize speech
        while True:
            audio = r.listen(source)
            # recognize speech using Google Speech Recognition
            try:
                text = r.recognize_google(audio, language='en-US')
                print(f"You said: {text}")
                return text
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service: {e}")



