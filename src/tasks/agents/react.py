from src.tasks.agents import workflow, memory
from IPython.display import Image

app = workflow.compile(
    checkpointer=memory,
    interrupt_before=[],  # Add node names here to update state before they're called
    interrupt_after=[],  # Add node names here to update state after they're called
    )

agent_graph = Image(app.get_graph().draw_mermaid_png())