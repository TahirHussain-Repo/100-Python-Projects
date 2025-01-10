import requests

month = input("Enter the month (e.g. '3' for March): ")
day = input("Enter the day (e.g. '1' for 1st): ")

url = f'https://history.muffinlabs.com/date/{month}/{day}'

reponse = requests.get(url)
data = reponse.json()
events = data['data']['Events']

for event in events:
    print(f'Year: {event['year']}')
    print(f'Description: {event['text']}')
    print(f'Link: {event['links'][0]['link']}')
    print('\n')


