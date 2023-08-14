from flask import Blueprint, request, render_template, redirect, flash
from app.weather import convert_weather, get_weather_data
from app.alpha import API_KEY, WEATHER_API_KEY

weather_routes = Blueprint("weather_routes", __name__)

@weather_routes.route("/weather/form")
def weather_form():
    print("WEATHER FORM...")
    return render_template("weather_form.html")

@weather_routes.route("/weather/dashboard", methods=["GET", "POST"])
def weather_dashboard():
    print("WEATHER DASHBOARD...")

    if request.method == "POST":
        # for data sent via POST request, form inputs are in request.form:
        request_data = dict(request.form)
        print("FORM DATA:", request_data)
    else:
        # for data sent via GET request, url params are in request.args
        request_data = dict(request.args)
        print("URL PARAMS:", request_data)

    city_name = request_data.get("city") or "New York"

    try:
        json_data = get_weather_data(city_name, WEATHER_API_KEY)
        print(json_data)
        data = convert_weather(json_data)
        return render_template("weather_dashboard.html", city=city_name.capitalize(), 
                            temp=data['temp'], 
                            feels_like=data['feels'], 
                            humid=data['humid'],
                            weather=data['weather'],
                            temp_min=data['temp_min'],
                            temp_max=data['temp_max'],
                            country=data['country'],
                            desc=data['desc'],
                            wind_speed=data['wind_speed'],
                            pressure=data['pressure'],
                            vis=data['vis']
                            )

    except Exception as err:
        print('OOPS', err)

        flash("Weather Data Error. Please check your city and try again!", "danger")
        return redirect("/weather/form")

#
# API ROUTES
#

@weather_routes.route("/api/weather.json")
def weather_api():
    print("STOCKS DATA (API)...")

    # for data supplied via GET request, url params are in request.args:
    url_params = dict(request.args)
    print("URL PARAMS:", url_params)
    city_name = url_params.get("city_name") or "New York"

    try:
        json_data = get_weather_data(city_name, WEATHER_API_KEY)
        print(json_data)
        data = convert_weather(json_data)
        return {"city": city_name, "data": data}
    except Exception as err:
        print('OOPS', err)
        return {"message":"Weather Data Error. Please try again."}, 404