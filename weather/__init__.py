import requests


def get_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=API_KEY"
    response = requests.get(url)
    data = response.json()
    return data["main"]["temp"]
