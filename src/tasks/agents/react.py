from src.tasks.agents import workflow, memory

app = workflow.compile(
    checkpointer=memory,
    interrupt_before=[],  # Add node names here to update state before they're called
    interrupt_after=[],  # Add node names here to update state after they're called
    )
