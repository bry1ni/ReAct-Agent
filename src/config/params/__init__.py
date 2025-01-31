from .utils import load_json
import os

# Define paths to the JSON configuration files
CONFIG_DIR = os.path.dirname(__file__)
GENERATION_PARAMS_PATH = os.path.join(CONFIG_DIR, "generation_params.json")

GENERATION_PARAMS = load_json(GENERATION_PARAMS_PATH)