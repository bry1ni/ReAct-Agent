from src.tasks.react import react

query_test = "what's Ryan ibrahim's biography ? and what is he studying atm ?"

response = react.run(
    query_test,
    images=None,
    show_reasoning=True
)

assistant_response = next(
    (msg.content for msg in response.messages if msg.role == "assistant" and msg.content), 
    None
)
print(assistant_response)