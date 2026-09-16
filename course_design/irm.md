# Curriculum Map (I / R / M)

> **Status: derived artifact, not law.** This table is *generated from* [course_outcomes.md](course_outcomes.md),
> [learning_arcs.md](learning_arcs.md), and [activities_assessments.md](activities_assessments.md). When it
> disagrees with any of those, they win and this file is wrong. See [README.md](README.md) for the
> precedence rules.

The standard curriculum-alignment artifact: outcomes down the side, units across the top. This is what
accreditors ask for and what most departments keep. It is included here to establish the baseline —
and to show where it runs out.

**Legend**

| Code | Meaning | Assessment expectation |
|------|---------|------------------------|
| **I** | Introduced — first exposure, low stakes | Not assessed at criterion |
| **R** | Reinforced — practiced with feedback | Formative; failure is expected and useful |
| **M** | Mastered — demonstrated at criterion | Summative; this is where the grade comes from |
| — | Not present in this unit | — |
| `?` | Inferred with weak or no evidence in the repo — correct these | — |

**Units** (per [learning_arcs.md](learning_arcs.md) and [teaching_philosophy.md](teaching_philosophy.md))

| Unit | Arc | Project |
|------|-----|---------|
| **U1** | Build a **"Bad"** Agent (includes Day 0.1) | P1: powerful, unpredictable agent |
| **U2** | **"Why"** was it bad? | P2: diagnostics |
| **U3** | Build a **"Good"** Agent | P3: context engineering |
| **Cap** | Contribution Assignment + self-directed final project | Portfolio, Ethics Manifesto, Coding Interview, Grade Letter, Final Interview |

> Battle of the Bots was removed from the capstone — see [research/shelved_ideas.md](research/shelved_ideas.md).
> The self-directed final project is referenced in [teaching_philosophy.md](teaching_philosophy.md) but is not
> yet defined in [activities_assessments.md](activities_assessments.md); the `Cap` column below is provisional
> until it is.

---

## Level 1 — Outcomes × Units

| # | Outcome | U1 | U2 | U3 | Cap |
|---|---------|:--:|:--:|:--:|:---:|
| 1 | Build AI agent harnesses | **I** | R | **M** | **M** |
| 2 | Evaluate agents using agent observability tools | — | **I → M** | R | R |
| 3 | Translate ambiguous goals into architecture and success criteria | I | R | **M** | R |
| 4 | Communicate about AI using language fitted to the audience | **I** | R | R | **M** |
| 5 | Use quality sources to self-learn | **I** | R | R | **M** |
| 6 | Form and live a personal ethic for the use of AI agents | I | **I → R** | R | **M** |

Outcome 1 masters twice on purpose: pass-offs and P3 in U3, then the coding interview in the
capstone. Outcome 2 masters in U2 because P2 *is* its summative assessment — see the design-smell
note below.

### What this table tells you

Almost nothing. Most rows are some flavor of `I → R → R → M`, and that is what *always* happens to a
capstone-based course under I/R/M, because the capstone assesses everything. The only facts here you
did not already know are that Outcome 2 starts late and masters early, and that Outcome 3 has no U1
presence — and you knew both.

This is the established solution, it took an afternoon, and it cannot find a single one of your gaps.
That is not a defect in your course. It is the resolution limit of the instrument: six rows cannot
locate a problem that lives at competency 3.7.

---

## Level 2 — Competencies × Units

The same instrument at the resolution where signal actually appears. Twenty-nine rows — every
second-level competency in [course_outcomes.md](course_outcomes.md), one page.

> **These are judgment calls, not a record of intent.** Cells marked `?` are ones inferred with weak
> or no evidence. Correct them — the corrections are the point.

