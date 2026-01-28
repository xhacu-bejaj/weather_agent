from app.agent.tools import weather_tool
import re

# Mock Agent 
class Agent:
    def __init__(self):
        # A simple mapping of known locations to their coordinates
        # will be substituted with geocoding (location --> lat/lon) 
        self.known_locations = {
            "new york": (40.7128, -74.0060),
            "london": (51.5074, -0.1278),
            "tokyo": (35.6895, 139.6917),
        }
        
        self.parameter_mappings = {
            "temperature": ["temperature_2m_mean"],
            "max temperature": ["temperature_2m_max"],
            "min temperature": ["temperature_2m_min"],
            "precipitation": ["precipitation_sum"],
            "wind": ["wind_speed_10m_max", "wind_direction_10m_dominant"],
        }

    def process_query(self, query: str):
        query = query.lower()
        
        
        latitude, longitude = None, None
        for loc, coords in self.known_locations.items():
            if re.search(r'\b' + loc + r'\b', query):
                latitude, longitude = coords
                break
        
        if latitude is None or longitude is None:
            return {"error": "Sorry, I don't know that location. Please be more specific."}

        
        user_params = []
        temp_query = " " + query + " " # Add spaces for better regex word boundary matching
        
        # Sort keys by length descending to match longer phrases first
        sorted_keywords = sorted(self.parameter_mappings.keys(), key=len, reverse=True)

        for keyword in sorted_keywords:
            if re.search(r'\b' + keyword + r'\b', temp_query):
                user_params.extend(self.parameter_mappings[keyword])
                # Remove the matched keyword from the query to prevent re-matching shorter substrings
                temp_query = temp_query.replace(keyword, "")
        
        
        if not user_params:
            user_params = ["temperature_2m_mean", "precipitation_sum", "weather_code"]

       
        user_params = list(dict.fromkeys(user_params))

        
        print(f"Agent identified location: ({latitude}, {longitude})")
        print(f"Agent identified parameters: {user_params}")
        
        weather_data = weather_tool(
            latitude=latitude,
            longitude=longitude,
            user_params=user_params
        )
        
        return weather_data
