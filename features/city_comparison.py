"""
Feature: City Comparison 
    - Compare current weather in two cities side-by-side

"""

# from tkinter import simpledialog, messagebox
# from core.weather_logic import get_custom_description


def compare_city(weather_api, city_one_data: dict, city_two: str):
    """
    Fetches and validates weather data for two cities.

    Args:
        weather_api: WeatherAPI instance
        city_one: Name of the first city
        city_two: Name of the second city

    Returns:
        tuple: (city_one_data, city_two_data) if successful

    Raises:
        ValueError: If any city is invalid or API fails
    """
    city_two_data = weather_api.fetch_weather(city_two)

    # Validate both cities
    if not city_one_data or str(city_one_data.get("cod")) != "200":
        raise ValueError("First city data is invalid. Please fetch it again.")
    
    if not city_two_data or str(city_two_data.get("cod")) != "200":
        raise ValueError(f"Second city '{city_two}' is invalid.")

    return city_one_data, city_two_data
