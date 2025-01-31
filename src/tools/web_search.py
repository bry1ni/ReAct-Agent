from tavily import TavilyClient
from langchain_core.tools import tool

tavily_client = TavilyClient(api_key="TVLY_API_KEY")

@tool
def web_search(query: str):
    """
    Search the internet for information.

    Args:
        query (str): Focused search query about the asked topics.
                    Include specific technical terms if required for better results.

    Returns:
        dict: Search results containing:
            - Relevant web pages
            - Snippets of information
            - Source URLs
            - Relevance scores
    """
    response = tavily_client.get_search_context(query)
    return response