import asyncio
from src.tasks.react import react
from agents import Runner

query_test = "what's Ryan ibrahim's biography ? and what is he studying atm ?"

async def run_react(agent=react, query=query_test):
    result = await Runner.run(
        agent,
        query,
    )
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(run_react())