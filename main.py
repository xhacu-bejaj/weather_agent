from app.services.chat_service import start_interactive_session
# TODO: Add memory to the agent 
# TODO: Add more tools to the agent (e.g., historical weather data, weather alerts, etc.)
# TODO: fastapi integration for API access to the agent
def main():
    query = input("Enter your weather query: ")
    start_interactive_session(query)


if __name__ == "__main__":
    main()