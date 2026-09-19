# Lesson 1.1 Planning

Started as a side-effect of planning Lesson 1.2 — capturing decisions that landed on Day 1 instead.
Not yet a full pass through Lesson 1.1 the way `drafts/lesson1_2/planning.md` is doing for Day 2.

## Notes so far

- **`lessons/lesson1_1.qmd` as currently written is outdated.** Confirmed 2026-09-17 while scoping Day 2.
  Most of it still holds (API key setup, Colab Secrets, installing LangChain, calling `create_agent`/
  `agent.invoke` once in class), but the in-class tool call is no longer how students first encounter one.
  - Students are now expected to meet a tool call *and* memory for the first time through the
    `create_agent` quickstart in their own **prep reading**, not through in-class work on Day 1 — hopefully,
    without understanding either yet.
  - Not everyone will get the quickstart running successfully on their own before class.
  - **Action item:** a runnable Colab (`.ipynb`) with just the bare quickstart, as a fallback for students
    who couldn't get it working solo. Not yet built; not yet placed (prep material vs. in-class fallback).

- **Structure of input/output belongs in 1.1, not 1.2.** Understanding the shape of `agent.invoke()`'s
  input (the `messages` list) and its output (the response object) is Day 1 content — it was originally
  drafted as a Day 2 objective (see `drafts/lesson1_2/planning.md` item 4) but moved here since students
  are already calling `agent.invoke()` on Day 1.
