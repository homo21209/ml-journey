from bs4 import BeautifulSoup
import requests

url = 'https://trends.rbc.ru/trends/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text,'html.parser')

    titles = soup.find_all('span',class_="item__title")

    for i,title_tag in enumerate(titles[:10],1):
        print(f'{i}. {title_tag.text.strip()}')
    
    else:
        print('ошибка загрузки',response.status_code)
