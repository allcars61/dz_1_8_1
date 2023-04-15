# Задача №1
# Кто самый умный супергерой?
# Есть API по информации о супергероях с
# информацией по всем супергероям.
# Нужно определить кто самый умный(intelligence)
# из трех супергероев- Hulk, Captain America, Thanos.

import requests

def get_heroes_data(url):
    response = requests.get(url)
    return response.json()

url = "https://akabab.github.io/superhero-api/api/all.json"
heroes_data = get_heroes_data(url)
intelligence = {}

for hero in heroes_data:
    if hero['name'] == 'Hulk' or hero['name'] == 'Captain America' or hero['name'] == 'Thanos':
        intelligence[hero['name']] = int(hero['powerstats']['intelligence'])

smartest = max(intelligence, key=intelligence.get)

print(f"Самый умный супергерой из Hulk, Captain America, Thanos: {smartest}")