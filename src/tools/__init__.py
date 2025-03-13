from src.tools.lookup_student_info import lookup_student_info
from agents import WebSearchTool

TOOLS = [lookup_student_info, WebSearchTool(user_location={"type": "approximate", "city": "Algiers", "country": "Algeria"})]