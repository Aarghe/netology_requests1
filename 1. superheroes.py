import requests

url = 'https://superheroapi.com/api/2619421814940190/'
method = 'search/'
heroes = ['Hulk', 'Captain America', 'Thanos']
hero_int = {}
for hero in heroes:
    req = requests.get(url + method + hero)
    hero_int[hero] = req.json()['results'][0]['powerstats']['intelligence']

print(max(hero_int))