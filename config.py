import os

class Config:
    """
    Holds the API Key
    """
    def __init__(self, api_key: str):
        self.api_key = api_key #Key to authenticate with weather API


def load_config():
    api_key = os.getenv("WEATHER_APP_API_KEY") #Loading API key from environment file
    if not api_key:
        raise ValueError("WEATHER_APP_API_KEY environment variable needed.")
    
    return Config(api_key)