from .utils import create_workflow
from langgraph.graph import MessagesState
from langgraph.checkpoint.memory import MemorySaver
import uuid

# Create the workflow
workflow = create_workflow(MessagesState)
memory = MemorySaver()

thread_id = str(uuid.uuid4())
config = {"configurable": {"thread_id": thread_id}}