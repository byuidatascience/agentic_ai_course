# Lesson 2.2 design log

## Instructor's starting request (2026-10-14)

- Biggest goal: students **derive and feel the purpose of observability platforms**, leaning on their own Unit 1 agent-building experience.
- Mostly traces today. Experiments (why they exist) come later in the unit.
- Show what a trace would look like if we implemented one ourselves in the terminal.
- Show other observability platforms and what a trace looks like in each.
- Starts the conversation on failure modes: look at a few traces of different failure modes.
- Needs prepared examples so the instructor can run them and have traces ready to show.

## Conflicts flagged

- `drafts/unit2_one_things.md` (draft outline) puts local LangSmith setup + tracing their own Unit 1 agent in 2.2, and failure modes in 2.3 (2.3.2). Today's request adds a failure-mode *preview*. Not overriding; decide in Phase 2/3 where setup lands.
- `instructor_notes/notes2_2.qmd` (stale draft) centers on LangSmith UI and run types; useful input for the run-type objective.

## Phase status

- [x] Phase 1: Most Important Thing + destination
- [ ] Phase 2: Story + objectives
- [ ] Phase 3: Module outline
- [ ] Phase 4: Prototype
- [ ] Phase 5: Content

## Decisions

**Most Important Thing (approved):** They are reintroduced to the problems that drive agent observability, and invent tracing themselves to solve it.

**Destination (approved):** "My Unit 1 agent sends its traces to LangSmith, and I can read what it actually did."

## Most Important Thing: candidates (not approved)

- A. They feel the pain of debugging an agent blind (print statements in a terminal) so a trace UI lands as relief, not as one more tool.
- B. They can open a trace in any platform (terminal, LangSmith, another) and say what the agent did, step by step.
- C. They realize "it gave an answer" was never evidence: a trace shows failures the final answer hides.
- D. They see every observability platform is the same idea (a tree of runs with inputs and outputs), so the tool is swappable but the habit isn't.

### Instructor feedback (2026-10-14)

- They already felt the pain in Unit 1; the lesson **connects** to it, it doesn't recreate it.
- A missed "derive." Leaning D: they derive and feel the *purpose*, so they recognize how it operates in any platform.
- Deriving the purpose needs the *problems* too → stronger case for failure modes today.

Reworded candidates built on D:

- D1. From the failures they already hit, they derive what an observability platform must do, so they recognize that purpose in any platform's trace.
- D2. They derive why traces exist from real agent failures, so any platform's trace reads as an answer to problems they've had.

Instructor: too long, punchier. Short candidates:

- E1. They derive why traces exist, so they can read one anywhere.
- E2. Traces exist because agents fail. They derive it, then see it everywhere.
- E3. They could have invented tracing themselves.

**Story premise (approved): P3, the handoff pile.** The engineer who left hands over a stack of complaint tickets. Each is a different failure mode, and all anyone has is the agent's final answers.

- Afterward (instructor idea): reveal the departed engineer's own "debug" console output, meant to help solve it, but it only barely advances the diagnosis. Contrast with a real trace.

**Scripture (approved):** D&C 93:24

**The pile (approved): T1, T2, T4.** Each hides in a different place in the trace.

