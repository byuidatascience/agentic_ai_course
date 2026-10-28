# Lesson 2.1 design log

## Instructor's starting request (2026-10-12)

1. Unit 1 / Project 1 review: planned activities and good questions, what we saw in projects, what was hardest, success stories, award for most MCPs.
2. Transition into Unit 2 using the course map, plus a new Unit 2 map (instructor to make).
3. Textbook this unit: LangChain Academy "Intro to LangSmith."
4. Project 2: a report (a few types); aim to get there in 3 weeks, then 2 weeks to fix the agent and deliver the final version.
5. Introduce ACME.io, the tech division of ACME. Subtle humor (instructor supplies), clear story per `course_design/learning_arcs.md`.
6. LangSmith intro: show traces, students make an account and click around. No local environment setup yet.

## Conflicts flagged (resolved)

- Local setup and tracing their own Unit 1 agent moved to 2.2 in `drafts/unit2_one_things.md`.
- "Bad": students may hear it after Unit 1, but as a gradual reveal, not the one-shot "You made a BAD agent!" in `instructor_notes/notes2_1.qmd`. `learning_arcs.md` updated.

## Open notes (revise later)

- **ACME agent not built yet.** That drives Unit 2 timing. For now: "access as soon as our lead technician gets around to it"; students do training materials meanwhile. Revisit the 3-week report / 2-week fix split once the agent exists.
- **Story mostly ready, not complete:** failure moment still open. Options pitched: (A) goodbye sticky note "It works. Don't touch it."; (B) customer asks why the agent said something odd; (C) CFO asks "Is this agent worth what we pay for it?" (ties to Project 2 report). Departed engineer has no name/backstory yet.
- **Intern vs. AI Engineer:** story says interns; `projects/project2_resources/resource.md` says AI Engineer. Reconcile.

## Conventions

- Most Important Thing is instructor-facing. Destination is student-facing.

## Phase status

- [x] Phase 1: Most Important Thing + destination
- [ ] Phase 2: Story + objectives
- [ ] Phase 3: Module outline
- [ ] Phase 4: Prototype
- [ ] Phase 5: Content

## Decisions

**Most Important Thing (approved):** They leave asking, "How would I even know if an agent is good?" Secondarily, they feel hired at ACME.io and know what their boss expects in the Project 2 report.

**Objectives (approved):**

- Discuss Project 1's biggest wins and hardest moments as a group and class `4.2.2`
- Write down the lessons from Unit 1 they're carrying forward `4.2.2`
- Gain a clear vision and expectation for Unit 2 and Project 2 `4.1.2`
- Orient themselves as new hires at ACME.io (story setup; no id)
- Obtain a LangSmith account (setup; no id)
- Click around a real trace `2.1.2`

**ACME story material (instructor's):**

- ACME Corporation: a company making everything from cartoon explosives to dirt-flavored toothpaste
- Established 1920
- ACME.io is its tech division, founded at the start of the internet age, starting with website.com
- They have a beautiful, robust agent that does everything
- The trouble: the one person who knew what it does has left
- We're hiring you as interns to figure out what it does and make it better
- Orientation: interns go through training materials; they get access to the agent "as soon as our lead technician gets around to it" (corporate humor)
- Possible callback: ACME Clothing's chatbot vs. Shelley and the blue hoodie (`drafts/lesson1_2/lesson1_2.qmd`)

**Story premise (approved): B then A.**

- B (mirror): end of review: "If you left tomorrow, could anyone tell what your Project 1 agent does, or whether it's any good?"
- A (ACME): ACME.io is that exact situation: the one person who knew what the agent does left. Groups brainstorm how they'd find out without its builder → "watch what it actually does" → traces.

**Unit 1 review: candidates (not approved)**

Activities:
1. Lessons on paper: write silently → share in groups → class fills gaps (from `notes2_1.qmd`)
2. "Who had this problem?": hands up for struggles we saw (async, confusing errors, setup, agent hard to reach)
3. Lightning demos: 60 seconds per agent; class awards (most MCPs, most useful, most chaotic)
4. Failure museum: each group shows its best failure, priming failure-spotting (`unit1_one_things.md` thread 6) and setting up the mirror question

Questions:
- When did you know your agent "worked"? How did you know? (primes the One Thing)
- What did your agent do that surprised you, good or bad?
- What does your agent do that you'd actually use tomorrow?
- With one more week, what would you fix first?
- What did building without AI coding help teach you?
- What would you tell yourself on day 1.1?

**Destination (approved):** "I've closed the book on Project 1: celebrated it, wrote down what I learned, and I'm ready to give Unit 2 my full attention with a clear path forward."
