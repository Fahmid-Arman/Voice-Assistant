import requests

API_KEY = '1c7f75e7ae87b3028b8c0999fec1c4cf'
lat = 23.8103
lon = 90.4125
url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'
json_data = requests.get(url).json()

def temp():
    temperature = round(json_data['main']['temp'] - 273.15, 1)
    return temperature

def des():
    description = json_data['weather'][0]['description']
    return description