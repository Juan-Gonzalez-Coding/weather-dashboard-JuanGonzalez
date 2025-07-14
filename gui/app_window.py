# gui/app_window.py
"""Main application window"""

import tkinter as tk
from tkinter import messagebox

class AppWindow:

     def __init__(self, fetch_weather_callback):
        self.root = tk.Tk()
        self.root.title("Weather App") #App window title
        self.root.geometry("800x600")

        self.label = tk.Label(self.root, text="Weather Dashboard 🌤️", font=("Helvetica", 25, "bold"), fg="black")
        self.label.pack(pady=20)

        self.city_label = tk.Label(self.root, text="City: ")
        self.city_label.pack(pady=10)

        self.temperature_label = tk.Label(self.root, text="Temperature: ")
        self.temperature_label.pack(pady=10)

        self.description_label = tk.Label(self.root, text="Description: ")
        self.description_label.pack(pady=10)

        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        self.input_label = tk.Label(input_frame, text="Enter a City: ")
        self.input_label.grid(row=0, column=0, padx=5)

        self.city_input = tk.Entry(input_frame, width=40)
        self.city_input.grid(row=0, column=1, padx=5)
        
        self.button = tk.Button(self.root, text="Get Weather",command = fetch_weather_callback)
                                
        self.button.pack()

     def run(self):
        self.root.mainloop()

     def get_city(self) -> str:
        """Returns the user input for city."""
        try: 
           city = self.city_input.get() #Getting user input for city

           if not city.strip(): #Checks if the city input is empty when using strip()
               raise ValueError("No city entered, please enter a city.")
           
           return city
         
        except Exception as err: #Catches any error that was raised in the try block
           messagebox.showerror("Input Error", f"{err}") #Opens a popup window and displays the error.
           return "" #Returns an empty string if input fails.
        
     def update_weather_info(self, city: str, temperature: float, description: str):
        """Updates the GUI labels with weather data."""

        try:
            self.city_label.config(text=f"City: {city}")
            self.temperature_label.config(text=f"Current Temperature: {temperature}°F")
            self.description_label.config(text=f"Weather Description: {description}")

        except Exception as err:
            messagebox.showerror("Update Error", f"Could not update weather information: {err}")  #Shows an alert popup window if weather information coud not be updated.