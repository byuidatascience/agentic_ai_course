# Lesson 1.2 Planning

Compiled planning notes for Day 2 (Unit 1, Lesson 2), confirmed with instructor one item at a time.
This file separates **MVP** (minimum viable, ship-first) scope from **Ideal** (fuller-treatment) scope
where they diverge.

**Files in this folder:**
- `planning.md` — this file
- `use-case-draft.qmd` — first working spike testing use-case plausibility (superseded by `lesson1_2.qmd`, kept for history)
- `lesson1_2.qmd` — the drafted lesson page, site-template shaped, ready to review
- `practice1_2.qmd` — drafted take-home practice

**Open call made while drafting `lesson1_2.qmd`:** "Apply It" (Supply Chain) was placed as the final
**in-class** activity, not take-home — even though `lessons/_use_case_map_TEMP.md` tags Supply Chain as
`type: practice`. That map is an explicitly throwaway planning file, and the instructor's own narration
("they apply it to a fresh problem" as the last step of the day) read as in-class independent work to me.
Flagging in case Supply Chain was actually meant to be the take-home instead of the separate
pick-your-own-domain practice drafted in `practice1_2.qmd`.

---

## 1. Course competencies addressed — ✅ confirmed

Day 2 scope, per instructor:

- **Agent anatomy / scaffold** (supporting, not a standalone competency id — underlies 1.1 and sets up 1.3/1.4)
  - LLMs are stateless
  - What a manual conversation flow looks like without a framework
  - How LangChain's `create_agent` simplifies that
  - The agent's tool-calling loop is *coded into* `create_agent`, not something inherent to the model provider
  - **MVP:** instructor explains verbally, lesson page carries just a line noting this
  - **Ideal:** a slide deck that visually points out the parts
- **1.4 Extend the agent with tools and services** → **1.4.1** Define, register, and invoke custom tools — **essential (MVP)**
  - Students should try a few different things with tools, not just one canned example
- **1.3 Give the agent memory and manage its context** → **1.3.1** Implement short-term memory — **essential (MVP)**
- **Ideal adds:** **4.1 Use current industry terminology correctly** — vocabulary practice

Source: [course_outcomes.md](../../course_design/course_outcomes.md), [irm.md](../../course_design/irm.md), instructor confirmation 2026-09-17.

## 2. Content students should already know — ✅ confirmed

Note: `lessons/lesson1_1.qmd` as currently written is itself outdated (Day 1 is being reworked); most of
it still holds, **except** that the in-class tool call is no longer how they first encounter one.

- Have a working Gemini API key stored in Colab Secrets, and know not to hardcode it
- Have installed `langchain` / `langchain-google-genai` in Colab
- Have called `create_agent(...)` / `agent.invoke(...)` at least once (Day 1 in-class)
- **Hopefully** (not guaranteed) encountered a tool call *and* memory, without understanding either, through the `create_agent` quickstart in their own prep reading going into Day 2 — not from in-class Day 1 work
- Not everyone will have gotten the quickstart running successfully on their own

