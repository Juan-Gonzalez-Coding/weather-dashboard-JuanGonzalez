#main.py

from core.storage import log_weather
from config import load_config
from core.api import WeatherAPI 
from dotenv import load_dotenv #This is used for loading the .env file
from gui.app_window import AppWindow
from tkinter import simpledialog, messagebox
from features.simple_statistics import get_temp_stats
from features.city_comparison import compare_city
from features.display_icon import display_icon

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
        city_name = data['name'] #Extractding city name
        city_desc = data['weather'][0]['description'] #Extracting weather description
        
        icon_image = display_icon(app.icon_canvas, data)

        min_temp, max_temp, weather_type = get_temp_stats(data)

        app.set_current_city(data) #Setting the current city

        app.update_weather_info(city_name, city_temp, max_temp, min_temp, weather_type, city_desc) #Update GUI 

        if icon_image:
            app.update_weather_icon(icon_image)

        log_weather(city_name, city_temp, city_desc) #Log data into CSV

    except ValueError as err:
        messagebox.showerror("Invalid City", str(err))

    except Exception as err:
        messagebox.showerror("Error", f"Something went wrong: {err}")

def compare_cities():
    """Handle UI for city comparison feature."""
    try:
        # Get first city from input
        city_one_data = app.get_current_city()
        if not city_one_data:
            messagebox.showwarning("No Data", "Please fetch weather for the first city before comparing.")
            return

        # Ask user for second city
        city_two = simpledialog.askstring("City Comparison", "Enter the second city to compare:")
        if not city_two or not city_two.strip():
            messagebox.showwarning("Input Error", "Second city cannot be empty.")
            return

        # Use compare_city from features
        city_one_data, city_two_data = compare_city(weather_api, city_one_data, city_two)

        # Display comparison window
        app.open_compare_window(city_one_data, city_two_data)

    except ValueError as ve:
        messagebox.showerror("Invalid City", str(ve))
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")

app = AppWindow(fetch_weather, compare_cities) #Creates an instance of my AppWindow class and passes the fetch_weather function
app.run()
