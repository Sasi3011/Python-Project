import requests

def get_weather_data(location):
    api_key = "YOUR_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    res = requests.get(url)
    return res.json()['main']
