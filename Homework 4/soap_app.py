import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

data = []
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}


def parse(url):
    page = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    for product in soup.find_all('div', class_='catalogue-product'):
        title = product.find('h4', class_='_name')
        price = product.find('span', class_='price-html')
        picture = product.find('img')

        data.append({'title': title.text.strip() if title else None,
                     'price': price.text.strip() if price else None,
                     'picture': picture['src'] if picture else None})

    next_page = soup.find('button', class_='-right').a

    if next_page:
        parse(urljoin('https://arvutitark.ee', next_page['href']))


if __name__ == '__main__':
    parse('https://arvutitark.ee/arvutid-ja-lisad/heliseadmed/mikrofonid')

    with open('soap_data.json', 'w', encoding='utf8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
