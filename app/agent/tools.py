import openmeteo_requests


def weather_tool(latitude: float, longitude: float):
    """Get the weather forecast for a given latitude and longitude.
    Args:
        latitude (float): The latitude of the location.
        longitude (float): The longitude of the location.
    """
    openmeteo_client = openmeteo_requests.Client()
    url = "https://api.open-meteo.com/v1/forecast"
    # Params contain the info i'm requesting from the API
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": (
            "temperature_2m_max", # multiple parameters can be requested as a collection
            "temperature_2m_min",
            "precipitation_sum"
            ),
        "timezone": "auto",
    }

    responses = openmeteo_client.weather_api(url, params=params)
    response = responses[0]

    daily = response.Daily()
    if daily is None:
        print("No daily data available.")
        return
    
    daily_temperature_max = daily.Variables(0)
    daily_temperature_min = daily.Variables(1)
    daily_precipitation_sum = daily.Variables(2)

    if daily_temperature_max is None or daily_temperature_min is None or daily_precipitation_sum is None:
        print("One or more daily variables are not available.")
        return

    temperature_max = daily_temperature_max.ValuesAsNumpy()
    temperature_min = daily_temperature_min.ValuesAsNumpy()
    precipitation_sum = daily_precipitation_sum.ValuesAsNumpy()
    print(f"Daily max temperatures: {temperature_max} °C")
    print(f"Daily min temperatures: {temperature_min} °C")
    print(f"Daily precipitation sum: {precipitation_sum} mm")
    
    

    # should return data requested by the user, specified in a schema
    # print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°W")
    # print(f"Elevation: {response.Elevation()} m asl")
    # print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()/3600}h")
    # print(f"Timezone: {response.Timezone()}")
    

if __name__ == "__main__":
    # Example usage
    weather_tool(40.7128, -74.0060)  # Coordinates for New York City




    


