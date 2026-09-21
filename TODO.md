# Overview

As of Spring 2026 end of semseter, the shape of the course is highly defined. The implementation is little. There are some major bones in place already:
- Course outcomes and competencies (what is taught)
- The shape of major assessments
- Unit topics
- Well-defined teaching philosophy (the "why")
- Daily schedule
- Website structure
- Grading shape
- Various activities and assessments
- Teachers notes through unit 1 and part of unit 2
- Some readings

Most items are mostly defined shapes, with few genuine deliverables. This is at a high leverage decision point.

The course currently exist just prior to commitment on a tech framework. Pivot is easy before constructing lesson content.

# Itemized

## Immediate: prepare Day 1 and Day 2

This is the short-term working queue. Complete or consciously defer these before publishing/running the relevant lesson; do not let the broader build-out obscure them.

### Day 1: first LLM call in Google Colab

- [ ] Revise the opening discussion so it follows the actual preparation reading, **Agent Engineering**, rather than asking students to report on an API prep they did not read.
- [ ] Decide the in-class artifact: a purpose-built Day 1 Google Colab, or an adapted version of `practice/practice1_1.ipynb`.
  - [ ] Give students one canonical link that opens the artifact directly in Colab.
  - [ ] Include only the essential launch sequence: store `GOOGLE_API_KEY` in Colab Secrets, install packages, and make one LLM call.
- [ ] Run the canonical path from a student perspective in a fresh Colab session: API-key retrieval, secret permission, package install, and first response.
- [ ] Decide what must be taught live after setup (versus discovered through guided experimentation): API/agent-engineering framing, system prompts, temperature, token limits, and the distinction between an LLM call and an agent.
- [ ] Decide whether slides earn their place. If yes, create only the slides needed for the live concepts and transitions; if no, make the lesson page/notebook carry those explanations.
- [ ] Write and verify an explicit **What to do next** menu for students who finish setup early:
  - [ ] First: verify a partner's setup or help troubleshoot.
  - [ ] Then: complete a bounded prompt/configuration experiment.
  - [ ] Then: begin optional/stretch work without skipping the class's shared checkpoints.
- [ ] Decide whether `practice/practice1_1.ipynb` is sufficiently open-ended and worthwhile for after class; revise its scope, prompts, or stretch work if it is only a repeat of class.
- [ ] Establish a simple in-class contingency for a student who cannot get a key or Colab working, without sending them into local-machine setup on Day 1.

### Day 1 release check

- [ ] Ensure the student-facing Day 1 page, preparation link, Colab link, and next-step menu all agree and work after rendering.
- [ ] Remove or correct Day 1 links that promise a real example, slide deck, or practice route but lead elsewhere.

## Now

[x] Solidify course competencies (course_outcomes.md)
[x] Enter learning outcomes and milestones into repository
[ ] Visit every lesson and create instructor notes and revisions notes
[ ] Create documents for the following deliverables
- [ ]  Daily instructor notes (✓ 1.1-1.8; 2.1-2.3)
- [ ]  Grading rules (needs more in depth)
- [ ]  Daily student-facing lesson plan
- [ ]  Readings
- [ ]  Practices
- [ ]  Project instructions and guiding documents
    - [/] Project 1
        - [ ] Create MCP for them to connect to and submit responses
    - [ ] Project 2
        - [ ] Create initial agent for them to clone, instrument, and diagnose
        - [ ] Guide explaining what they need to submit and when
    - [ ] Project 3
        - [ ] Create Slack agents to interrogate for problem
        - [ ] Guide for what to submit and when
- [ ] Asessment content
- [ ] Activity content
    - [ ] (currently have prototypes)
- [ ]  Student resources
    - [ ] Semester overview
    - [ ] Cheat sheet
- [/]  Syllabus

## Whenever

[ ] Create Claude skill for taking the template and context (lesson outline, outcomes, previous lesson, constitution) and making a lesson
[ ] Create Claude skill for updating the lesson given current standards
[ ] Easy skill for creating slides with revealjs
    [ ] Probably needs to start with brainstorming what needs to go in the slides - a good outline (including discussion on what visualizations would be useful)

[ ] Decouple the Quarto render from git so multiple agents can work the repo at once
    [ ] `docs/` is tracked output; every render rewrites ~144 files, so any two agent branches collide
    [ ] Full plan, workflow file, and fallbacks: `scratch/decouple_render_from_git.md`
    [ ] Final step needs admin on the GitHub repo (Pages source → GitHub Actions)
