import requests
import pyjokes
import pywhatkit
from TTS import speak

# Jokes
def joke(result):
    if result['Intent'] == 'Joke':
    
        res = requests.get('https://icanhazdadjoke.com/',headers={"Accept":"text/plain"})
    
        if res.status_code == 200:
            print(res.text)
            
        speak(res.text)

# Play Music
def play_music(result):
    if result['Intent'] == 'PlayMusic':
        
        if 'song_name' in result['Entities']:
            song = result['Entities']['song_name']
        
        elif 'artist' in result['Entities']:
            song = result['Entities']['artist']
            
        elif 'music_genre'in result['Entities']:
            song = result['Entities']['music_genre']
        
    pywhatkit.playonyt(song)
    
# Play Podcast
def play_podcast(result):
    return None

