from bs4 import BeautifulSoup
import requests
import json

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
    urls = [
        "https://aifindy.com/directorio-en-lista/chatgpt",
        "https://aifindy.com/directorio-en-lista/dall-e-2",
        "https://aifindy.com/directorio-en-lista/ai-art-apps",
        "https://aifindy.com/directorio-en-lista/copymatic",
        "https://aifindy.com/directorio-en-lista/2shortai",
        "https://aifindy.com/directorio-en-lista/synthesia",
        "https://aifindy.com/directorio-en-lista/ai-careers",
        "https://aifindy.com/directorio-en-lista/runwayml",
        "https://aifindy.com/directorio-en-lista/contentfries",
        "https://aifindy.com/directorio-en-lista/adcreativeai",
        "https://aifindy.com/directorio-en-lista/humata-ai",
        "https://aifindy.com/directorio-en-lista/rytr",
        "https://aifindy.com/directorio-en-lista/eightify",
        "https://aifindy.com/directorio-en-lista/sheet-ai",
    ]
    for url in urls:
        soup = create_soup_from_url(url)
        
        name = {"name": soup.find('h1', class_='notion-header__title').text}
        description = {"description": soup.find('div', class_='notion-callout').find('span', class_='notion-semantic-string').text}
        link = {"website_url": soup.find('a', class_='notion-link link').get('href')}
        
        properties = soup.find_all('span', class_='notion-pill')
        properties_list = [tag.get_text() for tag in properties]
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