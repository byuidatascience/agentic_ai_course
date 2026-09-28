# Summit Wireless: MCP practice repo

Ludwig's internet went out, and the Summit Wireless support bot told him there was no outage. In this repo, you fix that bot with MCP.

The folders are split by **who owns the code**:

| Folder | Owner | What it is |
|---|---|---|
| `network_ops/` | Network Ops team | An MCP server for outage lookups |
| `field_service/` | FieldPro (a vendor) | An MCP server for technician appointments |
| `support_bot/` | **You** (the chatbot team) | The agent |

In a real company, these folders would be three separate repos, and you would only ever see `support_bot/`. They're together here so you can run everything on one laptop.

## Setup

```bash
git clone <this repo's URL>
cd summit-wireless-mcp
uv sync
```

Copy `.env.example` to `.env` and paste in your Gemini API key.

## 1. stdio: the agent launches the server

```bash
uv run support_bot/agent.py
```

Try: `My internet in 83440 has been out for 20 minutes. What's going on?`

You only started **one** program. Where did the outage server come from? Look at `NETWORK_OPS` in `support_bot/agent.py`.

## 2. HTTP: the server is already running

Open **two** terminals.

```bash
# terminal 1: you are Network Ops. Start the server and leave it running.
uv run fastmcp run network_ops/outage_server.py:mcp --transport http --port 8000
```

```bash
# terminal 2: you are the chatbot team.
uv run support_bot/agent.py --http
```

Ask the same question. Watch terminal 1 while the agent works: every `POST /mcp` line is your agent talking to Network Ops.

Stop the agent, then start it again. Did the server restart? Now stop the server (Ctrl+C) and ask a question. What happens?

## 3. Fix Ludwig's whole night

Ludwig also booked a $79 technician visit he doesn't need. The vendor's server in `field_service/` can find and cancel appointments.

Connect the agent to **both** servers, so it can check the outage *and* cancel the visit in one conversation. You should only need to change the `target` in `support_bot/agent.py`.

Try: `Hi, it's Ludwig in 83440. My internet is out and I booked a technician for tomorrow. Do I still need them?`

<details>
<summary>Hint</summary>

`MCPAdapter` accepts a config with several servers:

```python
target = {"mcpServers": {
    "network": {"command": "python", "args": [str(NETWORK_OPS)]},
    "field":   {"command": "python", "args": [str(REPO / "field_service" / "scheduling_server.py")]},
}}
```

Tool names now get the server name as a prefix: `network_check_outage`, `field_cancel_appointment`.
</details>

## Stretch: be the billing team

Write `billing/billing_server.py` with a tool that gives a customer an outage credit. Connect it as a third server. What did you have to change in the agent besides the config?
