#core/api.py

import requests
from typing import Optional, Dict

class WeatherAPI:
    """Handles weather API fetching"""

    def __init__(self, api_key: str):
        self.api_key = api_key #API key for authenticating with OpenWeather
        self.base_url = "https://api.openweathermap.org/data/2.5/weather" #Endpoint for weather
        self.timeout = 10 # Max seconds before timing out

    def fetch_weather(self, city: str) -> Optional[Dict]:
        """
        Fetch weather data for user city

        Args: 
            city: Name of the city

        Returns: 
            Dictionary with weather data or None if error occurs
        """
        try: 
            params = {
                "q": city,
                "units": "imperial", # Imperial for Fahrenheit
                "appid": self.api_key
            }
            #Sending a GET request to Weather API
            response = requests.get(
                self.base_url,
                params=params,
                timeout=self.timeout
            )

            response.raise_for_status() #Raises an error if request failed 
            return response.json() #Return parsed JSON as a python dictionary
        
        except requests.RequestException as err:
            #Prints an error and returns None if something goes wrong
            print(f"API Error: {err}")
            return None