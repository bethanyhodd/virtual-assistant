import datetime

from commands.speak import speak

def tell_time():
    time = str(datetime.datetime.now())
    print(time)

    hour = time[11:13]
    min = time[14:16]
    speak("The time is "+hour+" hours and "+min+" minutes")