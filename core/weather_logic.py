# core/weather_logic.py

import json
import os
from tkinter import simpledialog, messagebox
from features.simple_statistics import get_temp_stats
from features.city_comparison import compare_city
from features.display_icon import display_icon
from core.storage import log_weather


def load_custom_descriptions():
    """ Load custom descriptions from JSON in the same directory."""
    json_path = os.path.join(os.path.dirname(__file__), 'custom_descriptions.json')
    with open(json_path, 'r') as file:
        return json.load(file)

custom_descriptions = load_custom_descriptions()

def extract_data(app, weather_api):
    """Fetches and displays weather data of a user-input city."""
    user_city = app.get_city()

    try:
        data = weather_api.fetch_weather(user_city)

        if data is None:
            raise ValueError("Not a valid city.")

        city_temp = data['main']['temp']
        city_name = data['name']
        city_desc = data['weather'][0]['description']
        custom_description = custom_descriptions.get(city_desc.lower(), city_desc)

        # Display icon
        icon_image = display_icon(app.icon_canvas, data)

        # Get min/max/weather_type
        min_temp, max_temp, weather_type = get_temp_stats(data)

        # Update the GUI
        app.set_current_city(data)
        app.update_weather_info(city_name, city_temp, max_temp, min_temp, weather_type, custom_description)

        if icon_image:
            app.update_weather_icon(icon_image)

        # Log data
        log_weather(city_name, city_temp, city_desc)

    except ValueError as err:
        messagebox.showerror("Invalid City", str(err))
    except Exception as err:
        messagebox.showerror("Error", f"Something went wrong: {err}")


def compare_cities(app, weather_api):
    """Compares weather between current city and a second user-entered city."""
    try:
        #Get first city from user input
        city_one_data = app.get_current_city()
        if not city_one_data:
            messagebox.showwarning("No Data", "Please fetch weather for the first city before comparing.")
            return
        #Prompt user for second city
        city_two = simpledialog.askstring("City Comparison", "Enter the second city to compare:")
        if not city_two or not city_two.strip():
            messagebox.showwarning("Input Error", "Second city cannot be empty.")
            return
        #Use compare_city from features
        city_one_data, city_two_data = compare_city(weather_api, city_one_data, city_two)
        
        #Display comparison window
        app.open_compare_window(city_one_data, city_two_data)

    except ValueError as ve:
        messagebox.showerror("Invalid City", str(ve))
    except Exception as err:
        messagebox.showerror("Error", f"Something went wrong: {err}")