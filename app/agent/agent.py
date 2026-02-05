from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langchain.agents.structured_output import ToolStrategy

from app.agent.tools import weather_tool
from app.models.schemas import DailyWeatherParameters

SYSTEM_PROMPT = """
    You are a helpful weather assistant that provides accurate
    and concise weather forecasts based on user requests. 
    Use the provided tools to fetch weather data as needed.
    """


model = ChatOllama(
    model="llama3.1:8b",
    
)

agent = create_agent(
    model,
    tools=[weather_tool],
    response_format=ToolStrategy(DailyWeatherParameters),
    system_prompt=SYSTEM_PROMPT,
)


