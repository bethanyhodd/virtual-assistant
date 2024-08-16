import datetime

from commands.speak import speak

def tell_day():
    day = datetime.datetime.today().weekday() + 1

    day_dict = {1: 'Monday', 2: 'Tuesday', 
                3: 'Wednesday', 4: 'Thursday', 
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
    
    if day in day_dict.keys():
        day_of_the_week = day_dict[day]
        print(day_of_the_week)
        speak("It is "+day_of_the_week+" today")