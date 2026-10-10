# Lesson 1.7 design log

**Outline line:** 1.7 - MCP deepen uses: file system, web browsing - [1.5.2]

## Status (as of 2026-09-29)

> **2026-09-30: files published but NOT approved.** The user ran out of time, so the prototypes were
> moved to their final paths and rendered as-is. The user will go back and revise them later.
> Treat all three as unapproved Phase 4 drafts, not finished work:
>
> - `lessons/lesson1_7.qmd` (was `drafts/lesson1_7/lesson1_7.qmd`)
> - `lecture_slides/slide1_7.qmd` (was `drafts/lesson1_7/slides1_7.qmd`)
> - `notebooks/notebook1_7.ipynb` (was `drafts/lesson1_7/notebook1_7.ipynb`)
>
> Wherever this log says `drafts/lesson1_7/...` for these files, read the new paths above.
> `slides1_7.html`, `slides1_7_files/`, and `_shot*` here are stale render output from the draft.

- Phase 1: **approved**.
- Phase 2: story and beats **approved**. The Reveal diagrams are **not committed**. The user wants to
  see what the Reveal instruction looks like first.
- Phase 2 objectives: **approved** (2026-09-30).
- Phase 3 module outline: **approved** (2026-09-30). Prep and practice direction are still open (see Outline).
- Phase 4: prototyping. Notebook first, then slides for modules 3 and 5.
- **Pick up here:** notebook prototype `drafts/lesson1_7/notebook1_7.ipynb`. It was tested in Colab on 2026-09-30 (see
  "Colab test results"). Sections 1–7 pass. Still open: the "I can't" vs. made-up papers story beat, and the 33-tool list. The slides for modules 3 and 5 come after that.

## Lesson page prototype (2026-09-30)

`drafts/lesson1_7/lesson1_7.qmd` follows `lessons/_example.qmd`. All links point at the **final** paths, so they
work once files are moved and rendered:

- Slides: `https://byuidatascience.github.io/agentic_ai_course/lecture_slides/slide1_7.html` (from `lecture_slides/slide1_7.qmd`)
- Notebook (Colab): `https://colab.research.google.com/github/byuidatascience/agentic_ai_course/blob/main/notebooks/notebook1_7.ipynb`
- Lesson: `.../lessons/lesson1_7.html`, prep `.../preps/prep1_7.html`, practice `practice/practice1_7.ipynb`
- Not written yet: prep1_7, practice1_7, lesson1_6, lesson1_8, practice1_6 (Before Class links to it), and a rewrite of notes1_7.
- Not added yet: navbar entry in `_quarto.yml`, Day 7 row in `lessons/unit1.qmd`.

## Colab test results (2026-09-30)

- **Works:** `uvx arxiv-mcp-server` (19 tools) and `npx @modelcontextprotocol/server-filesystem` (Colab has
  Node). Two servers make 33 tools, prefixed `arxiv_` / `files_`. The "Next Friday" beat works in code: the lab folder
  is empty, and the papers are in `~/.arxiv-mcp-server/papers`. The filesystem server refuses writes outside its folder
  ("Access denied - path outside allowed directories"), which could be a teaching moment.
- **Fixed:** stdio fails in Colab (`fileno`) because the subprocess inherits Jupyter's stderr. Fix: a "Colab quirk" cell
  that sets `sys.stderr` to a file and turns fastmcp logging down to WARNING (that also removes the INFO log noise).
  The live 1.6 notebook uses stdio too, so it probably has the same bug.
- **Fixed:** the model assumed it was 2024 when choosing the search dates. Today's date now goes in the system prompt.
- **Fixed:** asking for 4 files (notes plus the digest) gave `MALFORMED_FUNCTION_CALL`. It now asks for one short `digest.md`.
- **Open, story:** the no-tools agent did **not** say "I can't". It invented 3 plausible fake papers
  ("hypothetical" arXiv IDs) and wrote a digest of them.
