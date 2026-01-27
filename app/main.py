import os

from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_agent

#load_dotenv()

#api_key = os.getenv("GOOGLE_API_KEY")

SYSTEM_PROMPT = """You are a helpful assistant that provides weather information
"""

def get_weather(location: str) -> str:
    """Get weather for a given city."""
    return f"The weather in {location} is sunny with a high of 25°C."

agent = create_agent(
    model = "google_genai:gemini-2.5-flash",
    tools=[get_weather],
    system_prompt="You're a helpful assistant that provides weather information, you can use the get_weather tool to fetch weather data, always end the response with a friendly note.",
)

response = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather like in New York?"}]}
)

print(response["messages"][-1].content)