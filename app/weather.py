from app.alpha import WEATHER_API_KEY
import requests

def convert_weather(json_data):
    temperature = json_data["main"]["temp"]
    feels_like = json_data["main"]["feels_like"]
    humidity = json_data["main"]["humidity"]
    weather = json_data["weather"][0]["main"]
    temp_min = json_data["main"]["temp_min"]
    temp_max = json_data["main"]["temp_max"]
    country = json_data['sys']["country"]
    desc = json_data['weather'][0]['description']
    wind_speed = json_data['wind']['speed']
    pressure = json_data['main']['pressure']
    vis = json_data['visibility'] / 1000.0

    weather_data = {
        "temp": str(temperature),
        "feels": feels_like,
        "humid": str(humidity),
        "weather": weather,
        "temp_min": temp_min,
        "temp_max": temp_max,
        "country": country,
        "desc": desc,
        "wind_speed": wind_speed,
        "pressure": pressure,
        "vis": vis
        }

    return  weather_data

def get_weather_data(city, api):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api}"
    url_forecast = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={api}"
    jsonf = requests.get(url)
    forecast_jsonf = requests.get(url_forecast)
    return jsonf.json(), forecast_jsonf.json()

if __name__ == "__main__":

    print("WEATHER REPORT...")

    city_name = input("Please input a city (default: 'New York'): ") or "New York"
    print("CITY:", city_name)

    json_data, forecast_json_data = get_weather_data(city_name, WEATHER_API_KEY)
    weather_data = convert_weather(json_data)

    print(weather_data)