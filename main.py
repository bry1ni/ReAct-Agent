from src.tasks.agents.react import app
from src.tasks.agents.utils import send_user_message_with_stream
from src.tasks.agents import memory, config

# Interact with the agent
query_test = "what's Ryan ibrahim's biography ? and what is he studying atm ?"

response = send_user_message_with_stream(query_test, app, config, memory, stream_mode="none")
print(response)