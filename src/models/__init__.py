from agno.models.openai import OpenAIChat
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
# Load the model
GPT4 = OpenAIChat(id="gpt-4")