# course_design/

The design layer for DS 488. Everything the course *is* — as opposed to what it *says on a given day* —
is decided here. Lesson content, primers, slides, and instructor notes elsewhere in the repo are
downstream of these files and must conform to them.

---

## How to weight these documents

Two things get confused when people call a document "authoritative," so they are tracked separately:

- **Authority** — when two documents disagree, which one wins? This is about *precedence*, and it
  almost never changes.
- **Solidity** — how settled is the content? This is about *confidence*, and it changes constantly as
  the course hardens.

A document can have high authority and low solidity. `course_outcomes.md` is the clearest case: it
wins every argument, and half of it still carries `*flag wording*` markers. High authority means
"fix it here first," not "it is finished."

### The precedence chain

When two documents conflict, resolve in this order:

```
course_outcomes.md          <- the ids. Nothing overrides these.
  |
user_profiles.md            <- the scope boundary. Settles "is X in this course?"
learning_arcs.md            <- the narrative shape of the three units
  |
teaching_philosophy.md      <- pedagogy, grading, and the why behind structure
  |
plan.md                     <- the coverage and sequencing rules the design must satisfy
use_case_coverage.md        <- the breadth rule (competency 5.5)
menus.md
  |
activities_assessments.md   <- the actual inventory of activities and assessments
  |
assessments.md              <- a summary of the above. Derived.
irm.md                      <- a projection of the above. Derived.
coverage/                   <- generated from the above. Never wins.
```

Two shortcuts that follow from the chain and come up often:

- **`activities_assessments.md` beats `assessments.md`.** The first carries the machine-readable
  `competency:` tags; the second is prose summary and is currently stale against it.
- **`user_profiles.md` beats `teaching_philosophy.md` on scope.** The philosophy doc is the oldest
  file here and predates several scope decisions. It is authoritative on *how* to teach and *why*, not
  on *what is in the course*.

---

## The documents

### Tier 1 — Binding. Change these first; everything else follows.

| Document | Authority | Solidity | Notes |
|---|---|---|---|
| [course_outcomes.md](course_outcomes.md) | **Highest** | **Medium** | The spine. Every competency id used anywhere in the repo is defined here. Outcome 3 is self-flagged as "nearly taken shape"; 1.5.5 is an empty placeholder; several items carry `*flag wording*`. Ids 1.x–6.x are stable enough to tag against — the wording under them is not. |
| [user_profiles.md](user_profiles.md) | **Highest** | **High** | Short and decisive. The exit profiles are the scope boundary: they are what put deployment, hosting, and real UI out of the course. Reach for this when the question is "does this belong here at all?" |
| [teaching_philosophy.md](teaching_philosophy.md) | **High** | **Mixed** | The guiding document, and the oldest. Solid on pedagogy — fail-first, antifragility, cognitive load, group formation, the purpose of grading. **Soft on grading mechanics**: `TODO: Needs revision to align with University Policy`, blank rubric cells, and an unresolved tension between a student-decided grade and hard A-requirements. Where it implies productization or UI it has been superseded; see its Scope Boundary section. |
| [learning_arcs.md](learning_arcs.md) | **High** | **High** | 28 lines, entirely settled. Bad agent → why was it bad → good agent. The single most load-bearing idea in the course. |

### Tier 2 — Binding rules and inventory. Actively churning.

| Document | Authority | Solidity | Notes |
|---|---|---|---|
| [plan.md](plan.md) | **High** | **High** | The coverage rules the design has to satisfy, plus the build order. The rules are settled; the course does not yet meet several of them. Its estimated counts (~8 assessments, ~30 activities) are stale against the actual 16 and 22. |
| [use_case_coverage.md](use_case_coverage.md) | **High** | **Firm rule, empty list** | The rule — one tagged instance per use case — is settled and descends from competency 5.5. The 24 cases are currently stubs with zero `use_case:` tags pointing at them. |
| [activities_assessments.md](activities_assessments.md) | **High** | **Low–Medium** | The real inventory, and the file that most needs work. Authoritative over `assessments.md` and `irm.md` because it carries the tags. But it holds undecided material (Pass-offs lists four mutually exclusive grading schemes), nine untyped nodes that satisfy nothing, and one `type: acivity` typo. Several things named as law elsewhere have no entry here at all. |
| [menus.md](menus.md) | **Medium** | **Low** | Self-declared: "How this is used is in flux." Soft, changeable sub-competency lists. Treat as a staging area between research and the outcomes. |

### Tier 3 — Derived or stale. Never win an argument.

| Document | Authority | Solidity | Notes |
|---|---|---|---|
| [assessments.md](assessments.md) | **Low (derived)** | **Low** | Maps outcomes to their primary measures. Useful as a one-page view, but stale against `activities_assessments.md` and carrying its own `TODO coverage gap` markers. Names an "ethics contract" that exists everywhere else as the Ethics Manifesto. |
| [irm.md](irm.md) | **Low (derived)** | **Medium** | The accreditation-shaped I/R/M table, regenerated 2026-09-15 against the current outcomes. Kept to show the resolution limit of the standard instrument, not to drive decisions. |
| [course_structure.md](course_structure.md) | **Low** | **Stale** | Describes a four-level model (outcomes → competencies → evidence → tasks) that the rest of the design has outgrown — no examples, prep readings, use cases, days, or template/instance distinction. Needs rewriting, or folding into this README. |
| [first_go.md](first_go.md) | **Advisory** | **n/a** | Opens with "My initial thoughts (not requirements)." By its own first line it is not law — it is reasoning about first-offering pacing vs. future offerings. Probably belongs in `research/`. |
| [syllabus](syllabus) | **Student-facing** | **Medium** | Downstream of everything here, but the only document that binds externally: university policy, cost, the AI-use policy, and the semester calendar. Where it states a calendar fact or a policy, that fact is real and the design fits around it. |

### Not law

| Path | What it is |
|---|---|
| [research/](research/) | Working documents. Explorations, gap analyses, shelved ideas, scenario drafts, competing framings. Nothing here binds anything. Often more current than the law docs, never authoritative. |
| [coverage/](coverage/) | A generated artifact — a browser linter that parses the tags out of these files and reports rule violations. It reports on the design; it does not define it. If it disagrees with a law document, either the tags are wrong or the linter is. |

---

## Rules of thumb

1. **Tag against ids, not names.** `competency: 3.4` survives a rewording; "Find hidden domain
   knowledge" does not.
2. **A blanket tag is a promise, not coverage.** `competency: 1` on Pass-offs covers twenty
   sub-competencies on paper and none of them in practice. Same for `competency: 3` on Project 3.
3. **An untyped node satisfies nothing.** Every node needs a `type:`, or the coverage rules skip it
   silently.
4. **When an idea leaves the law layer, it goes to `research/`, not to the trash.**
   [research/shelved_ideas.md](research/shelved_ideas.md) keeps the reasoning so it does not get
   silently reinvented.
