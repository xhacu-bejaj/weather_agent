from pydantic import BaseModel, Field

class DailyWeatherParameters(BaseModel):
    temperature_2m_max: float = Field(..., description="Maximum daily air temperature at 2 meters above ground.")
    temperature_2m_mean: float = Field(..., description="Mean daily air temperature at 2 meters above ground.")
    temperature_2m_min: float = Field(..., description="Minimum daily air temperature at 2 meters above ground.")
    
    apparent_temperature_max: float = Field(..., description="Maximum daily apparent temperature (feels like).")
    apparent_temperature_mean: float = Field(..., description="Mean daily apparent temperature (feels like).")
    apparent_temperature_min: float = Field(..., description="Minimum daily apparent temperature (feels like).")
    
    precipitation_sum: float = Field(..., description="Sum of daily precipitation (including rain, showers and snowfall)")
    rain_sum: float = Field(..., description="Sum of daily rain.")
    showers_sum: float = Field(..., description="Sum of daily showers.")
    snowfall_sum: float = Field(..., description="Sum of daily snowfall.")
    precipitation_hours: float = Field(..., description="Number of hours with rain.")
    
    precipitation_probability_max: float = Field(..., description="Maximum daily precipitation probability.")
    precipitation_probability_mean: float = Field(..., description="Mean daily precipitation probability.")
    precipitation_probability_min: float = Field(..., description="Minimum daily precipitation probability.")
    
    weather_code: float = Field(..., description="The most severe weather condition on a given day")
    
    sunrise: int = Field(..., description="Sunrise time iso8601 format.")
    sunset: int = Field(..., description="Sunset time iso8601 format.")
    
    sunshine_duration: float = Field(..., description="Daily sunshine duration in seconds.")
    daylight_duration: float = Field(..., description="Daily daylight duration in seconds.")
    wind_speed_10m_max: float = Field(..., description="Maximum daily wind speed at 10 meters above ground.")
    wind_gusts_10m_max: float = Field(..., description="Maximum daily wind gusts at 10 meters above ground.")
    wind_direction_10m_dominant: float = Field(..., description="Dominant daily wind direction at 10 meters above ground.")
    shortwave_radiation_sum: float = Field(..., description="The sum of solar radiation on a given day in Megajoules per square meter.")
    et0_fao_evapotranspiration: float = Field(..., description="Daily sum of ET₀ Reference Evapotranspiration of a well watered grass field")
    uv_index_max: float = Field(..., description="Maximum daily UV index.")
    uv_index_clear_sky_max: float = Field(..., description="Maximum daily clear-sky UV index.")
