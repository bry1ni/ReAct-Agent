import os
import json

def load_json(file_path):
    """
    Load a JSON file and return its content as a Python dictionary.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        dict: Parsed JSON content.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)
