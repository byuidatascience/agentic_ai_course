"""Summit Wireless support bot. Owned by the chatbot team: you.

Notice what's missing: no import from network_ops/, no hand-written wrapper,
no field names. Everything the agent knows about outages comes from the server.
"""
import asyncio
import sys
from pathlib import Path

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.mcp import MCPAdapter

load_dotenv()

REPO = Path(__file__).resolve().parent.parent

# stdio (Spider-Man): the agent launches Network Ops' server when it needs it.
NETWORK_OPS = REPO / "network_ops" / "outage_server.py"

# HTTP (Stark Industries): the server is already running; the agent only knows its URL.
NETWORK_OPS_URL = "http://127.0.0.1:8000/mcp"

SYSTEM_PROMPT = (
    "You are the customer support agent for Summit Wireless, an internet provider. "
    "Before suggesting troubleshooting or a technician visit, check for a known outage."
)


async def build_agent(target):
    async with MCPAdapter(target) as adapter:
        tools = await adapter.list_tools()
    print("Tools from MCP:", [tool.name for tool in tools])
    return create_agent("google_genai:gemini-flash-lite-latest", tools, system_prompt=SYSTEM_PROMPT)


async def main():
    target = NETWORK_OPS_URL if "--http" in sys.argv else NETWORK_OPS
    agent = await build_agent(target)

    messages = []
    while True:
        try:
            prompt = input("Customer: ")
            if prompt == "exit": break
        except EOFError:
            break
        messages.append({"role": "user", "content": prompt})
        result = await agent.ainvoke({"messages": messages})
        messages = result["messages"]
        print("Bot:", messages[-1].text)


if __name__ == "__main__":
    asyncio.run(main())
