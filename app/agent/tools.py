from typing import List

import openmeteo_requests
import numpy as np
from langchain.tools import tool

@tool
def weather_tool(latitude: float, longitude: float, user_params: List[str]):
    """Get the weather forecast for a given latitude and longitude.
    Args:
        latitude (float):
        longitude (float):
        user_params (List[str]): A list of weather parameters to retrieve.
    """
    openmeteo_client = openmeteo_requests.Client()
    url = "https://api.open-meteo.com/v1/forecast"
    # Params contain the info i'm requesting to the API
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": user_params,
        "timezone": "auto",
    }

    responses = openmeteo_client.weather_api(url, params=params)
    response = responses[0]

    daily = response.Daily()
    if daily is None:
        return {"error": "No daily data available."}
    
    daily_data = {}
    for i, param in enumerate(params["daily"]):
        variable = daily.Variables(i)
        if variable is not None:
            values = variable.ValuesAsNumpy()
            if isinstance(values, np.ndarray):
                daily_data[param] = values.tolist()
            else:
                daily_data[param] = values

    if not daily_data:
        return {"error": "No daily variables could be processed."}

    return daily_data
    





    


