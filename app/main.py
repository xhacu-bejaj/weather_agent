import json
from app.agent.agent import Agent

def main():

    weather_agent = Agent()


    query = "What is the max temperature and precipitation in New York?"

    print(f"User Query: \"{query}\"")
    print("-" * 20)

    
    result = weather_agent.process_query(query)

   
    print("-" * 20)
    print("Agent Response:")
    print(json.dumps(result, indent=4))

if __name__ == "__main__":
    main()