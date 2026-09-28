"""Outage lookup, published as an MCP server.

Owned by the Network Ops team. In real life this file lives in *their* repo,
next to the monitoring system it reads from. The support bot never imports it.
"""
from fastmcp import FastMCP

mcp = FastMCP("Network Ops")

# Stand-in for Network Ops' real monitoring database.
OUTAGES = {
    "83440": "Fiber cut reported at 9:15 PM. Crews on site, ETA 11:30 PM.",
    "83460": "Planned maintenance 1:00-3:00 AM.",
}


@mcp.tool
def check_outage(postal_code: str) -> str:
    """Check whether there is a known network outage in a postal code."""
    return OUTAGES.get(postal_code, "No known outages.")


if __name__ == "__main__":
    # stdio by default: whoever launches this file talks to it over stdin/stdout,
    # so never print() in here. stdout *is* the conversation.
    mcp.run()
