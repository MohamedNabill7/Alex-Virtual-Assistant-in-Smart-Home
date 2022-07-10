from datetime import datetime
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from playsound import playsound
from pathlib import Path
import pytz
from TTS import speak


# Ask for Time
def timezone(result):
        # Get Time Zone of a Given Location 
        # The 'Timezonefinder' module is able to find the timezone of any point on earth (coordinates)
        # 'Geopy' makes it easy to locate the coordinates of addresses, cities, countries, and landmarks across the world
    if 'location' in result['Entities']:
        loca = result['Entities']['location']
        # initialize Nominatim API
        geolocator = Nominatim(user_agent="geoapiExercises")
        
        # getting Latitude and Longitude
        location = geolocator.geocode(loca) 
    
        # pass the Latitude and Longitude into a timezone_at and it return timezone
        obj = TimezoneFinder()
        res = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        # get current time
        current_time = datetime.now(pytz.timezone(res)).strftime("%H:%M:%S")
        # Convert 12 hour format
        hour = current_time[:2]
        minute = current_time[3:5]
        hour = int(hour) - 12 if 12 < int(hour) <= 24 else int(hour) 
        current_time = str(hour) + ':' + str(minute)
    else:
        # get current time without location
        current_time = datetime.now().strftime("%H:%M:%S")
        # Convert 12 hour format
        hour = current_time[:2]
        minute = current_time[3:5]
        hour = hour - 12 if 12 < hour <= 24 else hour 
        current_time = str(hour) + ':' + str(minute) 

    # speak current time
    return(speak("The Current Time is" + current_time))

    
# Ask for Date
def date(result):
    if 'date' in result['Entities']:
        date = result['Entities']['date']
        current_date = datetime.now().strftime("%d/%m/%Y")
    else:
        current_date = datetime.now().strftime("%d/%m/%Y")
    
    # speak current date
    return speak(current_date)
    

# Reminder
def alarm(result):
    alarm_time = ''
        
    if 'time' in result['Entities']:
        alarm_time += result['Entities']['time']

    alarm_hour , alarm_minute , alarm_period = int(alarm_time[:1]) , int(alarm_time[2:4]) , alarm_time[5:7].upper()
    alarm_hour = alarm_hour if alarm_period == 'AM' else alarm_hour + 12
        
    while True:
        now = datetime.now()

        if (alarm_period == now.strftime("%p") and 
            alarm_hour == now.hour and 
            alarm_minute == now.minute ):

            playsound("alarm.mp3")
            break


def reminder(result):
    # Reminder functoin that takes event name and time as input
    # date as input and returns a reminder message
    # for the event on the date     

    # Ask for event name
    speak("What do you want to remind me of?")
    event = input("What do you want to remind me of?\n")
    # Ask for date
    speak("What date do you want to set the reminder for?")
    date = input("What date do you want to set the reminder for?\n")
    # Ask for time
    speak("What time do you want to set the reminder for?")
    time = input("What time do you want to set the reminder for?\n")
    # Ask for period
    speak("What period do you want to set the reminder for?")
    period = input("What period do you want to set the reminder for?\n")
    # Ask for description 
    speak("What description do you want to set the reminder for?")
    description = input("What description do you want to set the reminder for?\n")
    # Ask for confirmation
    speak("Do you want to set the reminder for " + event + " on " + date + " at " + time + " " + period + " " + " " + description + "?")
    confirmation = input("Do you want to set the reminder for " + event + " on " + date + " at " + time + " " + period + " " + " " + description + "?\n")
    # Confirm the reminder
    if confirmation == 'yes':
        speak("Reminder set for " + event + " on " + date + " at " + time + " " + period + " "  + " " + description)
        print("Reminder set for " + event + " on " + date + " at " + time + " " + period + " "  + " " + description)
    else:
        speak("Reminder not set")
        print("Reminder not set")
    # Ask for another reminder
    speak("Do you want to set another reminder?")
    another_reminder = input("Do you want to set another reminder?\n")
    if another_reminder == 'yes':
        reminder()
    else:
        speak("Thank you for using the reminder service")
        print("Thank you for using the reminder service")


def productivity(result):
    text = result['Text']
    if 'time' in text:
        res = timezone(result)
    elif 'date' in text:
        res = date(result)
    elif 'alarm' in text:
        res = alarm(result)
    return res