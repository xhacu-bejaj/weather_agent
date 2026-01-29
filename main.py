import os
from dotenv import load_dotenv
from app.agent.agent import agent

def main():

    result = agent.invoke({
        "messages":[{
            "role":"user",
            "content":"Get the weather forecast for latitude 45.6874 and longitude 12.6386 including maximum temperature, minimum temperature, and precipitation sum."
        }]
    }
    )

    print(result)


if __name__ == "__main__":
    main()
