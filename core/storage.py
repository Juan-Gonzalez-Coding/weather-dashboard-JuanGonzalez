import os
import csv 
from datetime import datetime

def get_timestamp():
    """Returns current date and time as separate strings."""
    date = datetime.now().strftime("%Y-%m-%d")  #Getting current date
    time = datetime.now().strftime("%H:%M")     #Getting current time 

    return date, time

def get_data_file_path(filename = "weather_log.csv") -> str:
    """
    Finds the file path to the data directory 
    to save weather_log.csv

    """
    core_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of core/

    root_dir = os.path.dirname(core_dir) #Going up one level to the root directory

    data_dir = os.path.join(root_dir, "data") #Pointing to the data/ directory in the project root directory.
    os.makedirs(data_dir, exist_ok=True)

    file_path = os.path.join(data_dir, filename)

    return file_path

def file_exists(file_path: str) -> bool:
    """Checks to see if the file exists."""
    file_exists = os.path.isfile(file_path) # Check to see if the file exists.
    return  file_exists

def write_to_csv_row(file_path: str, row: list, headers: list): 
    """Adds one row to CSV and adds a header if needed"""
    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)
        
        if not file_exists(file_path):  # Directly check inside the if statement
            writer.writerow(headers)
        
        writer.writerow(row)

def log_weather(city: str, temp: float, description: str):
    """Uses all methods to save a weather log into a CSV."""
    date, time = get_timestamp()
    file_path = get_data_file_path()
    row = [city, temp, description, date, time]
    headers = ["City", "Temperature", "Description","Date","Time"]
    write_to_csv_row(file_path, row, headers)