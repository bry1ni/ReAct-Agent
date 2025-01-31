from langgraph.graph import END, START, StateGraph, MessagesState
from src.config.prompts import REACT_INSTRUCTIONS
from langchain_core.messages import HumanMessage, SystemMessage
from src.tools import TOOLS
from src.models import GPT4
from langgraph.prebuilt import ToolNode

bound_model = bound_model = GPT4.bind_tools(TOOLS)
tool_node = ToolNode(TOOLS)

def should_continue(state: MessagesState):
    """Return the next node to execute."""
    last_message = state["messages"][-1]
    # If there is no function call, then we finish
    if not last_message.tool_calls:
        return END
    # Otherwise if there is, we continue
    return "action"

# Define the function that calls the model
def call_model(state: MessagesState):
    response = bound_model.invoke(state["messages"])
    # We return a list, because this will get added to the existing list
    return {"messages": response}

def create_workflow(state: MessagesState):
    # Define a new graph
    workflow = StateGraph(state)

    # Define the two nodes we will cycle between
    workflow.add_node("agent", call_model)
    workflow.add_node("action", tool_node)

    # Set the entrypoint as `agent`
    # This means that this node is the first one called
    workflow.add_edge(START, "agent")

    # We now add a conditional edge
    workflow.add_conditional_edges(
        # First, we define the start node. We use `agent`.
        # This means these are the edges taken after the `agent` node is called.
        "agent",
        # Next, we pass in the function that will determine which node is called next.
        should_continue,
        ["action", END]
    )

    # We now add a normal edge from `tools` to `agent`.
    # This means that after `tools` is called, `agent` node is called next.
    workflow.add_edge("action", "agent")

    return workflow

def send_user_message_with_stream(query, app, config, memory, stream_mode="none"):
    """
    Sends a user message to the app and retrieves the response, optionally handling streaming.
    
    Parameters:
        - message: The user-provided message.
        - app: The conversational AI application instance.
        - config: Configuration details for the interaction.
        - memory: A dictionary-like structure for state or past interactions.
        - stream_mode: The mode of streaming. "none" for regular, "values" for streamed responses.

    Returns:
        - The final response (either from streaming or full message content).
    """
    # Add the user message to the state
    if memory.get(config):
        inputs = {"messages": [HumanMessage(query)]}
    else:
        # Add initial state (prompt) with the user query
        inputs = {
            "messages": [
                SystemMessage(REACT_INSTRUCTIONS),
                HumanMessage(query),
            ]
        }

    # Handle streaming
    if stream_mode != "none":
        stream = app.stream(inputs, config, stream_mode=stream_mode)
        for s in stream:
            for m in s["messages"]:
                if isinstance(m, tuple):
                    print(m)
                else:
                    m.pretty_print()
        return "Streamed response completed."  # Optional feedback for the caller.

    # Handle regular invocation
    response = app.invoke(inputs, config)
    llm_response = response["messages"][-1].content
    return llm_response