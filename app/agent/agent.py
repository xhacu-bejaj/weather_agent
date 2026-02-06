from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langchain.agents.structured_output import ToolStrategy

from app.agent.tools import get_weather_by_location # Only import the super-tool
from app.models.schemas import DailyWeatherParameters

SYSTEM_PROMPT = """
    You are a helpful weather assistant that provides accurate
    and concise weather forecasts based on user requests.
    Use the get_weather_by_location tool to retrieve the weather forecast for any specified location.
    """


model = ChatOllama(
    model="llama3.1:8b",
    
)

agent = create_agent(
    model,
    tools=[get_weather_by_location], 
    response_format=ToolStrategy(DailyWeatherParameters),
    system_prompt=SYSTEM_PROMPT,
)


