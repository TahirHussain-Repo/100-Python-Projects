import requests

url = 'https://restcountries.com/v3.1/all'
response = requests.get(url)

content = response.json()

##print(content)
country = input('Enter country: ')

for c in content:
    country_name = c['name']['common']
    if country_name == country:
        print(c['capital'][0])