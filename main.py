import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.imdb.com/list/ls003992425/')

soup = BeautifulSoup(r.content, 'html.parser')

film_headers = soup.find_all('h3', class_='lister-item-header')

film = []

for header in film_headers:
    film_title = header.find('a').text.strip()
    film.append(film_title)

print(film[:])
