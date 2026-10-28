# Lesson 2.3 design log

## What already exists (inventory, 2026-10-16)

- `drafts/unit2_one_things.md` (draft outline, not approved): 2.3 = **Threads and naming failures** `2.3.2, 2.3.1`. Prep: ILS M1 L3 Alternative Ways to Trace, L4 Conversational Threads + BRA M1 L3 "Analyzing your Agent" (~26 min).
- `drafts/an_outline.md` (older): 2.3 = Failure Modes, Advanced tracing `2.3.2, 2.1.3`.
- `instructor_notes/notes2_3.qmd` (stale draft): MIT "deepen understanding of 'good'... identify failure modes." Six lever-named modes (Tool, Grounding, State, Control, Specification, Safety), three dimensions (silent/loud, isolated/cascading, model/code), aliases, OWASP/MAST comparison, "defend the classification with trace evidence."
- `course_design/research/failure_modes.md`: the taxonomy source of truth (notes link to an old path, `course_design/failure_modes.md`).
- `lecture_slides/_slide2_3.qmd` (underscore = unpublished): taxonomy slides + three worked modes (Infinite Loop/Control, Hallucinated Planning/Tool, Unsafe Tool Use/Safety) + long-list appendix.
- From 2.2 (`drafts/lesson2_2/`): handoff-pile notebook already shows ungrounded answer (T1), swallowed tool error (T2), loop (T4), and its objective 1 claims `2.3.2`. T3 wrong argument and T5 policy ignored were set aside "for 2.3."

## Conflicts flagged

- 2.2 already names three failure modes and tags `2.3.2`. 2.3 has to build on that, not repeat it.
- 2.2's names (ungrounded answer, swallowed error, loop) are phenomenon names; the 2.3 taxonomy is lever-named (Grounding, Tool, Control). Needs a bridge or a rename.
- Threads (ILS M1 L4) appear only in the draft outline; nothing in the notes or slides covers them.

## Decisions

**Most Important Thing (approved 2026-10-16):** Identify the six main failure types in all three dimensions in traces.

## Side work (instructor, 2026-10-16)

- Revise 2.2's objectives (2.3 now owns failure-mode identification).
- Flesh out ACME's business model in a new profile file: what ACME does and who it serves, so the agent can be deliberately bloated (many users, many jobs) and supply failures for many lessons.

## Phase status

- [ ] Phase 1: Most Important Thing + destination (MIT approved; destination open)
- [ ] Phase 2: Story + objectives
- [ ] Phase 3: Module outline
- [ ] Phase 4: Prototype
- [ ] Phase 5: Content

## Pick up here

MIT approved. Order: revise 2.2 objectives → 2.3 destination + objectives → ACME profile → how failures show up in the story.
