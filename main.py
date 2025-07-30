#main.py

from config import load_config
from core.api import WeatherAPI 
from dotenv import load_dotenv #This is used for loading the .env file
from gui.app_window import AppWindow
from core.weather_logic import extract_data, compare_cities

load_dotenv() #Loading the .env variables

#Loading the API key using the config load function
try: 
    config = load_config()
    api_key = config.api_key
except ValueError as e:
    print(e)
    api_key = None #If the key is missing 

#Set up the WeatherAPI client
weather_api = WeatherAPI(api_key)

#Creates an instance of my AppWindow class and passes the extract_data function
# Wrap the logic functions to pass required arguments
app = AppWindow(
    lambda: extract_data(app, weather_api), 
    lambda: compare_cities(app, weather_api)
    ) 
app.run()

