import requests
from TTS import speak
import speech_recognition as sr

api_key = "661d81f3b17f7764fba64a3b2e0118db"
 
def weather(result):
    # Check if the user has provided a city name or not
    if 'location' in result['Entities']:
        city = result['Entities']['location']
    else:
        speak('What city')    
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.1)
            audio = recognizer.listen(source)
            ans = recognizer.recognize_google(audio)
        city = ans

    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city,api_key)
    response = requests.get(url)
    # get information from the response object and convert it to json format to be able to access the data
    x = response.json()
    
    if x["cod"] != "404":
        y = x["main"]
        z = x["weather"]
        # get the temperature in kelvin and convert it to celsius and weather description    
        max_temp = int(y["temp_max"] - 273.15)
        weather_describe = z[0]["description"]
        
        if 'weather_descriptor' in result['Entities']:
            description = result['Entities']['weather_descriptor']
            if description in weather_describe : 
                speak(f"Yes, weather is {weather_describe}")
            else :
                speak(f"No, weather is {weather_describe}")
        else :
            res = f"Currently in {city} it's {max_temp} degrees celsius with {weather_describe}"
            speak(res)