Not yet known: what a tool actually is, the anatomy of tools in LangChain (what's essential vs. incidental),
the `@tool` decorator, docstrings-as-instructions, anything about memory/statelessness, or the internals of
`create_agent`'s loop.

**Action item — placement confirmed:** a standalone `.ipynb` example with just the bare quickstart, as a
fallback for students who couldn't get it running solo before class. Lives as its own example notebook
(not folded into prep or practice), linked from inside the lesson page. Not yet built.

## 3. Outcomes for the day — ✅ confirmed

By the end of Day 2, students will be able to:

1. Explain why LLMs need a framework to hold a conversation, and what `create_agent`'s loop actually does
2. Explain what a tool is and what differentiates it from a plain Python function
3. Build a custom tool to solve a problem and wire it into an agent
4. Explain what short-term memory is, and how it differs from long-term memory

Note: no separate "vocabulary" objective (competency 4.1, ideal scope) — it's not a distinct outcome.
Instead, 4.1 is served by being precise with wording in objectives 1–4 themselves (favoring explicit
"explain"/"define" verbs over vaguer ones), not by adding a fifth item.

## 4. Plans already in instructor notes — ⏳ pending confirmation

Revising my earlier read: `instructor_notes/notes1_2.qmd` turns out to line up well with the confirmed
scope above, not stale after all. Its content:

- **Most Important Thing:** "Understand the basic scaffold of an agent" — matches outcome 1
- **Objectives:** Principles of agents; Anatomy of `create_agent`; Structure of input/output; Introduce
  memory and tools
- **Practice:** "Inspect the structure of output, fill in the blank for memory, fill in the blank for tools"

Three of the four objectives map directly onto confirmed outcomes 1, 2/3, and 4. The fourth —
**"Structure of input/output"** — has been moved to **Lesson 1.1** instead (see
`drafts/lesson1_1/planning.md`): students are already calling `agent.invoke()` on Day 1, so that's where
understanding its input/output shape belongs, not Day 2.

The practice note ("inspect output structure, fill-in-blank for memory, fill-in-blank for tools") still
splits across both days now — the "inspect output structure" piece moves to 1.1's practice; "fill-in-blank
for memory" and "fill-in-blank for tools" stay here as candidates for item 7 below.

## 5. Known prep readings — ✅ confirmed

Serves competency **5.1 Learn from primary-source documentation and tutorials**.

- Use the [LangChain quickstart](https://docs.langchain.com/oss/python/langchain/quickstart) to get an agent with tools and memory running
- Spend no more than 30 minutes
- Toward the end of the quickstart: note that we are using LangChain Agents, not DeepAgents (for pedagogical purposes), and that we are not using tracing yet

## 6. Outline for lesson content — ⏳ pending confirmation

Per `lessons/_use_case_map_TEMP.md` (a throwaway planning map, not real content yet), Day 2 (`day: 1_2`)
already has two use cases planned, both currently tagged only for tools (1.4.1):

- **Retail — custom tool over store inventory** (`type: example`) — guided/instructor-led
- **Supply Chain — tool that answers "where is the shipment"** (`type: practice`) — student applies on their own

This happens to match what the instructor wants structurally: one use case for guided instruction, a
second for independent application, so abstraction starts to take hold. Proposed shape, folding in the
instructor's requirement that tools and memory be implemented and observed **separately** before being
combined:

1. **Anatomy explanation** (brief, per item 1 — MVP: instructor talks through it; Ideal: slide deck)
2. **Guided use case — Retail (inventory tool):**
   a. Build/demo the custom tool alone, see its effect (agent answers an inventory question via the tool)
   b. **Review step** (checkpoint discussion before moving on)
   c. Add short-term memory alone, see its effect (agent recalls something across turns) — not yet
      combined with the tool
3. **Independent use case — Supply Chain (shipment tracker):** student builds a tool *and* wires in
   memory together in this new context — this is where tools + memory actually combine

**Use cases confirmed usable** (2026-09-17, via `drafts/lesson1_2/use-case-draft.qmd`): Retail
`check_inventory` + Supply Chain `get_shipment_status` both hold up as plausible, genuinely multi-turn
scenarios.

**Structure — revised and confirmed**, failure-first / fill-in-the-blank rhythm rather than lecture-first:

1. **Problem 1 (Retail, tool):** run the agent *without* the tool on "Do you have the blue hoodie in
   stock?" — it can't know. Fill in three blanks (`@tool`, docstring, `tools=[...]`) on a given function.
   Deliberately land on a weak docstring first — run it, it still doesn't answer right. Fix the
   docstring — run it, now it works.
2. **Problem 2 (Retail, memory):** ask a follow-up ("What about in black?") as a fresh call — agent has
   no idea what "it" means. Explain what's missing, fill in one blank (carrying `first_response["messages"]`
   forward). Run it — now it resolves correctly.
3. **Apply it (Supply Chain, independent):** no blanks — student builds a shipment-tracking tool and
   wires in memory from scratch, combining both pieces in a new context.

This replaces the earlier tool-alone → review → memory-alone → combined draft. Second draft is in
`drafts/lesson1_2/use-case-draft.qmd`; open questions at the bottom of that file (untested docstring-bug
reliability, whether one deliberate bug is enough, whether "Apply it" needs any scaffolding). Instructor
confirmed: this content is authored to run/be tested in Colab by the instructor next, separately.

**Guiding questions — ✅ drafted**, two layers:

- *Embedded checkpoints* (now in `use-case-draft.qmd` as `.callout-note` blocks at each failure/fix
  point): why can't the agent answer on its own; was the tool even called; what changed between the two
  docstrings; why does it seem to have forgotten; where does memory actually live
- *Pre-class discussion* (standard template Discussion section, tied to the quickstart prep reading):
  - What surprised you about how easy or hard the quickstart was to get running?
  - Where in the quickstart did you see a tool get used? Did you understand why the agent called it?
  - Did you notice memory in action anywhere in the quickstart? What did it look like?
  - What's one thing from the quickstart you're hoping today's class clarifies?

## 7. Known practice content — ✅ drafted

Instructor notes' practice idea ("fill in the blank for memory, fill in the blank for tools") is now the
in-class content itself (Problems 1–2 above), so take-home practice needs to be distinct — reinforcing at
the fluency/transfer level rather than repeating the same blanks. Proposed take-home:

- Pick a domain that is **not** retail or supply chain (own choice, own creativity — matches the
  precedent in the current `lessons/lesson1_2.qmd` Activity 2 Step 3)
- Build one custom tool with a clear docstring
- Design a short multi-turn conversation (2–3 turns) where a later question only makes sense if the
  agent remembers something from an earlier turn — same shape as "What about in black?"
- Confirm it fails without carrying `messages` forward, then fix it
- Short written reflection: what wording in the docstring mattered, and where the "memory" actually lived

Open question for instructor: is a written reflection worth requiring, or does that add friction without
enough payoff at this stage?

## 7. Known practice content — ⏳ pending confirmation