- **Model is now `gemini-flash-lite-latest`** (the user's choice). gemini-2.5-flash hit the free tier's 20 requests
  per day partway through one run of the notebook, and gemini-2.5-flash-lite wrote bad queries and gave up.
  flash-lite-latest runs the whole notebook. Its quota under a full class is still unchecked.
- **Fixed, papers now show up in the lab folder:** the filesystem server gets two allowed folders (`LAB_FOLDER`, `ARXIV_FOLDER`),
  and the prompt asks the agent to move each paper's `.md` into the lab folder. Verified end to end: `lab_papers` ends up
  with 3 papers plus `digest.md`, via `files_move_file` (19 tool calls). It left the `.meta.json` files behind, which is fine.
  It also read each paper in full before moving it, which costs tokens but isn't a problem.

## Module outline (approved)

| # | What | How | Where | Outcome |
|---|---|---|---|---|
| P | *open:* setup checklist (uv, maybe Node) for the local Apply, maybe plus a reading | | prep | |
| 1 | Problem: the scoop, then Mateo's Fridays, then "I can't." | narrated story | slides | 5.5 |
| 2 | Brainstorm: "What would the agent need?" | groups for 1–2 min, follow-ups in notes | slides + notes | 1.5.2 |
| 3 | Reveal: someone ships it. arXiv MCP server, stdio vs HTTP | instructor-led | slides | 1.5.2, 4.1 |
| 4 | Try it: arXiv server, change the topic | run cells | notebook | 1.5.2 |
| 5 | Next Friday: can't find last week's paper | story beat | slides | 1.5.2 |
| 6 | Add the filesystem server: one agent, two servers | edit config, rerun | notebook | 1.5.2 |
| 7 | Pair quiz (see below) | pairs, then instructor reveal | slides | 1.5.2, 4.1 |
| 8 | Apply: own P1 agent with docs + filesystem + one they pick | local | lesson → practice | 1.5.2, 5.1.2 |

**Module 7 pair quiz (quick in-class quiz):** pairs (a) define the stdio/HTTP difference, (b) explain what
problems MCP solves, (c) name what's in an MCP server (prompts, resources/documents, tools), and (d) look at two
code snippets side by side and decide which is stdio and which is HTTP, and where the processing happens
for each. Then the instructor reveals the answers and re-explains. This is where the Reveal diagrams / slides come back.

**Practice (proposed, not confirmed):** finish the destination, then automate a new routine with a different server
combination (e.g. fetch + filesystem), and end with "what routine of yours could this take over?"

## Objectives (approved)

1. **Connect** a ready-made stdio MCP server (arXiv) to an agent and use its tools. `[1.5.2]`
2. **Explain** how stdio and HTTP transports differ. `[1.5.2, 4.1]`
   Include a brief pair moment where students describe the difference to each other.
3. **Run** one agent with several MCP servers at once by adding servers to a single config. `[1.5.2]`
4. **Find** an MCP server that fills a gap in your own Project 1 agent, and connect it. `[5.1.2]`
   Not 5.4: evaluating servers is out of scope.

Not an objective: "don't build what someone already ships." The story carries it.

## Decisions

- **Most Important Thing (approved):** You don't need to build common capabilities like browsing or
  files. Someone already ships them as a server.
- **Destination (approved):** My Project 1 agent runs with 3+ MCP servers at once (docs, filesystem,
  plus one I picked).
- **Story culmination:** multiple MCPs on a single agent.
- **Transport split:** 1.6 focuses on HTTP; 1.7 introduces stdio (the ready-made servers here are stdio).
  Re-use the Spider-Man (stdio) / Iron Man (HTTP) analogy from `instructor_notes/notes1_6.qmd`.
- **Visual (tentative):** possibly reuse the client/transport/server diagram from `scratch/mcp_deck.qmd`
  ("The mental model first"), with more iteration. The user will describe the changes. It's not
  committed until the Reveal instruction is prototyped.
- **Safety evaluation of servers is out of scope** (not enough research time). See future directions.
- 1.6 scope is cut to make room. See `drafts/lesson1_6/README.md`.
- Subagents (1.5) are background knowledge, not a planned contrast.

## Story: Mateo's Friday digest (approved)

Framing: **automation.** A tedious routine an agent *could* do but *can't reach*. The agent doesn't do
something wrong. Use-case map: move `ucmap-automation` from 1_6 to 1_7 in `drafts/_use_case_map_TEMP.md`.
This is a new story, not a continuation of Summit Wireless.

- **The miss:** at a conference, the lab learns a paper scooped their project. It was in the arXiv
  results three weeks earlier, and Mateo skimmed past it in a rush.
- **Why it keeps happening:** Mateo, an undergrad RA, spends every Friday 1–4 PM searching arXiv,
  saving papers to the lab folder, and writing the digest (about 150 hrs/yr).
- **"I can't":** he asks his AI agent to do it, and it replies with an ominous "I can't."
  Hidden cause: the model is capable but has no reach.
- Keep it brief on the slides. No essay.

## Beats (approved)

1. **Problem:** the scoop → Mateo's Fridays → *"I can't."* There's no "follow the code" beat; the problem
   is self-explanatory.
2. **Brainstorm (1–2 min):** the slide asks only "What would the agent need?" Follow-ups go in the
   instructor notes: you can write tools (1.4), but should you, and who maintains them (1.6)? Would
   someone already have built these? Two servers means two agents? Where do they run? (stdio / Spider-Man)
3. **Reveal:** someone already ships it. The arXiv MCP server, stdio / Spider-Man, maybe the diagram (not committed).
4. **Try it:** arXiv server only. Change the research topic.
5. **Next Friday:** Mateo can't find last week's paper. He used to download papers himself and stopped once
   the agent took over.
6. **Add the filesystem server** to the same config: one agent, two servers. Papers appear in the folder.
7. **Apply:** their own Project 1 agent gets docs (HTTP), filesystem, and one server they pick (the destination).

**v2 idea (not for first ship):** after the brainstorm, show Mateo writing a web-scraping script from
scratch, and then the website changes and it breaks. Add it only once everything else is solid.

## Environment (proposed, untested)

Colab for the story and no cloned repo. Both servers are stdio via `uvx` on the Colab VM (needs
`!pip install uv`). The filesystem server acts on Colab's disk, so saved papers show up in the Files
pane. The own-agent Apply step is local.

## Feasibility notes (from a web search on 2026-09-29, test in Phase 4)

- arXiv: `uvx arxiv-mcp-server` (blazickjp, stdio). Has search_papers and download_paper, which saves
  papers as Markdown. Exposes about 19 tools. `--storage-path` sets where papers are saved.
- Files: `uvx filesystem-mcp <folder>` (kujirahand, Python, no Node needed), or the official Node
  server (`npx`, needs Node).
- Optional third server: `uvx mcp-server-fetch`.
- **Story risk:** `download_paper` already saves to the server's own hidden folder. Phase 5 has to
  hold up anyway: that folder isn't the lab's shared folder. Don't point `--storage-path` at the lab folder.
- **Class risk:** a whole class on one campus IP could hit arXiv rate limits, and 19 tools crowd the tool list.

## Future directions (not this lesson)

- Judging an MCP server before connecting it: who maintains it, is it current, what can its tools
  change, is it safe (outcome 5.4). Needs research first. Candidates: Unit 3 or the 1.8 ethics day.
- A Canvas MCP dissection (was in `instructor_notes/notes1_7.qmd`, now superseded).
- Two 1_7 entries in `drafts/_use_case_map_TEMP.md` (software-technology, it-devops) were planned
  around server judging (5.4). They need a new home.