- T1. Ungrounded answer: tool said "out of stock," agent promised delivery Friday. (hidden in a tool's output)
- T2. Swallowed tool error: lookup failed, agent invented an order status. (hidden in an error)
- T4. Loop: called the same tool 8 times; customers report long waits and timeouts (worse for some, since runs vary). (hidden in the trace's shape)
- Not used: T3 wrong argument, T5 policy ignored (candidates for 2.3 failure-mode work).

## Derivation path (tentative, 2026-10-14)

1. Final answers only: groups guess what went wrong per ticket. Can't tell.
2. Reveal the engineer's console prints: "calling tool... done." Barely helps.
3. Brainstorm per ticket: "What would you need to see to know?" → each step's inputs/outputs (T1), errors (T2), order, count, and time (T4), which step called which.
4. Combine the lists: that record is a trace. They invented it.
5. Terminal trace: the instructor's hand-rolled version of their list.
6. Other platforms: same tree, different paint. Then LangSmith on their own agent (destination).

## Beats: draft v2 (not approved)

1. Problem: the handoff pile. Three tickets, final answers only.
2. Follow the code: run the pile (or saved output). The answers all look fine.
3. Discuss: groups talk about what went wrong on each ticket. Collect guesses; confirm none.
4. Engineer's prints: "looking up order... done." Barely helps; "done" even lies.
5. Name it (longer section):
   - Name the problems: each ticket becomes a failure mode (ungrounded answer, swallowed error, loop).
   - Name the solutions: for each, what would you need to see? (tool outputs, errors, call order/count/time, which step called which.) Combine lists; T4 pushes toward order and nesting.
6. Reveal: that list is a trace. Terminal trace built from their list; confirm each failure mode in it.
7. Other platforms: the same three tickets as traces in LangSmith and others. Same tree, different paint.
8. How it works: runs, traces, run types, inputs/outputs/metadata (kept as its own beat).
9. Apply: LangSmith key on their Unit 1 agent, read their own trace (destination).

Instructor (2026-10-14): group discussion between running the pile and the prints; failure modes named early, in the "name it" section, with problems and solutions both named.

Instructor clarifications (2026-10-14):
- Beat 2: tickets appear in the slides as chat/ticket mockups, no code.
- Beat 4: show the console output only, not the code that produced it.
- Beat 5: "students coin names" vs "instructor names" are the same in practice: after discussion, instructor names the failure modes; students derive the solutions.
- Moved on to slides (instructor's call); module outline skipped for now.

## Objectives (approved 2026-10-16; on the slide)

1. **Diagnose** a few failed agent examples from output, code, and traces `2.3.1`
2. **Discover** the "why" behind traces and what problems they solve that code doesn't `2.1.2`
3. **Point out** the run types inside a trace `2.1.3`
4. **Send** your Unit 1 agent's traces to LangSmith `2.1.1` (*flag wording* in course_outcomes.md)

Revised because 2.3 now owns naming failure modes (`2.3.2`). Ids on 1 and 2 are Claude's tagging; confirm.

## Prototype: `handoff_pile.ipynb` (tested in Colab 2026-10-14)

One ACME support agent, three tools, one system prompt. All three tickets fail on their own and produce cheerful final answers.

- T1: `check_stock` returns `status: BACKORDERED` next to `standard_delivery: arrives Friday`; agent says "arrives Friday." (Sometimes it says "on backorder, but Friday!", which is still wrong.)
- T2: `lookup_order` catches a TimeoutError and returns `{"status": None, "error": ...}`; prompt says "never mention technical problems," so the agent invents "being prepared, arriving Friday."
- T4: `track_package` returns "UPDATING... call again" 7 times, then a location; agent calls it 8 times and answers fine. Cut from 14 to 8 because of the free-tier limit (15 calls/min).
- Engineer's prints (`DEBUG = True`): "looking up order... done" prints "done" even when the lookup failed. A nice reveal: the prints say *that* things happened, not *what*.
- The hidden causes live in the system prompt + tool outputs, both visible in a trace.
- Rate limit: T4 + the debug rerun can hit Gemini's 15 RPM free tier. Wait a minute between them. If students run it, same issue.

## Saved outputs (no live demos)

Instructor: live demos never work live, so slides use saved output.

- `captured_outputs.md`: slide-ready text blocks (pile, engineer's prints) + an evidence table per ticket.
- `captured_runs.json`: full condensed message history of one real run (for the terminal trace and platform mockups).
- Found in capture: T2 borrows "arrives Friday" from `check_stock` after the failed lookup, and its tool message is marked `success`. T4 took 5.1 s.
- **T4 complaint (decided):** unexpectedly long waits / model timeouts ("Your chat keeps hanging, and sometimes it just times out."). Don't produce a minute-long run; 5.1 s is fine for the demo. Story line: other customers have it worse because the model isn't deterministic.

## Slides: first draft `slides2_2.qmd` (2026-10-14, not approved)

33 slides, rendered to `slides2_2.html`. Scripture (D&C 93:24, verbatim) → objectives → memo + 3 ticket mockups → discuss → engineer's console output → name the problems → name the solutions → combined list → "you invented tracing" → terminal traces T1/T2/T4 (real, from captured_runs.json) → tree-of-runs diagram → platforms grid → how it works (run/trace/tracing, run types image, inputs/outputs/metadata) → turn on tracing in Unit 1 agent → "what did your agent actually do?"

Open / TODO:
- Platform screenshots (LangSmith, Langfuse, Phoenix, W&B Weave, Braintrust) are placeholders. Prep: send ticket #2 to each and screenshot.
- LangSmith trace of ticket #2 for a shared project + Slack link.
- Ticket #1 slide shows the "They will arrive on Friday!" run; the T1 trace slide shows a different run ("on backorder, but Friday"). Noted in speaker notes.
- T2 complaint written as "payment never went through" so the invented status is clearly false.
- Terminal trace is shown as output only; no live code for it yet (could become a notebook cell later).
- Speaker notes inline; move to the notes file in Phase 6.

### Slide review log

- 2026-10-14: Slide 10 now shows the instructions + three ticket summary cards; discussion prompts moved to notes. "Did that help?" slide removed; the question is now the last click on the debugging-output slide (answer in notes). Deck is 32 slides.

## Pick up here

Phase 1 approved. Phase 2: premise, pile, scripture approved. Derivation path tentative. First-draft slides built. Next: instructor review of slides2_2 (one section at a time), then notebook/lesson/prep/practice.
