# Unit 2 (Diagnose): One Things

Unit destination: "I can gather evidence of an agent's strengths, failures, and shortcomings; explain it clearly to technical and non-technical audiences; and implement safety guardrails and meaningful improvements."

Short version: "I can first-pass diagnose and fix an agent."

Diagnosis is never definitive. This is iterative refinement: their initial testing before production.

Same per-day format as `drafts/unit1_one_things.md`.

## Unit shape (2026-10-12)

- **First: diagnose and communicate.** Students' first experience is only diagnosing; they don't fix anything yet. Communication is a big part.
- **Then: fix the agent (2 weeks).** This is where safety guardrails and controlling output come in.
- **Length: 5 weeks**, 3 days per week.
- **The agent:** students work predominantly with the ACME agent. The only touch on their Unit 1 agent is adding a LangSmith key and project to it. Otherwise Project 1 is let go; the focus is entirely Project 2.
- **Textbook:** LangChain Academy's "Intro to LangSmith" / Introduction to Agent Observability & Evaluations (video and notebook heavy) is primary. "Building Reliable Agents" (reading-heavy, light readings with good visuals) is a supplement for gaps, e.g. code-based evals and "Analyzing your Agent." Chosen partly to reduce work. Scope caps at production: use Modules 0–3, stop before Module 4/5.
    - Considered: letting students pick either course as their track. Doable if days anchor on concepts with a prep map, but set aside for now to reduce work.
    - Idea: pairwise experiments fit the fix phase better, since that's when there are two versions to compare.
- **Daily rhythm:** the course videos are short, so students do them before class. Class: light review → a series of activities → apply it.
    - "Every class leads to evidence" on the ACME agent was liked but set aside: too much bandwidth, since the ACME agent is hard to diagnose and non-deterministic, so in-class results can't be guaranteed.
    - Instead: class uses a **reliably failing example**, a tested Colab whose behavior the instructor knows, focused on one use case with a story, taught through a problem-solution ladder.
    - Worry: one thing before class (course), another in class (Colab example), and something else after (ACME). Don't overload them on top of the Project 2 agent.
    - Direction: the class examples are **slices of ACME** (ACME is big, so it has many use cases), keeping one company and one story at different scales. Pre-recorded traces in a shared LangSmith project are an option for reliable observation days.

## To work out later

- **ACME's major agent vs. the daily example agents:** which use cases each covers and how they integrate. Takes a lot of planning.

## Outline — DRAFT (proposed 2026-10-12, not approved)

Five weeks, 3 days per week: 3 weeks diagnose and report, 2 weeks fix. Ignores the old outline.

| Day | Topic | Competencies |
|---|---|---|
| **Week 1: See it** | | |
| 2.1 | Welcome to ACME: Project 2 intro, LangSmith set up, trace their own Unit 1 agent | 2.1.1 |
| 2.2 | Reading traces and types of runs | 2.1.2, 2.1.3 |
| 2.3 | Threads and naming failures | 2.3.2, 2.3.1 |
| **Week 2: Measure it** | | |
| 2.4 | Datasets | 2.2.3 |
| 2.5 | Evaluators: code-based and LLM-as-judge | 2.2.1, 2.2.2 |
| 2.6 | Experiments and analyzing results | 2.2.4, 2.3.1 |
| **Week 3: Report it** | | |
| 2.7 | Beyond "does it work": aligned and ethical | 3.3.1, 6.5 |
| 2.8 | Communicating findings to technical and non-technical audiences; work time | 4.3 |
| 2.9 | Progress meeting / diagnosis report | 4.3 |
| **Week 4: Fix it** | | |
| 2.10 | Planning the fix: prioritize findings, the prompt engineering lifecycle | — |
| 2.11 | Fixing prompts in the Playground | — |
| 2.12 | Managing prompt versions: Prompt Hub and Polly | — |
| **Week 5: Make it safe and prove it** | | |
| 2.13 | Safety guardrails | — |
| 2.14 | Controlling output | — |
| 2.15 | Prove the fix: pairwise experiments, before vs. after | 2.2.5 |

