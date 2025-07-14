#main.py

from core.storage import log_weather
from config import load_config
from core.api import WeatherAPI 
from dotenv import load_dotenv #This is used for loading the .env file
from gui.app_window import AppWindow
from tkinter import messagebox

load_dotenv() #Loading the .env variables

#Loading the API key using the config load function
try: 
    config = load_config()
    api_key = config.api_key
except ValueError as e:
    print(e)
    api_key = None #If the key is missing 

#Setting up the WeatherAPI client
weather_api = WeatherAPI(api_key)


def fetch_weather():
    """Fetches weather when the user clicks the button"""
    user_city = app.get_city() #Get city from user input

    try:
        data = weather_api.fetch_weather(user_city) #Calling the API
        
        if data is None:
            raise ValueError("Not a valid city.")
        
        city_temp = data['main']['temp'] #Extracting the temperature
        max_temp = data ['main']['temp_max'] #Extracting max temp from data
        min_temp = data['main']['temp_min'] #Extracting min temp from data
        city_name = data['name'] #Extractding city name
        city_desc = data['weather'][0]['description'] #Extracting weather description
        weather_type = data['weather'][0]['main'] #Extracting weather type
             
        # print(data)

        app.update_weather_info(city_name, city_temp, city_desc) #Update GUI 
        log_weather(city_name, city_temp, city_desc) #Log data into CSV

    except ValueError as err:
        messagebox.showerror("Invalid City", str(err))

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")
        

app = AppWindow(fetch_weather) #Creates an instance of my AppWindow class and passes the fetch_weather function
app.run()
