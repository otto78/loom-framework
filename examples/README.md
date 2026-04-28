# Loom Framework — Examples

This directory contains example projects that demonstrate how Loom Framework works in practice.

## Available Examples

| Example | Description | Stack |
|---------|-------------|-------|
| [`python-api-project/`](./python-api-project/) | A FastAPI project with Loom fully configured | Python, FastAPI |

## How to Use an Example

Each example contains:
- A pre-filled `PROJECT.md` showing what information Loom needs
- A generated `AGENT.md` showing what the agent will read each session
- Example `docs/TASKS.md`, `docs/STORY.md` showing the task lifecycle
- Example IDE config files

## Contributing an Example

To add your own example:
1. Create a new directory: `examples/your-project-name/`
2. Add a `PROJECT.md` describing the project
3. Run `python loom/scripts/setup.py --auto` to generate the Loom files
4. Add a `README.md` explaining what the example demonstrates
5. Open a PR!