Unplaced: summary evaluators (M2 L6, optional), human review / annotation queues (2.3.3, from Module 4).

### Prep by day — DRAFT

ILS = Intro to LangSmith (primary). BRA = Building Reliable Agents (supplement; no durations listed, so its times are estimates).

| Day | Prep | Time |
|---|---|---|
| 2.1 | ILS Welcome: Course Overview, LangSmith Background, Getting Set Up (video guide) + BRA "Intro: The Agent Development Lifecycle" | 8 min + ~10 min read (est.) |
| 2.2 | ILS M1 L1 Tracing Basics, L2 Types of Runs | 23 min |
| 2.3 | ILS M1 L3 Alternative Ways to Trace, L4 Conversational Threads + BRA M1 L3 "Analyzing your Agent" | 16 min + ~10 min read (est.) |
| 2.4 | ILS M2 L1 Datasets | 15 min |
| 2.5 | ILS M2 L2 Evaluators + BRA M2 L4 "Eval 1: Code-based Eval" | 15 min + ~10 min read (est.) |
| 2.6 | ILS M2 L3 Experiments, L4 Analyzing Experiment Results | 21 min |
| 2.7 | Alignment/ethics reading (TBD) | TBD |
| 2.8 | None | — |
| 2.9 | None (diagnosis report due) | — |
| 2.10 | ILS M3 L3 Prompt Engineering Lifecycle | 8 min |
| 2.11 | ILS M3 L1 Playground | 13 min |
| 2.12 | ILS M3 L2 Prompt Hub, L4 Polly | 14 min |
| 2.13 | Instructor content (TBD; neither course covers guardrails) | TBD |
| 2.14 | Instructor content (TBD) | TBD |
| 2.15 | ILS M2 L5 Pairwise Experiments (optional in the course) | 10 min |

## Reference: Intro to LangSmith, Modules 0–3 (from the instructor)

| Module | Lesson / Title | Type | Duration / Details |
| :--- | :--- | :--- | :--- |
| **Welcome to the course!** | Course Overview | Video | 1 min |
| | LangSmith Background | Video | 1 min |
| | Getting Set Up | Text | — |
| | Getting Set Up (Video Guide) | Video | 6 min |
| | Module 0 Resources | Text | — |
| | Course Transcripts | Downloads | — |
| **Module 1: Visibility While Building with Tracing** | Module 1 Introduction | Video | < 1 min |
| | Module 1 Resources | Text | — |
| | Lesson 1: Tracing Basics | Video | 13 min |
| | Lesson 2: Types of Runs | Video | 10 min |
| | Lesson 3: Alternative Ways to Trace | Video | 11 min |
| | Lesson 4: Conversational Threads | Video | 5 min |
| | Module 1 Feedback | Survey | 2 questions |
| **Module 2: Testing and Evaluation** | Module 2 Introduction | Video | < 1 min |
| | Module 2 Resources | Text | — |
| | Lesson 1: Datasets | Video | 15 min |
| | Lesson 2: Evaluators | Video | 15 min |
| | Lesson 3: Experiments | Video | 11 min |
| | Lesson 4: Analyzing Experiment Results | Video | 10 min |
| | [Optional] Lesson 5: Pairwise Experiments | Video | 10 min |
| | [Optional] Lesson 6: Summary Evaluators | Video | 5 min |
| | Module 2 Feedback | Survey | 2 questions |
| **Module 3: Prompt Engineering** | Module 3 Introduction | Video | < 1 min |
| | Module 3 Resources | Text | — |
| | Lesson 1: Playground | Video | 13 min |
| | Lesson 2: Prompt Hub | Video | 10 min |
| | Lesson 3: Prompt Engineering Lifecycle | Video | 8 min |
| | Lesson 4: Polly | Video | 4 min |
| | Module 3 Feedback | Survey | 2 questions |
