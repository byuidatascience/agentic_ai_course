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

## Phase status

- [ ] Phase 1: Most Important Thing + destination
- [ ] Phase 2: Story + objectives
- [ ] Phase 3: Module outline
- [ ] Phase 4: Prototype
- [ ] Phase 5: Content

## Pick up here

Settle whether Lesson X = 2.3 (and so whether 2.3's approved Most Important Thing carries over). Then the destination.
