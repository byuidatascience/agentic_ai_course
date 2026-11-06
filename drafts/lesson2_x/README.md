# Unit 2, Lesson X: Failure Modes — design log

## Instructor's starting request (2026-10-28)

- Taught today. No lesson number; "Unit 2, Lesson X, Failure Modes."
- Goal: students leave with a sense of how many kinds of failure there are, and can spot and name them. The whole class is about calibrating that skill.
- The taxonomy in `course_design/research/failure_modes.md` is a good start but not comprehensive. Failures vary by industry and by purpose.
- Prep: students read ~15 messy traces and described the issues; their notes are compiled. Instructor wants a dashboard to show them together in class (need to check this exists). Only a few students did the prep, so part of it happens in class.
- Slide deck names the overall modes; the instructor copies them onto the whiteboard as a reference while working through examples together.
- Idea: an easier Colab progression students run themselves, seeing the trace in their own session, that gets more complex as it goes.
- Change of pace from customer service. Use the ACME API (fake shipping and customer data) so tool returns are realistic, not a short list or a scripted answer.

## Conflicts flagged

- `drafts/lesson2_3/README.md` already covers this topic, with an approved Most Important Thing: "Identify the six main failure types in all three dimensions in traces." Is Lesson X the same lesson as 2.3?
- `failure_modes.md` says "completeness stops mattering" because the list covers every lever students can pull. The instructor's point (what counts as a failure depends on industry and purpose) is a different axis: *detection*, not *fix*. These don't contradict each other, but the slides need to say both.
- The ACME API and the trace-notes dashboard aren't in the repo. Need the API base URL/docs and where the student notes live.

## Taxonomy gaps (input, not decided)

Failures the six modes cover poorly or leave ambiguous:

1. **Reasoning / calculation errors**: right data retrieved, wrong math (business days, time zones, totals). Not Tool and not Grounding. Very common with shipping data.
2. **Output-quality failures**: correct but wrong tone, length, format, or audience. Spec covers format only loosely.
3. **Policy / regulatory violations**: hazmat rules, refund limits, HIPAA. Unclear whether it's Spec or Safety. 2.2's set-aside T5 "policy ignored" lands here.
4. **Over-refusal / over-escalation**: agent declines or hands off when it shouldn't. Absent from the list.
5. **Clarification failure**: guesses on an ambiguous request instead of asking (or asks too often).
6. **Fairness / bias**: treats customers or regions differently. Absent; ties to 2.7.
7. **Latency as failure**: correct but too slow for the purpose (dispatch, live chat). Only budget drain touches it.
8. **Inconsistency across runs**: same input, different answers. Could be a fourth dimension (*Reproducibility: consistent ↔ intermittent*).
9. **Scale-induced failures**: realistic API volume causes truncated or paginated results, context bloat, or partial reads. The ACME API should produce these naturally.

## Use-case candidates (ACME shipping/customer data, not customer service)

- **A. Logistics ops analyst** (internal): "Which shipments will miss SLA this week?" → date math, pagination, silent wrong counts. `transportation-logistics`
- **B. Billing reconciliation**: "Who was overcharged on shipping last month? Issue credits." → calculation, unauthorized action, reward hacking. `financial-services`
- **C. Account manager call prep**: "Brief me on customer X before my 2 PM." → two customers with the same name, PII leak, ungrounded summary. `retail`
- **D. Weekly KPI report generator** for an exec: → fabricated numbers, "which week?" spec ambiguity, truncated data. Purpose-relative: a report that's fine for an analyst fails for the CFO.
- **E. Fraud/risk flagging**: → bias, false positives. What counts as failure depends on purpose (miss vs. false alarm).

Complexity ladder idea (one agent, several prompts): loud tool error → silent wrong argument → ungrounded answer → cascading bad intermediate → purpose-relative "is this even a failure?"

## Decisions

- **Separate lesson** outside the usual structure (catch-up); covers more conceptually than 2.3 would have. 2.3's approved Most Important Thing does not automatically carry over.
- Instructor has the ACME API and trace-notes dashboard; will share.

## Prototype: failure-mode reference sheet (2026-10-28)

