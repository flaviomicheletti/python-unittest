import requests


def get_holidays():
    try:
        r = requests.get("http://localhost/api/holidays")
        if r.status_code == 200:
            return r.json()
    except:
        return None
