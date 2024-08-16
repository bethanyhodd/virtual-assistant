import speech_recognition as sr

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 0.7
        audio = r.listen(source)

        try:
            print("Recognising")
            Query = r.recognize_google(audio, language='en-GB')
            print("the command is printed=", Query)
        except Exception as e:
            print(e)
            print("Please repeat")
            return "None"
        return Query