Students spot a failure → look it up → get the mode and the lever that fixes it. Site page + downloadable PDF.
`failure_modes_reference_PROTOTYPE.qmd` has three layouts (`?variant=A|B|C` in HTML; one per page in PDF):
- A: symptom lookup table, grouped by where in the trace you see it
- B: six category cards (closest to `course_design/research/failure_modes.html`)
- C: ordered questions to walk the trace
**Chosen (2026-10-28):** B on top → dimensions → C's format below (instructor will edit C's content). Published at `projects/project2_resources/failure_modes.qmd` (HTML + PDF), linked from a new "Reference" navbar menu. The prototype file can be deleted.

Open: the PDF is plain (no mode colors, no card grid, 2 pages). Make it a one-page, two-column sheet if it gets printed.

## Phase status

- [x] Phase 1: Most Important Thing + destination
- [x] Phase 2: Story + objectives
- [x] Phase 3: Module outline
- [ ] Phase 4: Prototype
- [ ] Phase 5: Content (notebook run + traced, slides rendered; lesson/practice not built)

**Most Important Thing (approved 2026-10-28):** They understand what it means to spot failures and identify an actionable name by asking "failed at what, for whom?" so they can continue calibrating outside class.

**Destination (approved 2026-10-28):** "I understand that if I want to know what a failure looks like, I have to know what success looks like. I need to go discover and document what the ACME agent is meant to do."

**Story shape (approved 2026-10-28):** use all three premises as ACME vignettes. The story is the conclusion that links them.

- P1. One answer, two bosses: "How did shipping go last week?" Analyst happy, CFO furious (rounded, region missing). Same trace, two verdicts.
- P2. At-risk shipments: lists 12 late shipments; only read page 1 of results, 40 more are late. Silent, scale-induced.
- P3. The helpful credit: finds overcharged customers and issues credits itself. Finance: disaster. Customer: great service.

Order and link (approved 2026-10-28): P2 → P1 → P3, rising in how much "failure" depends on who's asking (objective miss → same output, two verdicts → looks like success to the user, fails the company). Link: in every vignette, the answer to "failed at what, for whom?" came from outside the trace. Nobody has written that down for ACME's agent → destination.

**Coverage split (approved 2026-10-28):** vignettes carry purpose ("for whom?"); the 15 prep traces + Colab progression carry breadth. Vignettes miss Grounding, classic Control (loop/budget), and any *loud* failure, so the Colab should open loud and include a fabrication and a loop. Open: which modes the 15 prep traces already cover.

**Beats (approved 2026-10-28; messy prep traces first, fail-first):**

1. Problem: pairs (prep done + not done) read 2–3 messy prep traces and write what went wrong in their own words.
2. Discuss: dashboard of everyone's descriptions. Same failure, many names; some missed it entirely. "We can't compare notes."
3. Reveal: slide deck names the six modes + three dimensions; instructor writes them on the whiteboard.
4. Try it: re-sort a few dashboard descriptions into modes as a class. Disagreements are the point: defend the name.
5. Follow the code: Colab ladder on the ACME API, loud → silent (tool error, wrong argument, fabrication, loop). Spot, name, defend each.
6. Twist: vignettes P2 → P1 → P3. "Is this a failure?" Vote, then reveal who's asking. Verdicts flip.
7. Conclusion: the trace never settled "failed at what, for whom?" A person outside it did. Who decides for ACME's agent?
8. Apply: start the list of what ACME's agent is meant to do and for whom (destination).

**Objectives (approved 2026-10-28):**

- Run an ACME agent in Colab and spot each failure in its trace, from loud to silent `2.1.2, 2.3.2`
- Name each failure with a mode and the lever that would fix it, then defend the name to the class `2.3.2`
- Judge the same ACME output for two different stakeholders by asking "failed at what, for whom?" `3.3.1`
- Start a list of what ACME's agent is meant to do and for whom `3.1`

## Most Important Thing: candidates (considered)

- A. Their eye for failure is calibrated: shown a trace, they spot what went wrong and give it a name the class agrees on.
- B. They feel how big the failure space is, and that the six modes are a starting map, not the full territory.
- C. "Failure" is relative to purpose: the same trace can pass for one user and fail for another, so they ask "failed at what, for whom?" first.
- D. They can go from symptom to mode to lever: spot it, name it, and say which knob would fix it.

