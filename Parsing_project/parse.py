import re  # Модуль для регулярных выражений (поиск чисел или слов)
import csv # Модуль для записи в CSV файл
import requests # Библиотека для скачивания веб-страницы
from bs4 import BeautifulSoup # Библиотека для разбора HTML

URL = "https://mashina.kg/search/passenger" # Страница которую будем парсить
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "ru-RU,ru;q=0.9,en;q=0.8",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
} # Предсьтавляемся браузером чтобы сайт
# не отклонил наш запрос

def get_html(url: str):
    response = requests.get(url=url, headers=HEADERS)
    # Отправили GET- запрос на сайт, и передали заголовки для получения HTML
    response.raise_for_status()
    print(response)
    return response.text

def parse_listings(html):
    soup = BeautifulSoup(html, 'html.parser')
    cards = soup.select('a[href^="/details/"]')
    
    listings = [] # Сюда будем закидывать данные по каждой машине 
    # в виде словаря 
    seen_urls = set()
    for card in cards:
        href = card.get("href") # Достаем саму ссылку
        
        if href in seen_urls:
            continue
        seen_urls.add(href)
        
        text = card.get_text(" ", strip=True)
        title_tag = card.find("img")
        if title_tag and title_tag.get("alt"):
            title = title_tag['alt'].strip()
        else:
            title = None
        
        price_match = re.search(r'\$\s*(\d[\d\s]*)', text)
        if price_match:
            price_usd = price_match.group(1)
            price_usd = price_usd.replace("\xa0", "")
            price_usd = int(price_usd)
        else:
            price_usd = None
            
        year_match = re.search(r'((?:19|20)\d{2})', text)
        year = int(year_match.group(1)) if year_match else None
        
        
        millage_match = re.search(r'(\d[\d\s]*)\s*km', text)
        if millage_match:
            millage_km = millage_match.group(1).replace("\xa0", '')
            millage_km = int(millage_km)
        else:
            millage_km = None
            
        city_match = re.search(r'г\.\s*([А-Яа-яЁё\-]+)', text)
        city = city_match.group(1) if city_match else None
        
        car_data = {
            "title": title,
            "price_usd": price_usd,
            "year": year,
            "millage_km": millage_km,
            "city": city,
            "url": "https://mashina.kg/" + href
        }
        listings.append(car_data)
    return listings
        

def save_to_csv(listings, file_name='cars.csv'):
    if not listings:
        print("Нечего сохранять")
        return None
    with open(file_name, "w", newline="", encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=listings[0].keys())
        writer.writeheader()
        writer.writerows(listings)
        

if __name__ == "__main__":
    html = get_html(URL)
    listings = parse_listings(html)
    save_to_csv(listings)
    print("Все спарсили")