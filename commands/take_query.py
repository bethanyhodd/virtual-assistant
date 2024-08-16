import webbrowser
import wikipedia

from commands.hello import hello
from commands.speak import speak
from commands.take_command import take_command
from commands.tell_day import tell_day
from commands.tell_time import tell_time

def take_query():
    hello()
    while(True):
        query = take_command().lower()

        if "open google" in query:
            speak("Opening Google")
            webbrowser.open("www.google.com")
            continue
        elif "what day is it" in query:
            tell_day()
            continue
        elif "what time is it" in query:
            tell_time()
            continue
        elif "bye" in query:
            speak("Goodbye")
            exit()
        elif "from wikipedia" in query:
            query = query.replace("from wikipedia", "")
            speak("Checking wikipedia for "+query)
            
            result = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            speak(result)
            continue
        elif "your name" in query:
            speak("I am Alexis, your desktop assistant")
            continue

            


