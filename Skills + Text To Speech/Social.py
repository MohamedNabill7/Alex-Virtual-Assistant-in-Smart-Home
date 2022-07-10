import random
from TTS import speak

# Greeting 
def greet():
    responses = [ "Good to see you again", "it's good to see you" ,
                  "Hi there, how can I help?" , "hey how can I help you?" ,
                  "hi what's going on"]
    res = random.choice(responses)
    return speak(res)

# Goodbye
def goodbye():
    responses = ["See you", "Have a nice day", "Bye Come back again soon." ,
                 "Bye Take care" , "Bye See you soon",
                 "Bye Have a nice day" , "Bye See you later"]
    res = random.choice(responses)   
    return speak(res)

# Thanks
def thank():
    responses = ["Happy to help", "Any time", "My pleasure" ,
                 "No problem" ,"You're welcome"]
    res = random.choice(responses) 
    return speak(res)

# Call the right function based on the intent
def Social(result):
 
    if result['Intent'] == 'Greeting':
        res = greet()
    elif result['Intent'] == 'Goodbye':
        res = goodbye()
    elif result['Intent'] == 'Thanks':
        res = thank()
    else:
        res = None
    
    return res

