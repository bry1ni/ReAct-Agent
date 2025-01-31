from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv, find_dotenv
from src.config.params import GENERATION_PARAMS

load_dotenv(find_dotenv())
# Load the model
GPT4 = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), 
                  temperature=GENERATION_PARAMS["models"]["openai"]["llm"]["temperature"], 
                  model=GENERATION_PARAMS["models"]["openai"]["llm"]["name"])