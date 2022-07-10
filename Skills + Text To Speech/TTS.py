from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import pygame as pg
import os


# Authentication
url = "https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/7eb7a571-08b6-4fb9-acbd-b7dfd5f3002c"
apikey = "U4O0CsB5mN_yXkgzYG6LHfQINK4Gh92jWojNCxXLjlPp"

#setup service
authenticator = IAMAuthenticator(apikey)
#new TTS service
tts = TextToSpeechV1(authenticator=authenticator)
#set service URL
tts.set_service_url(url)

num = 0
def speak(output):
    global num
    # num to rename every audio file with different name to remove ambiguity
    num += 1
    
    file = str(num)+'.mp3'
    with open(file, 'wb') as audio_file:
        res = tts.synthesize(output, accept='audio/mp3', voice='en-US_MichaelV3Voice').get_result()
        audio_file.write(res.content)    
        
    # for playing note.mp3 file
    pg.mixer.init()
    sound = pg.mixer.Sound(file)
    sound.play()
    
    while pg.mixer.get_busy():
        pg.time.delay(100)

    os.remove(file)          
   