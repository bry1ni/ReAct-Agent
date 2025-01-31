import os
import inspect
import importlib.util

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