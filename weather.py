import requests
import json
import pprint

# OpenWeatherMap
WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather?appid=7cffc975fdc6d54459c5901e470c0cee&units=metric&q="

GOOGLE_KEY = ""
NEWS_KEY = ""

pp = pprint.PrettyPrinter(indent = 3)

weather_data = None

def get_weather():
	global weather_data
	result = requests.get(WEATHER_URL + "Santa Rita do Sapucai")
	content = result.text
	weather_data = json.loads(content)
	# pp.pprint(weather_data)
	
def get_temperature():
	temperature = -1
	if weather_data is not None:
		temperature = int(weather_data["main"]["temp"])
	return str(temperature) + "ºC"
	
def get_condition():
	condition = "<not loaded>"
	if weather_data is not None:
		condition = weather_data["weather"][0]["main"]
	return condition
