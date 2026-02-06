from pydantic import BaseModel, Field

class DailyWeatherParameters(BaseModel):
    temperature_2m_max: float | None = Field(..., description="Maximum daily air temperature at 2 meters above ground.")
    temperature_2m_mean: float | None = Field(..., description="Mean daily air temperature at 2 meters above ground.")
    temperature_2m_min: float | None = Field(..., description="Minimum daily air temperature at 2 meters above ground.")

    apparent_temperature_max: float | None = Field(..., description="Maximum daily apparent temperature (feels like).")
    apparent_temperature_mean: float | None = Field(..., description="Mean daily apparent temperature (feels like).")
    apparent_temperature_min: float | None = Field(..., description="Minimum daily apparent temperature (feels like).")

    precipitation_sum: float | None = Field(..., description="Sum of daily precipitation (including rain, showers and snowfall)")
    rain_sum: float | None = Field(..., description="Sum of daily rain.")
    showers_sum: float | None = Field(..., description="Sum of daily showers.")
    snowfall_sum: float | None = Field(..., description="Sum of daily snowfall.")
    precipitation_hours: float | None = Field(..., description="Number of hours with rain.")

    precipitation_probability_max: float | None = Field(..., description="Maximum daily precipitation probability.")
    precipitation_probability_mean: float | None = Field(..., description="Mean daily precipitation probability.")
    precipitation_probability_min: float | None = Field(..., description="Minimum daily precipitation probability.")

    weather_code: float | None = Field(..., description="The most severe weather condition on a given day")

    sunrise: int | None = Field(..., description="Sunrise time iso8601 format.")
    sunset: int | None = Field(..., description="Sunset time iso8601 format.")

    sunshine_duration: float | None = Field(..., description="Daily sunshine duration in seconds.")
    daylight_duration: float | None = Field(..., description="Daily daylight duration in seconds.")
    
    wind_speed_10m_max: float | None = Field(..., description="Maximum daily wind speed at 10 meters above ground.")
    wind_gusts_10m_max: float | None = Field(..., description="Maximum daily wind gusts at 10 meters above ground.")
    wind_direction_10m_dominant: float | None = Field(..., description="Dominant daily wind direction at 10 meters above ground.")
    
    shortwave_radiation_sum: float | None = Field(..., description="The sum of solar radiation on a given day in Megajoules per square meter.")
    et0_fao_evapotranspiration: float | None = Field(..., description="Daily sum of ET₀ Reference Evapotranspiration of a well watered grass field")
    
    uv_index_max: float | None = Field(..., description="Maximum daily UV index.")
    uv_index_clear_sky_max: float | None = Field(..., description="Maximum daily clear-sky UV index.")
    
    response: str | None = Field(..., description="The final, human-readable answer to the user's question.")

class WeatherByLocationInput(BaseModel):
    location: str = Field(..., description="The city or location name to get the weather for.")
    temperature_2m_max: bool = Field(False, description="Set to true to request maximum daily air temperature at 2 meters above ground.")
    temperature_2m_min: bool = Field(False, description="Set to true to request minimum daily air temperature at 2 meters above ground.")
    precipitation_sum: bool = Field(False, description="Set to true to request the sum of daily precipitation (including rain, showers and snowfall).")
    apparent_temperature_max: bool = Field(False, description="Set to true to request maximum daily apparent temperature (feels like).")
    apparent_temperature_mean: bool = Field(False, description="Set to true to request mean daily apparent temperature (feels like).")
    apparent_temperature_min: bool = Field(False, description="Set to true to request minimum daily apparent temperature (feels like).")
    rain_sum: bool = Field(False, description="Set to true to request sum of daily rain.")
    showers_sum: bool = Field(False, description="Set to true to request sum of daily showers.")
    snowfall_sum: bool = Field(False, description="Set to true to request sum of daily snowfall.")
    precipitation_hours: bool = Field(False, description="Set to true to request number of hours with rain.")
    precipitation_probability_max: bool = Field(False, description="Set to true to request maximum daily precipitation probability.")
    precipitation_probability_mean: bool = Field(False, description="Set to true to request mean daily precipitation probability.")
    precipitation_probability_min: bool = Field(False, description="Set to true to request minimum daily precipitation probability.")
    weather_code: bool = Field(False, description="Set to true to request the most severe weather condition on a given day.")
    sunrise: bool = Field(False, description="Set to true to request sunrise time iso8601 format.")
    sunset: bool = Field(False, description="Set to true to request sunset time iso8601 format.")
    sunshine_duration: bool = Field(False, description="Set to true to request daily sunshine duration in seconds.")
    daylight_duration: bool = Field(False, description="Set to true to request daily daylight duration in seconds.")
    wind_speed_10m_max: bool = Field(False, description="Set to true to request maximum daily wind speed at 10 meters above ground.")
    wind_gusts_10m_max: bool = Field(False, description="Set to true to request maximum daily wind gusts at 10 meters above ground.")
    wind_direction_10m_dominant: bool = Field(False, description="Set to true to request dominant daily wind direction at 10 meters above ground.")
    shortwave_radiation_sum: bool = Field(False, description="Set to true to request the sum of solar radiation on a given day in Megajoules per square meter.")
    et0_fao_evapotranspiration: bool = Field(False, description="Set to true to request daily sum of ET₀ Reference Evapotranspiration of a well watered grass field.")
    uv_index_max: bool = Field(False, description="Set to true to request maximum daily UV index.")
    uv_index_clear_sky_max: bool = Field(False, description="Set to true to request maximum daily clear-sky UV index.")
