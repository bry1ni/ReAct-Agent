import json
import os
import inspect
import importlib.util
from typing import Any

def format_tool_output(tool_message: Any) -> str:
    """
    Formats the tool message into a JSON string ensuring it's always a valid str.
    
    Args:
        tool_message (Any): The tool message to be converted (typically a dict).
    
    Returns:
        str: JSON formatted string representation of the tool message.
    """
    return json.dumps(tool_message, ensure_ascii=False)

def get_all_tools():
    """
    Dynamically retrieves all callable tool functions from the tools directory.
    """
    tools_dir = "src/tools"
    tool_functions = []

    # Iterate through all .py files in the tools directory
    for filename in os.listdir(tools_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = f"src.tools.{filename[:-3]}"  # Strip .py extension for module name
            module_spec = importlib.util.spec_from_file_location(module_name, os.path.join(tools_dir, filename))
            if module_spec and module_spec.loader:
                module = importlib.util.module_from_spec(module_spec)
                module_spec.loader.exec_module(module)

                # Inspect members of the module
                for name, obj in inspect.getmembers(module):
                    # Check if the object is callable and has attributes like `func` or `name`
                    if callable(obj) and hasattr(obj, "func") and hasattr(obj, "name"):
                        tool_functions.append(obj)
    return tool_functions

# you can create your own decator tool @tool