| # | Competency | U1 | U2 | U3 | Cap |
|---|------------|:--:|:--:|:--:|:---:|
| | **1. Build AI agent harnesses** | | | | |
| 1.1 | Connect to the model (the "brain") | **I** | R | **M** | **M** |
| 1.2 | Design an agent's instructions and prompts | **I** | R | **M** | **M** |
| 1.3 | Give the agent memory and manage its context | **I** | R | **M** | R |
| 1.4 | Extend the agent with tools and services | **I → R** | — | **M** | R |
| 1.5 | Constrain the agent with deterministic safety guardrails | — | **I** | **M** | R |
| 1.6 | Architect multi-agent / sub-agent delegation | — | — | I `?` | R `?` |
| | **2. Evaluate agents using observability tools** | | | | |
| 2.1 | Observe agent performance | — | **I → M** | R | R |
| 2.2 | Measure agent performance | — | **I → M** | R | R |
| 2.3 | Diagnose agent performance | — | **I → M** | R | R |
| | **3. Translate goals into decisions** | | | | |
| 3.1 | Define purpose and intent without digital tools | I | R | **M** | R |
| 3.2 | Gut-check viability of AI for a problem | I | R | **M** | R |
| 3.3 | Define and operationalize success | — | **I** | **M** | R |
| 3.4 | Find hidden domain knowledge and assumptions | — | — | **I → M** | R |
| 3.5 | Anticipate what context the agent needs | — | — | **I → M** | R |
| 3.6 | Plan multiple harness architectures | — | — | **I → M** | R |
| 3.7 | Author intent into durable artifacts | — | — | I `?` | R `?` |
| | **4. Communicate** | | | | |
| 4.1 | Use current industry terminology correctly | **I** | **R → M** | R | R |
| 4.2 | Demonstrate competence to employers | I | R | R | **M** |
| 4.3 | Communicate an agent's behavior at work | — | **I → M** | R | R |
| | **5. Self-learn** | | | | |
| 5.1 | Learn from primary-source documentation | **I** | R | R | **M** |
| 5.2 | Find and evaluate trusted people and communities | — | — | — | — `?` |
| 5.3 | Evaluate relevance and currency of information | **I** | R | **R** | M |
| 5.4 | Find and evaluate software | — | — | — `?` | — `?` |
| 5.5 | Develop genuine excitement for AI use cases | *ambient* | *ambient* | *ambient* | *ambient* |
| | **6. Personal ethic** | | | | |
| 6.1 | Develop a personal conviction | — | **I** | R | **M** |
| 6.2 | Define what ethical AI use means to them | — | **I** | R | **M** |
| 6.3 | Examine how their AI use impacts self and others | I | R | R | **M** |
| 6.4 | Apply Church doctrine to real AI situations | I | **R** | R | **M** |
| 6.5 | Articulate industry's framing of alignment as ethics | — | **I** | R | M |

---

## What the second table found

**Outcome 3 has no home before Unit 3.** Four of its seven competencies (3.4–3.7) appear only in
Unit 3 or later, and 3.7 is `?` because no activity or assessment names it directly — it is carried
entirely by Project 3's blanket `competency: 3` tag. Outcome 3 is the hardest outcome and the one
[course_outcomes.md](course_outcomes.md) itself flags as "nearly taken shape" — and structurally it
is a Unit 3 outcome bolted onto a course whose first two-thirds barely touch it. Either it is a Unit 3
outcome and should say so, or it needs a U1–U2 presence that does not exist yet.

**Outcome 5 is thin where it matters.** 5.1 and 5.3 are well served — prep readings, Out of Date
Reading, docs in every lesson. 5.2 has one activity (`join-a-forum`) that carries no `type:` and no
day, so it currently satisfies nothing. 5.4 has no teaching activity at all and is assessed only
through Standard Test's blanket `competency: 5`. [assessments.md](assessments.md) already flags both
as gaps; this is the same finding arrived at independently.

**5.5 cannot be coded here.** Not because it is a bad outcome — because the only things serving it
("Convey a Personal Excitement", "Cover Every Use Case Under The Sun") are stances, not units. `I/R/M`
has no vocabulary for that. [use_case_coverage.md](use_case_coverage.md) is the instrument for 5.5;
it works by tagging instances with `use_case:`, and zero such tags currently exist.

**Outcome 1's twenty sub-competencies are invisible at this resolution and nearly invisible at any
other.** Every one of them is carried by two blanket `competency: 1` tags (Pass-offs and the Problem
Solution Ladder), both of which are patterns rather than named instances. The row for 1.4 above says
"Extend the agent with tools and services" masters in U3; nothing in the repo says *which* pass-off
proves it.

**The `I → M` cells in Unit 2 are a design smell worth a look.** Competencies 2.1, 2.2, 2.3, and 4.3
are introduced and mastered inside a single unit, then decay to `R`. That may be correct — P2 is a
real summative assessment. But mastery in the same unit as introduction usually means either the unit
is doing too much, or the mastery bar is lower than the word implies. Unit 2 is also where no teaching
activity currently exists for 2.1, 2.2, or 2.3 — they are assessed by P2 and taught by nothing, which
violates the ordering rule in [plan.md](plan.md).

---

## The limit of this artifact

Every cell above answers "does this competency appear in this unit." None answers:

- Which competencies have **no assessment**, as opposed to no teaching?
- Which days are **overloaded**?
- If MCP dies, **what breaks**?

Those need the relation between competencies and *instances* — a specific thing on a specific day —
not between competencies and units. That is what [coverage/](coverage/) is for. This table is the
honest ceiling of the established tool, and it is worth keeping precisely so the next thing has
something to beat.
