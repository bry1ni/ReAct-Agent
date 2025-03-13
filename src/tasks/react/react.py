from agents import Agent
from src.config.prompts import REACT_INSTRUCTIONS
from src.tools import TOOLS
from src.models import GPT4

react = Agent(
    name="react",
    model=GPT4,
    instructions=REACT_INSTRUCTIONS,
    tools=TOOLS,
    handoffs=None
)