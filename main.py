import os
from dotenv import load_dotenv

from langchain_core.messages import HumanMessage, AIMessage
from app.agent.agent import agent

def main():

    result = agent.invoke({
        "messages":[HumanMessage(content="Get the weather forecast for latitude 45.6874 and longitude 12.6386 including maximum temperature, minimum temperature, and precipitation sum.")]
    }
    )

    for element in result["messages"]:
        print("Result Element:")
        print("----------------")
        print(element)

    
    
    

if __name__ == "__main__":
    main()
