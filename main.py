import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

book_containers = soup.find_all('article', class_='product_pod')

for container in book_containers:
    title = container.h3.a.text
    price = container.find('div', class_='product_price')
    print(title, price)