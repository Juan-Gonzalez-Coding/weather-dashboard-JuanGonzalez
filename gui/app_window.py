# gui/app_window.py
"""Main application window"""

import tkinter as tk
from tkinter import messagebox

class AppWindow:

     def __init__(self, fetch_weather_callback, compare_callback):
        self.root = tk.Tk()
        self.root.title("Weather App") #App window title
        self.root.geometry("1200x1000")

        self.current_city_data = None

        self.label = tk.Label(self.root, text="Weather Dashboard 🌤️", font=("AppleGothic", 25, "normal"), fg="black")
        self.label.pack(pady=20)

        self.icon_canvas = tk.Canvas(self.root, width=120, height=120, borderwidth=1, relief="solid")
        self.icon_canvas.pack(pady=5)

        self.icon_image = None

        self.city_label = tk.Label(self.root, font="AppleGothic", text="City: ")
        self.city_label.pack(pady=10)

        self.temperature_label = tk.Label(self.root, font="AppleGothic", text="Temperature: ")
        self.temperature_label.pack(pady=10)

        self.max_temp_label = tk.Label(self.root, font="AppleGothic", text="Max: " )
        self.max_temp_label.pack(pady=10)

        self.min_temp_label = tk.Label(self.root, font="AppleGothic", text="Min: " )
        self.min_temp_label.pack(pady=10)

        self.weather_type_label = tk.Label(self.root, font="AppleGothic", text="Weather Type: ")
        self.weather_type_label.pack(pady=10)

        self.description_label = tk.Label(self.root, font="AppleGothic", text="Description: ")
        self.description_label.pack(pady=10)

        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        self.input_label = tk.Label(input_frame, font="AppleGothic", text="Enter a City: ")
        self.input_label.grid(row=0, column=0, padx=5)

        self.city_input = tk.Entry(input_frame, width=40)
        self.city_input.grid(row=0, column=1, padx=5)
        
        self.weather_button = tk.Button(self.root, font="AppleGothic", text="Get Weather",command=fetch_weather_callback)                         
        self.weather_button.pack(pady=5)

        self.compare_button = tk.Button(self.root, font="AppleGothic", text="Compare a City", command=compare_callback)
        self.compare_button.pack(pady=5)

     def set_current_city(self, data: dict):
         """Stores the most recent city weather data."""
         self.current_city_data = data

     def get_current_city(self) -> dict:
         """Returns the most recent city weather data."""
         return self.current_city_data

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
        

     def update_weather_info(self, city: str, temperature: float, max_temp: float, min_temp: float, weather_type: str, description: str):
        """Updates the GUI labels with weather data."""

        try:
            self.city_label.config(text=f"City: {city}")
            self.temperature_label.config(text=f"Current Temperature: {temperature}°F")
            self.max_temp_label.config(text=f"Max: {max_temp}°F")
            self.min_temp_label.config(text=f"Min: {min_temp}°F")
            self.weather_type_label.config(text=f"Weather Type: {weather_type}")
            self.description_label.config(text=f"Weather Description: {description}")

        except Exception as err:
            messagebox.showerror("Update Error", f"Could not update weather information: {err}")  #Shows an alert popup window if weather information coud not be updated.

     def update_weather_icon(self, tk_image):
         """
         Update the weather icon displayed in the GUI.

         Args:
            tk_image: A PhotoImage object to display. 
         """
         self.icon_image = tk_image 

     def open_compare_window(self, city_one_data: dict, city_two_data: dict):
         """Opens a new window to compare two cities side-by-side."""
         try: 
            compare_window = tk.Toplevel(self.root)
            compare_window.title("City Comparison")
            compare_window.geometry("600x400")

            # Header
            header_label = tk.Label(compare_window, text="City Weather Comparison", font=("AppleGothic", 20, "bold"))
            header_label.pack(pady=10)

            # Create a frame for side-by-side layout
            frame = tk.Frame(compare_window)
            frame.pack(pady=10)

            # City One Info
            city_one_frame = tk.Frame(frame)
            city_one_frame.grid(row=0, column=0, padx=20)

            tk.Label(city_one_frame, text=f"City: {city_one_data['name']}", font=("AppleGothic", 14)).pack()
            tk.Label(city_one_frame, text=f"Temp: {city_one_data['main']['temp']}°F").pack()
            tk.Label(city_one_frame, text=f"Max: {city_one_data['main']['temp_max']}°F").pack()
            tk.Label(city_one_frame, text=f"Min: {city_one_data['main']['temp_min']}°F").pack()
            tk.Label(city_one_frame, text=f"Weather: {city_one_data['weather'][0]['main']}").pack()
            tk.Label(city_one_frame, text=f"Description: {city_one_data['weather'][0]['description']}").pack()


            # City Two Info
            city_two_frame = tk.Frame(frame)
            city_two_frame.grid(row=0, column=1, padx=20)

            tk.Label(city_two_frame, text=f"City: {city_two_data['name']}", font=("AppleGothic", 14)).pack()
            tk.Label(city_two_frame, text=f"Temp: {city_two_data['main']['temp']}°F").pack()
            tk.Label(city_two_frame, text=f"Max: {city_two_data['main']['temp_max']}°F").pack()
            tk.Label(city_two_frame, text=f"Min: {city_two_data['main']['temp_min']}°F").pack()
            tk.Label(city_two_frame, text=f"Weather: {city_two_data['weather'][0]['main']}").pack()
            tk.Label(city_two_frame, text=f"Description: {city_two_data['weather'][0]['description']}").pack()

         except Exception as err:
            messagebox.showerror("Comparison Error", f"Could not open comparison window: {err}")

