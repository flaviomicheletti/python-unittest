# my_module.py
import requests

class MyClass:
    def __init__(self, url):
        self.url = url

    def get_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
