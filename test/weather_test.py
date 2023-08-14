from app.weather import get_weather_data
from app.alpha import WEATHER_API_KEY


def test_weather_data():

    data = get_weather_data("New York", WEATHER_API_KEY)

    # it returns a dict:
    assert isinstance(data, dict)

    # where each has a "weather"
    assert 'weather' in list(data.keys())

    # and wind_speed are formatted as floats:
    assert isinstance(data['wind']["speed"], float)

