from .utils import load_prompt
import os

# Define paths to the `.md` files
PROMPTS_DIR = os.path.dirname(__file__)
REACT_INSTRUCTIONS_PATH = os.path.join(PROMPTS_DIR, "react.md")

# Load prompts
REACT_INSTRUCTIONS = load_prompt(REACT_INSTRUCTIONS_PATH)