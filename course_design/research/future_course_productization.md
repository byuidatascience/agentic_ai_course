# A Possible Follow-On Course: Productization & Production

Holding pen for material that keeps trying to live in this course but belongs to a later one. Nothing
here is committed; this is a place to put things down so they stop distorting DS 488's scope.

The idea already has a seed in [open_tensions.md](open_tensions.md):

> "The loop really isn't complete without production. Maybe the end-to-end loop doesn't exist in this
> class — it's implemented in the following class where deployment and in-production observation are
> critical?"

That is the thesis of this document. DS 488 ends at "a reliable agent you can run and defend." The
follow-on course would start there.

---

## What has been pushed here, and from where

### UI and productization

**Moved out of:** `teaching_philosophy.md` — the phrase "the productization project may be group-led"
under Belonging/Group Work, and "create a UI" in the end-of-semester coding interview.

**Why it had to move:** [user_profiles.md](../user_profiles.md) already declares it out of scope, in
the Greenfielder exit profile:

> Outside the scope of this course is:
> - Turning an agent into a product with meaningful UI beyond a basic chat interface
> - Hosting and scaling the agent

`teaching_philosophy.md` is the older document and predates that boundary. The boundary wins; the
ambition goes here.

### Deployment

**Never in scope, but keeps leaking in.** `course_outcomes.md` says it explicitly under Outcome 1:

> *Only implementation to exist functionally, design and deployment are out of scope.*

An earlier draft of `irm.md` had grown a "1.3 Deploy" row anyway. That has been removed. Deployment,
hosting, and scaling are the natural spine of a second course.

### The complete build → observe → refine loop

DS 488 teaches the loop's edges — build (U1), observe and diagnose (U2), refine (U3) — but a student
never runs a full cycle against real production traffic, because there is no production. The
end-to-end loop, with live users generating the traces, is the thing this course structurally cannot
deliver.

---

## Candidate shape, if it is ever built

Rough, unvalidated, in rough dependency order:

1. **Deployment** — getting an agent off a laptop. Environments, secrets, cost controls.
2. **Interface** — chat is the floor; what does an agent-shaped product actually look like? Streaming,
   interruption, approval UX, showing the agent's work, failure states.
3. **Production observability** — online evals against real traffic, not offline datasets. Sampling,
   alerting, drift, regression gates in CI.
4. **The live loop** — ship, watch real users break it, fix, re-ship, with the measurement discipline
   from DS 488 Unit 2 applied continuously instead of once.
5. **Scale and cost at volume** — caching, routing, model tiering, rate limits, on-call.

## Open questions

- Is this one course or two (a deployment/infra course and a product/UX course)?
- Does it require DS 488 as a prereq, or does it re-teach a compressed version of the harness?
- Is the audience the same? The Greenfielder and Brownfielder profiles in
  [user_profiles.md](../user_profiles.md) both point at it; the Personal Use profile does not.
- Who teaches UI? That is a different department's competency than agent engineering.

## What to watch for in DS 488 meanwhile

Every time a DS 488 design decision stalls on "but they'd need to deploy it to really see this" —
note it here rather than expanding the course. That accumulating list is the actual evidence for
whether the follow-on course is needed.
