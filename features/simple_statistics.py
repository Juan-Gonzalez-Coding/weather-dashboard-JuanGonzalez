
def get_temp_stats(data: dict) -> tuple:
    """
    - Track min/max temperatures and count weather types
    Args:
        data (dict): Weather API response.

    Returns:
        tuple: (min_temp, max_temp) or (None, None) if unavailable.
    """
    try:
        if data and "main" in data and "weather" in data:
            min_temp = data['main']['temp_min']
            max_temp = data['main']['temp_max']
            weather_type = data['weather'][0]['main']  # e.g., "Clear", "Clouds"
            return min_temp, max_temp, weather_type
        else:
            return None, None, None
        
    except Exception as err:
        print(f"Error extracting temperature stats: {err}")
        return None, None, None
    