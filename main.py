from app.agent.agent import agent

def main():

    for chunk in agent.stream({
        "messages":[{"role":"user","content":"Get the weather forecast for latitude 45.6874 and longitude 12.6386 including maximum temperature, minimum temperature, and precipitation sum."}]
    }, stream_mode="values"):
        latest_message = chunk["messages"][-1]
        if latest_message.content:
            print(f"Agent: {latest_message.content}")
        elif latest_message.tool_calls:
            print(f"Calling tools: {[tc['name'] for tc in latest_message.tool_calls]}")

    

if __name__ == "__main__":
    main()
