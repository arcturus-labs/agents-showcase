# agents-showcase

Demo code for **"Build Your Own Agent — Escaping the Harness,"** a lightning talk that strips the agent harness down to its core and then rebuilds it step by step, demonstrating three things:

1. **Agents are simpler than they look** — a model + a loop + tools is the whole core.
2. **Agents can do more than coding work** — with the right instructions and tools they become reviewers, researchers, assistants.
3. **Agents can live far beyond the terminal** — embedded inside products, or interacting with products from the outside.

> Full slide outline: [presentation-workbench/examples/unharness-the-agent/planning/outline.md](https://github.com/the-rooks-nest/presentation-workbench/blob/main/examples/unharness-the-agent/planning/outline.md)

---

## How to run

All examples live in `src/`. From the repo root:

```bash
agents-from-simple-to-complex/.venv/bin/python src/N-<name>.py
```

A `.env` file at the repo root with `ANTHROPIC_API_KEY=…` is expected (`load_dotenv` handles the rest).

---

## The demo ladder

Each example adds one idea on top of the last.

| # | File | What it demonstrates |
|---|------|---------------------|
| 1 | `1-just-a-model.py` | Text in, text out. The prompt is still part of the program. |
| 2 | `2-tool-loop.py` | A manual tool-calling loop. The model can now see outside itself. |
| 3 | `3-pydantic-ai.py` | Same pattern standardized with PydanticAI. |
| 4 | `4-pydantic-ai-read-write-edit.py` | Read, write, and shell tools — enough to feel like a coding agent. |
| 5 | `5-pydantic-ai-research-skills.py` | Skills, web search, filesystem, shell. English as the programming language. |
| 6 | `6-pydantic-ai-assistant-w-compaction.py` | Sessions, hooks, and history compaction. |
| 7 | `7-pydantic-ai-reviewer.py` | Structured output, agent-as-embedded-service, an example non-coding agent. |

Example 7 is the bridge from "agents in a terminal" to "agents inside products" — it screens a job application using a skill file ([`skills/screen-candidate/SKILL.md`](skills/screen-candidate/SKILL.md)) and returns structured output that application code can consume.

## Repo structure

```
agents-showcase/
  .env                          ← API key (gitignored)
  src/                          ← all demo scripts
    event_logging.py            ← shared ANSI trace printer
    1-just-a-model.py
    2-tool-loop.py
    ...
    7-pydantic-ai-reviewer.py
  skills/
    screen-candidate/SKILL.md   ← skill used by demo 7
  agents-from-simple-to-complex/  ← pyproject.toml + venv
```
