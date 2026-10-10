# Unit 1 (Build): One Things

Unit destination: a powerful personal-use agent that does meaningful things for the student.

Each day: the **one thing** (teacher-facing: what to protect if nothing else happens), the **destination** (student-facing: "I did that"), then objectives tagged with ids from `course_design/course_outcomes.md`. Settled top-down; topics and content come after.

## 1.1 — Settled

**One thing:** Give them the thrill of a first LLM call, then hand them the controls.

**Destination:** "I called an LLM from my own code for the first time, then went a step further, changing its behavior through system prompts and model settings."

**Objectives (draft):**
- Explain what agent engineering is and how it differs from prompt and software engineering — 4.1.3
- Obtain a Gemini API key from AI Studio — 1.2.1
- Call an LLM provider's API from code and read the response — 1.2.1
- Find model parameters in the provider's documentation — 5.1.2
- Change a model's behavior with a system prompt and settings like temperature, and describe what changed — 1.2.3

Notes: the first call took only ~30 min last time, so the leftover class time goes to model features. The prep introduces agent engineering vocabulary.

## 1.2 — Settled

**One thing:** They see what's underneath an agent: a model, tools, and memory they can find and assemble themselves.

**Destination:** "I know the parts of an agent (a model, tools, and memory) and where to find each one in the docs."

**Objectives (draft):**
- Describe an agent and its parts: a model, tools, and memory — 4.1.1
- Find each part of an agent in the framework's docs — 5.1.1
- Build a working agent from scratch in a fresh Colab
    - Give the agent a custom tool — 1.5.1
    - Give the agent short-term memory — 1.4.1

Previous one thing: "Understand the basic scaffold of an agent" — 1.4.1, 1.5.1, 4.1.1

Lessons from teaching it:
- Prep (the LangChain quickstart) didn't work for students; doc-reading skills need developing.
- What worked: a fresh Colab together, students find each piece in the docs and try to assemble it before the next step is shown.
- Needs a better story, and more structured, guided exploration of the docs.

## 1.3 — Settled

**One thing:** Groups form that will actually work well together.

**Destination:** "I found a well-balanced group I work well with, and we proved it by fixing a broken agent together."

**Objectives (draft):**
- Choose a well-balanced project group — 5.2
- Define an agent together as a group — 4.1.1
- Help teammates fill gaps in their understanding of agents — 4.1.1
- Improve a weak tool description so the agent uses the tool correctly — 1.3, 1.5.1
- Troubleshoot a broken agent together — ?

Previous one thing: "Organize groups and work together on an activity" — competencies unclear (3.1 or 1.3?)

Lessons from teaching it:
- Besides forming groups, the day reinforced 1.2.
- Activity: groups got a bad tool description and improved it. Students were creative.
- Keep the focus on reinforcement activities.

## 1.4 — Settled

**One thing:** Everyone leaves with an agent idea worth building and a machine that can build it.

**Destination:** "I have an idea of what I want my own agent to do, and my computer is ready to build it."

**Objectives (draft):**
- Brainstorm what a personal agent could do for them, and choose an idea for Project 1 — 3.1, 5.5
- Set up a local environment for building agents — 1.1
- Run an agent with a tool and short-term memory on their own machine — 1.5.1, 1.4.1
- Publish their local agent repository publicly — 4.2.1
- Help a neighbor get through setup

Previous one thing: copy of 1.3 ("Organize groups…"). Outline topic: set up tools and memory locally — 1.5.1, 1.4.1

Lessons from teaching it:
- The day was just local environment setup, and it took a while.
- Pace varied widely: some never finished, some finished fast. Fast finishers need an invitation to help neighbors and a way to keep practicing.
- Missing: students brainstorming use cases for their own agent. Project 1 is a customized agent, and it's easier to build with an idea in hand. Consider opening class with the brainstorm and a Project 1 intro, before setup.

