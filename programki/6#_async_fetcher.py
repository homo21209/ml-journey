import asyncio
import aiohttp
from bs4 import BeautifulSoup

async def fetch_titles():
    url = "https://trends.rbc.ru/trends/"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                html = await response.text()
                soup = BeautifulSoup(html, "html.parser")
                titles = soup.find_all('span',class_='item__title')
                for i,tag in enumerate(titles[:10],1):
                    print(f"{i}. {tag.text.strip()}")
            else:
                print("Ошибка:", response.status)

# Запуск
asyncio.run(fetch_titles())
