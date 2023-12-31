# final-project



## Setup

Obtain an [OpenWeather API Key](https://openweathermap.org/api). Then create a file called ".env" and place it inside (like the following example):

```sh
# this is the ".env" file (in the root directory of the repo)

WEATHER_API_KEY="____________"
```

Create a virtual environment:

```sh
conda create -n weather-env python=3.10
```

```sh
conda activate weather-env
```

Install third-party packages:

```sh
pip install -r requirements.txt
```

## Usage

Run the weather report:

```sh
python -m app.weather
```


Run the web app:

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or try a ".env" file approach
export FLASK_APP=web_app
flask run
```

## Testing

Run tests:

```sh
pytest
```
