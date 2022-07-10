from bs4 import BeautifulSoup
import requests
import time
from TTS import speak


    
def cooking(result):
    if 'food' in result['Entities']:
        food_type = result['Entities']['food']
       
    link = f'https://www.allrecipes.com/search/results/?search={food_type}'
    response = requests.get(link).text
    soup = BeautifulSoup(response , 'lxml')

    contents = soup.find_all('div',class_="component card card__recipe card__facetedSearchResult")
    
    links = []
    for content in contents[:1]:
        link = content.find('a',class_="card__titleLink manual-link-behavior elementFont__titleLink margin-8-bottom")['href']
        links.append(link)

    for link in links:
        response = requests.get(link).text
        soup = BeautifulSoup(response , 'lxml')
        recipes = soup.find_all('div',class_="docked-sharebar-content-container")

        for recipe in recipes:
            ingrdients = recipe.find_all('span',class_="ingredients-item-name")

            speak('Start recipe')
            time.sleep(1)
            for ingrdient in ingrdients:
                print(ingrdient.text)
                speak(ingrdient.text)
                time.sleep(2.5)
        
            steps = recipe.find_all('span',class_="checkbox-list-text")
            paragraph = recipe.find_all('div',class_="paragraph")
            
            speak('Start steps')
            time.sleep(1)
            for i in range(len(steps)):
                if len(paragraph[i].text) > 15:
                    speak(steps[i].text)                
                    time.sleep(1)
                    speak(paragraph[i].text)
                    time.sleep(7)
                else:
                    speak(steps[i].text)                
                    time.sleep(1)
                    speak(paragraph[i].text)
                    time.sleep(3)
