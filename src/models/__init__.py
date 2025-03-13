from agents import OpenAIChatCompletionsModel, set_tracing_disabled
from openai import AsyncOpenAI
from dotenv import load_dotenv, find_dotenv
import os
load_dotenv(find_dotenv())

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
set_tracing_disabled(disabled=True)

# Load the model
GPT4 = OpenAIChatCompletionsModel(model="gpt-4", openai_client=client)