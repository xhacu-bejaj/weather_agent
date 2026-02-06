from app.agent.agent import agent


def start_interactive_session(query: str):
    """
    Runs the weather agent with a given query and prints the streamed response.
    """
    for chunk in agent.stream(
        {"messages": [{"role": "user", "content": query}]}, stream_mode="values"
    ):
        latest_message = chunk["messages"][-1]
        if latest_message.content:
            print(f"Agent: {latest_message.content}")
        elif latest_message.tool_calls:
            tool_names = [tc["name"] for tc in latest_message.tool_calls]
            print(f"Calling tools: {', '.join(tool_names)}")