Open questions (for the day's design):
- How much setup happens before class vs. in class vs. after?
- Which setup kinks did students hit? Warning them ahead could smooth it.
- Students didn't use their agents because they were hard to access. Address here (1.4)?

## 1.5 — Settled

**One thing:** Nobody heads into the weekend behind.

**Destination:** "My agent is caught up and ready for me to build on over the weekend."

**Objectives (draft):**
- Discuss AI ethics and begin forming a personal conviction — 6.1, 6.2
- Work out why an agent would delegate to a sub-agent, then build one — 1.7
- Finish setup and get their own agent running locally — 1.1
- Plan what they'll add to their agent over the weekend — 3.1

Previous: outline "Sub-agents as tools, basic prompting" — 1.7, 1.3, 1.2.2. Instructor notes: "Implement solutions from others' functions (community tools, etc.)"

Direction:
- Open with the ethics discussion (from an ethics reading). It went well but doesn't fill a day.
- Add a problem-solution ladder where students derive and build a subagent themselves. Teach it succinctly; subagents are really a Unit 3 topic (context engineering).
- Use the rest as a work day: catch up from 1.4 setup, and leave ready to work on their own agent over the weekend.
- Students need something good to do over the weekend, ideally moving their agent toward something they'll actually use.
- Maybe introduce MCP here? (undecided)

## 1.6 — In progress

**One thing:** They can explain MCP to a classmate in their own words, including its reason for existing and the problems it solves.

**Destination (draft):** "I got an MCP server working with my agent."

**Objectives (draft):**
- Explain why MCP exists and the problems it solves — 4.3.1, 1.5.2
- Identify MCP-shaped problems: problems an MCP server would solve — 1.5.2
- Write async Python well enough to run an agent with MCP tools — 1.1
- Connect a provided MCP server to their agent — 1.5.2

Students work with MCP servers provided in class.

Previous: instructor notes "Use an MCP (Slack/Canvas)"; lesson-design skill "Understand MCP well enough to use it on their own," destination "my own agent is plugged into the LangChain docs MCP" — 1.5.2

Lessons from teaching it:
- Went OK, but students needed async as a prerequisite. Async should be an objective.
- Slides weren't satisfying; content needs revision.
- Students didn't get enough chance to derive MCP's purpose and explain it to each other.

## 1.7 — In progress

**One thing:** They can find, judge, and connect an MCP server without help.

**Destination:** "I found an MCP server I actually need and added it to my agent on my own computer."

**Objectives (draft):**
- Find an MCP server that fills a gap in their own Project 1 agent — 5.1.2
- Judge whether an MCP server is maintained and safe to trust before connecting it — 5.4
- Differentiate between stdio and HTTP servers, and explain the difference to a friend — 1.5.2, 4.1
- Run one agent with several MCP servers at once by adding them to a single config — 1.5.2
- Explain why more servers means more power and more confusion for the agent — 1.5.2

Previous (drafts/lesson1_7/README.md, approved 2026-09-30): one thing "You don't need to build common capabilities like browsing or files. Someone already ships them as a server." Destination "My Project 1 agent runs with 3+ MCP servers at once (docs, filesystem, plus one I picked)." Transport split was: 1.6 HTTP, 1.7 introduces stdio.

## Unit shape — open threads (2026-10-10)

1. **Where does Unit 1 end?** After 1.8 is appealing: students have enough for Unit 2 to start diagnosing. But not all students reached an "unwieldy, powerful agent" by week 4, and 1.8 as a work day leaves gaps.
2. **Long-term memory.** Not enough time to teach it, but valuable now while they build their own agent. Could move to Unit 3.
3. **The agent as its own coding agent.** Students with unwieldy agents mostly used coding agents (not allowed; defeats the purpose). Idea: once they have a filesystem MCP, they set up their own agent to work on itself.
4. **Version history.** Biggest gap: an agent that edits itself can break itself, and they need a way to revert (git).
5. **AI coding in week 4 (1.9–1.11)?** Being debated.
6. **Priming failure-spotting.** Students should notice and point out failures throughout Unit 1, before Unit 2 teaches it explicitly. No framework for this yet.
