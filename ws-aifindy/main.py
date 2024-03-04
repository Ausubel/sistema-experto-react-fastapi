from bs4 import BeautifulSoup
import requests
import json
import numpy as np

def create_soup_from_url(url) -> BeautifulSoup:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def create_json_entries(entries):
    with open('entries.json', 'w', encoding="utf-8") as file:
        json.dump(entries, file, indent=2, ensure_ascii=False)
        file.close()


    
def run():
    entries = []
    urls = []
    with open('data_ais_urls.json', 'r') as file:
        urls = json.load(file)
        file.close()

    
    for url in urls:
        soup = create_soup_from_url(url)
        
        name = {"name": soup.find('h1', class_='notion-header__title').text}
        description = {"description": soup.find('div', class_='notion-callout').find('span', class_='notion-semantic-string').text}
        link = {"website_url": soup.find('a', class_='notion-link link').get('href')}
        
        properties = soup.find_all('span', class_='notion-pill')
        properties_list = [tag.get_text() for tag in properties]
        # elimina duplicados
        np_properties_list = np.array(properties_list)
        np_properties_list = np.unique(np_properties_list)
        properties_list = np_properties_list.tolist()
        props = {"props": properties_list}
        
        link_image = {"image_url": str(soup.find('img')).split('src="')[1].split('"')[0]}

        
        try:
            price = {"price": "Desde " + soup.find('div', class_='notion-property__number').find('span', class_='notion-semantic-string').text}
        except:
            if(properties_list[0] == "Gratis"):
                price = {"price": "$0.00"}
            else:
                price = {"price": "No disponible"}
        
        entry = {**name, **description, **price, **link, **link_image, **props}
        entries.append(entry)
    create_json_entries(entries)


if __name__=='__main__':
    run()