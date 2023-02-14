import requests


def get_data():
    url = f"http://localhost/api/holidays"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None
    # return response.json()
