# Lesson 1.6 revision notes

Live files: `lecture_slides/slide1_6.qmd`, `notebooks/notebook1_6.ipynb`, `drafts/summit-wireless-mcp/`.

## Scope cut (decided 2026-09-29, while designing 1.7)

1.6 runs long. Trim it to **what MCP is + connect over HTTP**. Move the rest into 1.7:

- **stdio moves to 1.7.** 1.6 focuses on HTTP (Stark Industries: server already running, agent hits a URL).
  The "Two ways to connect" / "Same server, two transports" slides and the stdio half of the
  Summit repo exercise are candidates to cut or shrink to a one-line teaser.
- **Multiple servers on one agent moves to 1.7.** Cut or move:
  - "Fix Ludwig's whole night" (network + field `mcpServers` config)
  - "Keep plugging things in" (docs + fetch config)
  - Summit README section 3 and the billing stretch
- Keep: Ludwig story, wrapper failure, brainstorm, smallest server/agent, Colab, how it works,
  LangChain docs MCP on their own agent (single HTTP server).

## Done

- 2026-09-29: Replaced the "Next time" slide. It promised pulling the Canvas server off GitHub and
  judging whether it is maintained, current, and safe. It now teases 1.7 (ready-made servers,
  several on one agent).

## Not done yet

- The cuts above are noted, not made. Make them when 1.7's design is settled, so nothing falls
  through the gap between the two days.
