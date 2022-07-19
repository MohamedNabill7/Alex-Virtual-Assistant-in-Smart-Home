import speech_recognition as sr
import requests , json , re , pygame
from Skills import Weather , News , IOT , Kitchen , Enterainment , Social , Productivity 

mapping={
        'Greeting'      : Social.Social,
        'Goodbye'       : Social.Social,
        'Thanks'        : Social.Social,
        'Joke'          : Enterainment.joke,
        'PlayMusic'     : Enterainment.play_music,
        'Cooking'       : Kitchen.cooking,
        'Weather'       : Weather.weather,
        'News'          : News.news,
        'Iot'           : IOT.smartHome,
        'Datetime'      : Productivity.productivity,
        'Reminder'      : Productivity.productivity
        } 
# Create an indicator to make attention to the user for speaking
pygame.init()
sound = pygame.mixer.Sound('Skills\indicator.mp3')
sound.play()

while True:
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        try :
            recognizer.pause_threshold = .8
            audio = recognizer.listen(source)
            sentence = recognizer.recognize_google(audio)
            if 'alex' in sentence.lower():  
                message = re.match('(.*)alex(.*)',sentence.lower()).group(2)
                message = message.strip()
                response = requests.post(f'http://127.0.0.1:8000/predict?message={message}').json()
                mapping[response['intent']](message)     
            else:
                continue 
        except:
            continue 
    
