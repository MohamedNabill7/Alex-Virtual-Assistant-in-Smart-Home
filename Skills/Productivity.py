from datetime import datetime
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from playsound import playsound
from pathlib import Path
import pytz
from TTS import speak

# Ask for Time
def timezone(result):
    if 'location' in result['Entities']:
        loca = result['Entities']['location']
        geolocator = Nominatim(user_agent="geoapiExercises")    
        # getting Latitude and Longitude
        location = geolocator.geocode(loca) 
        obj = TimezoneFinder()
        res = obj.timezone_at(lng=location.longitude, lat=location.latitude)
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

def productivity(result):
    text = result['Text']
    if 'time' in text:
        res = timezone(result)
    elif 'date' in text:
        res = date(result)
    elif 'alarm' in text:
        res = alarm(result)
    return res