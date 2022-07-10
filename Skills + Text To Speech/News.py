import requests
from bs4 import BeautifulSoup
import time
from TTS import speak

"""
Topics => [Sport , Science , Technology , Business , Climate , Health , News around the World]
There are three cases:
   - If None Entities =>>>
         By default show the News
   - Entities =>>>
         If the topic is not [Sport or Science or Climate] take the topic and show its news
         Else topic is [Sport or Science or Climate] change URL
"""
# Define the function to fetch the news from the BBC website and return the news 
def fetch_news(topic=None):
    if topic == None:
        url = 'https://www.bbc.com/news/'
    else :
        url = 'https://www.bbc.com/news/{}'.format(topic)
            
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    titles = soup.find('body').find_all('h3')
    summaries = soup.find('body').find_all('p')
    
    # Title & Summary        
    for i in range(2):
        title = list(dict.fromkeys(titles))[i].text.strip()
        summary = list(dict.fromkeys(summaries))[i+1].text.strip()

        speak('the title is '+ title)
        time.sleep(3)
        speak('the sammary of this' + summary)
        time.sleep(7)
# Define the function to fetch the news from the BBC website and return the news based on the region like [Africa , Aisa , Europe]
def fetch_news_by_region(region):
    
    url = 'https://www.bbc.com/news/world/{}'.format(region)        
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    titles = soup.find('body').find_all('h3')
    summaries = soup.find('body').find_all('p')
    
    # Title & Summary        
    for i in range(2):
        title = list(dict.fromkeys(titles))[i].text.strip()
        summary = list(dict.fromkeys(summaries))[i+1].text.strip()

        speak('the title is '+ title)
        time.sleep(3)
        speak('the sammary of this' + summary)
        time.sleep(7)
        
        
def fetch_sports_news():
    
    url = 'https://www.bbc.com/sport/'        
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    titles = soup.find('body').find_all('h3')
    summaries = soup.find('body').find_all('p')
    
    # Title & Summary        
    for i in range(2):
        title = list(dict.fromkeys(titles))[i].text.strip()
        summary = list(dict.fromkeys(summaries))[i].text.strip()

        speak('the title is '+ title)
        time.sleep(3)
        speak('the sammary of this' + summary)
        time.sleep(7)

# Final Function to fetch the news from the BBC website and return the news based on the topic like [Sport , Science , Technology , Business , Climate , Health , News around the World]
def news(result):

    dict_news = {'science':fetch_news('science_and_environment'),
                 'climate':fetch_news('science-environment-56837908'),
                 'sports':fetch_sports_news(),
                 'sport' :fetch_sports_news()}
                
    if result['Entities'] == None:
        output = fetch_news()
        
    else:
        if result['Entities']['region'] != None:
            output = fetch_news_by_region(result['Entities']['region'])
        
        elif result['Entities']['topic'] in dict_news.keys():
            output = dict_news(result['Entities']['topic'])
    
        else:
            output = fetch_news(result['Entities']['topic'])
            
    return output
    