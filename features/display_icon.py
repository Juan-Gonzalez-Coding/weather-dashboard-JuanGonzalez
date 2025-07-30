"""
Feature: Weather Icons 
    - Use canvas graphics to visually represent weather (e.g., sun, clouds)

"""

import requests
from io import BytesIO
from PIL import Image, ImageTk


def display_icon(canvas, data):
    """
    Displays a weather icon on the given canvas based on weather data.

    Args:
        canvas (tk.Canvas): The Tkinter canvas where the icon will be displayed.
        data (dict): The weather data dictionary returned by fetch_weather().
    
    Returns:
        PhotoImage: The Tkinter-compatible image to prevent garbage collection.
    """
    #Extracting the icon doe from the weather data
    try:
        icon_code = data["weather"][0]["icon"]
    except (KeyError, IndexError):
        raise ValueError("Weather data missing icon code.")

    #URL for fetching the image using icon code
    url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"

    #Fetching the image using url
    response = requests.get(url)
    response.raise_for_status()

    #Convert the response into a format PIL can read
    image_data = BytesIO(response.content ) 
    pil_image= Image.open(image_data)

    #Converting the PIL image into a Tkinter-compatible image
    tk_image = ImageTk.PhotoImage(pil_image)

    #Display the image on the canvas
    canvas.delete("all")
    canvas.create_image(60,60, image=tk_image, anchor='center')

    return tk_image
