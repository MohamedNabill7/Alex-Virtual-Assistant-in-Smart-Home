from TTS import speak
import speech_recognition as sr
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
 

cred = credentials.Certificate('serviceAccount.json')
firebase_admin.initialize_app(cred ,{'databaseURL': 'https://smart-home-2f967-default-rtdb.firebaseio.com/'})
ref = db.reference('/')
users_ref= ref.child('HOME01')


"""
Actions => [On , Off , Down , Up , Dim , Open , Close , Medium , Low , High]
Rooms   => [Living room , Bedroom , Bathroom , Kitchen , Garage , Reception]
Devices => [Light , Heating , Curtain , Window , Door , Fan]
"""


# Ask about a room if the user doesn't mention it
def is_room(result):
    if 'room' not in result['Entities'] :
        speak('What is the room')    
        
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.1)
            audio = recognizer.listen(source)
            ans = recognizer.recognize_google(audio)
            
        room = ans
    else:    
        room = result['Entities']['room']
        
    return room

# Take a result "Entities" and execute an action
# If an action is equal one of those [On , Open , Up]
def device_1(result):
    device = result['Entities']['device']
    room = is_room(result)
    action = result['Entities']['action']

    speak(f"ok,the {device} is {action}")

    return users_ref.update({'{}/{}/{}'.format(room,'on-off',device): 1})

# If an action is equal one of those [Off , Dim , Down , Close]
def device_0(result):
    device = result['Entities']['device']
    room = is_room(result)
    action = result['Entities']['action']

    speak(f"ok,the {device} is {action}")

    return users_ref.update({'{}/{}/{}'.format(room,'on-off',device): 0})

# Final function that identifies a device and an action     
def smartHome(result):   
    device = result['Entities']['device']
    action = result['Entities']['action']

    # Map every device to its action function 
    map_0 = {
        'light'   : device_0,
        'fan'     : device_0,
        'window'  : device_0,
        'heating' : device_0,
        'heater'  : device_0, 
        'curtain' : device_0,
        'door'    : users_ref.update({'door':0})
            }  

    map_1 = {
        'light'   : device_1,
        'fan'     : device_1,
        'window'  : device_1,
        'heating' : device_1,
        'heater'  : device_1,
        'curtain' : device_1,
        'door'    : users_ref.update({'door':0})
            } 
    
    
    if action in ['on','up','open']:
        if device in map_1.keys():
            res =  map_1[device](result)
            
    elif action in ['low','medium','high']:
        if 'light' in device:
            res = users_ref.update({f'bedroom/light/mode':{action}})

    elif action in ['off','dim','down','close']:
        if device in map_0.keys():
            res =  map_0[device](result)

    return res
   

print(smartHome({'Entities': {'action': 'off', 'device': 'fan', 'room': 'living room'}}))