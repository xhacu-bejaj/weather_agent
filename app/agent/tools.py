import openmeteo_requests
import requests
import numpy as np
from langchain.tools import tool
from app.models.schemas import WeatherByLocationInput 


def _get_location_coordinates_logic(location: str):
    """
    Retrieves the latitude and longitude coordinates for a given location.
    (Internal helper function, not a direct tool for the agent)
    """
    api_url = f"https://geocoding-api.open-meteo.com/v1/search?name={location}&count=10&language=en&format=json"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if "results" in data and len(data["results"]) > 0:
            result = data["results"][0]
            latitude = result.get("latitude")
            longitude = result.get("longitude")
            return {"latitude": latitude, "longitude": longitude}
        else:
            return {"error": "No results found for the specified location."}
    return {"error": f"Geocoding API request failed with status code {response.status_code}"}


def _weather_tool_logic(**kwargs):
    """
    Get the weather forecast for a given latitude and longitude using selected parameters.
    (Internal helper function, not a direct tool for the agent)
    """
    latitude = kwargs.pop('latitude')
    longitude = kwargs.pop('longitude')

    selected_params = [key for key, value in kwargs.items() if value is True]

    if not selected_params:
        return {"error": "No weather parameters were selected."}

    openmeteo_client = openmeteo_requests.Client()
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": selected_params,
        "timezone": "auto",
    }

    try:
        responses = openmeteo_requests.Client().weather_api(url, params=params)
        response = responses[0]

        daily = response.Daily()
        if daily is None:
            return {"error": "No daily data available from weather API."}
        
        daily_data = {}
        for i, param in enumerate(selected_params): 
            variable = daily.Variables(i) 
            if variable is not None:
                values = variable.ValuesAsNumpy()
                if isinstance(values, np.ndarray):
                    daily_data[param] = values.tolist()
                else:
                    daily_data[param] = values

        if not daily_data:
            return {"error": "No daily variables could be processed from weather API response."}

        return daily_data
    except Exception as e:
        return {"error": f"Weather API request failed: {e}"}



@tool(args_schema=WeatherByLocationInput)
def get_weather_by_location(**kwargs):
    """
    Get the current weather forecast for a specified location, including various weather parameters.
    This tool first retrieves the coordinates for the given location and then fetches the weather data.
    """
    location = kwargs.pop('location')
    
    
    coords_result = _get_location_coordinates_logic(location)
    if coords_result.get("error"):
        return coords_result
        
    latitude = coords_result.get("latitude")
    longitude = coords_result.get("longitude")
    
    
    weather_kwargs = {
        'latitude': latitude,
        'longitude': longitude,
    }
    
    weather_kwargs.update(kwargs) 
    
    return _weather_tool_logic(**weather_kwargs)