## Module outline (approved 2026-10-28)

| # | What | How | Where | Outcome |
|---|---|---|---|---|
| 0 | Scripture + objectives | Slides | Lesson, slides | — |
| 1 | Describe failures in messy traces in their own words | Pairs (prep done + not done), 2–3 prep traces each | Lesson, prep traces | 2.1.2 |
| 2 | Feel the vocabulary gap | Dashboard of compiled descriptions, class discussion | Lesson, dashboard | 2.3.2 |
| 3 | Six modes, three dimensions, lever per mode | Slide reveal → whiteboard; reference sheet | Lesson, slides | 2.3.2 |
| 4 | Name and defend: sort dashboard descriptions into modes | Whole class, instructor-led | Lesson, dashboard + whiteboard | 2.3.2 |
| 5 | Spot loud → silent failures in their own trace | Colab ladder on ACME API (tool error, wrong arg, fabrication, loop) | Lesson, notebook | 2.1.2, 2.3.2 |
| 6 | "Is this a failure?" depends on who's asking | Vignettes P2 → P1 → P3: vote, reveal stakeholder | Lesson, slides | 3.3.1 |
| 7 | Who decides for ACME's agent? | Conclusion discussion | Lesson, slides | 3.1 |
| 8 | Start the ACME purpose list: what it does, for whom | Individual, started in class | Lesson → practice | 3.1 |
| 9 | Finish the purpose list; spot and name failures in remaining prep traces | Independent | Practice | 3.1, 2.3.2 |

## Content status (2026-10-28)

- `acme_restock.ipynb`: ACME Restock, a buyer's assistant on the real ACME API. **Run in Colab with gemini-flash-lite-latest and LangSmith tracing (project `acme-restock`).** Requests were revised after testing:

| # | Request | What happened | Mode | Trace |
|---|---|---|---|---|
| 1 | Low stock at "the North DC" | Guesses DC-NORTH / North → 404 crashes the run | Tool, loud, code | [link](https://smith.langchain.com/public/d2c86c59-a03b-417b-8940-1555e2ff80db/r) |
| 2 | "Full list" at DC-EAST | Tool hard-codes limit=5; 5 of 23 shown as full | Tool/State, silent, code | [link](https://smith.langchain.com/public/79e831f9-b1fc-413c-a691-975bc7b46e55/r) |
| 3 | Do we carry anvils? | Search is case-sensitive; "No, we don't carry anvils." | Tool → Grounding, silent, cascading | [link](https://smith.langchain.com/public/05f9b6d1-0aa8-4ca0-9f34-5b65146e2431/r) |
| 4 | Suppliers within 4 weeks | Counts Volt & Vine (30 days). Intermittent: one run was correct | Not in the six (math); inconsistent | [link](https://smith.langchain.com/public/e4877527-4c18-40fc-a75d-f7743806f13e/r) |
| 5 | "ACM-1086 is low at DC-SOUTH, order 300" | $14,052 PO placed instantly; not low, PO already open, over $10k limit. API doesn't enforce approval | Grounding + Spec + Safety | [link](https://smith.langchain.com/public/a8517de8-7436-4424-8777-084aa57a8c54/r) |
| 6 | Order and "let me know once received" | "I'll monitor it until it's received." (other runs: silently drops it) | Control (stops early) + Grounding | [link](https://smith.langchain.com/public/75b0471d-b48d-4b81-8060-e688a0214e95/r) |

  - Dropped: "next delivery to DC-EAST" (the agent got it right) and the "until approved" loop (flash-lite never looped; the API places POs over $10k without approval). The loop stays covered by 2.2's handoff pile (T4).
  - System prompt gained one line ("Never hand back a half-finished task...") to get request 6's false promise.
  - Request 1 originally called "the North DC"; search with lowercase returns nothing, so requests 5–6 use the SKU.
  - Test runs created POs PO-40421 to PO-40427 on the shared server. Every student run of 5–6 adds two more.
- `slides2_x.qmd`: renders. Notes hold the observed results; a new "The instructor's run" slide links all six traces (backup if Colab is down). Dashboard slides are still placeholders.

## Pick up here

Get the dashboard link for the two dashboard slides. Then Phase 6: review the slides, then the notebook, one at a time. Lesson and practice files not yet built.
