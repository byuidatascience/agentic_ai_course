Main outcomes per day in [brackets], IDs from course_design/course_outcomes.md. "?" = best guess from the day title.

Week 1
0.1 - Intro: Is this course for me? Yes - [5.5, 4.1.1]
1.1 - API: Make a call, get a response - [1.1.1, 1.1.3]
1.2 - Concepts, internals of an agent, tools and memory - [1.3.1, 1.4.1, 4.1.1]
Week 2
1.3 - Group, solve a problem together - [? 3.1 or 1.2]
1.4 - Setup tools and memory locally - [1.4.1, 1.3.1]
1.5 - Sub-agents as tools, basic prompting - [1.6, 1.2, 1.1.2]
Week 3
1.6 - MCP, what it is, get connected - [1.4.2]
1.7 - MCP deepen uses: file system, web browsing - [1.4.2]
1.8 - Ethics discussion, Work day - [6.1, 6.2]
Week 4
1.9 - Long-term memory - [1.3.2]
1.10 - Long-term memory - [1.3.2]
1.11 - CLI, skills, plugins, oh my - [1.4.3, 1.2]
Week 4
2.1 - Debrief, review and intro - [4.2.2, 4.1.2]
2.2 - Tracing - Read and Instrument - [2.1.1, 2.1.2]
2.3 - Failure Modes, Advanced tracing - [2.3.2, 2.1.3]
Week 5
2.4 - Advanced tracing - [2.1.3, 2.3.1]
2.5 - Testing pipeline (datasets, LLM as judge, experiments) - [2.2.4, 4.1.2]
2.6 - Golden datasets - [2.2.3, 3.3.4]
Week 6 (May 25)
2.7 - LLM as judge (use defaults) - [2.2.2]
2.8 - Experiments (first time, with premade examples) - [2.2.4, 2.2.5]
2.9 - Alignment (define it for project agent) - [3.3.1, 3.3.3, 6.5]
Week 7 (June 1)
2.10 - Better datasets - [2.2.3, 3.3.4]
2.11 - Production datasets (they use the agent) - [2.1 (production), 3.3.5]
2.12 - Better judges (what actually matters?) - [3.3.1, 3.3.3]
Week 8 (June 8)
2.13 - Better judges (you define/modify) - [2.2.2, 2.3.3]
2.14 - Communication & ethics - [4.3.2, 4.3.3, 4.3.4]
2.15 - Project work - [—]
Week 9 (June 15)



Module 3 high level concept: 
- judgment layer: choosing and tuning levers based on diagnostic feedback to hit human-defined reliability goals
- deliberately steer an agent toward human-defined reliability and objectives


Environment direction:
Colab -> Local .py -> Gradio -> Slack -> agent-chat-ui (maybe)
(Streamlit, chainlit?)


## Unplaced Proposals

- Context Engineering Types - [1.3.3]
- Defining an agent's purpose without code - [3.1]
- AI viability: LLM limits, expensive parts of a build, cost estimates - [3.2.1, 3.2.2, 3.2.4]
- Predicting failure points - [3.2.3]
- Eliciting domain knowledge from clients/employees - [3.4]
- Defining success criteria and safety requirements - [3.3.1, 3.3.2, 3.3.3]
- Context needs at each step of a task - [3.5, 1.3.3]
- Comparing and choosing harness architectures - [3.6, 3.6.1, 1.6]
- Writing agent- and human-readable docs (AGENTS.md, specs, schemas) - [3.7, 1.2]
- Human-in-the-loop and permissions - [1.5.1, 1.5.3]
- Sandboxed code execution - [1.5.2]
- Error handling and retries - [1.5.4]
- Deterministic evaluators (or move to Unit 2) - [2.2.1, 3.3.3]
- Iterating on an agent from eval results - [2.3.1, 2.2.5, 3.3.5]
- Cost and latency: model choice per sub-agent, caching - [1.1.2, 3.2.4]
- Engineering terms: prompt, context, harness, intent - [4.1.3]
- Presenting an agent to a non-technical audience - [4.3.1, 4.2.2]
- Publishing a project write-up - [4.2.1]
- Ethics: gospel principles and AI's impact on others - [6.4, 6.3]
- [5.4]

### The One Things

"Tools from many servers all end up in one list the model picks from, so more servers means more power and more confusion."
"Every MCP server you connect is a new power and a new risk. Judge a server before you give it to your agent."

## More Open Questions

Is Outcome 1.5 (guardrails) a Module 3 anchor, or should Module 1 at least touch it (e.g., human-in-the-loop in 1.5 or 1.6)?
Which competencies do you consider taught throughout? My guess is 5.x, 1.2 and 4.1. If we list those explicitly as threads, every remaining gap is a real gap.
Is 2.2.1 left out on purpose, or should it replace one of the dataset or judge days?