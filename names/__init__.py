import requests

def fetch_data(url):
    response = requests.get(url)
    data = response.json()
    return [item['name'] for item in data]
