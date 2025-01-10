import requests

country = input("Enter the Country you would like to know about: ")

url = f'https://restcountries.com/v3.1/name/{country}'
response = requests.get(url)
data = response.json()

country_data = data[0]
name = country_data['name']['common']
capital = country_data['capital'][0]
region = country_data['region']
population = country_data['population']
languages = ', '.join(country_data['languages'].values())

print(f'Capital: {capital}')
print(f'Region: {region}')
print(f'Population: {population}')
print(f'Languages: {languages}')