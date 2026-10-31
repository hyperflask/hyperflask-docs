# Coding with agents

Hyperflask is optimized for coding with agents. Hyperflask high-level abstractions allow agents to efficiently create apps and maintain them long term.

Hyperflask-Start provides all the needed tools to get you started with agent coding:

- A proper `AGENTS.md` file
- A set of usefull skills (including the Hyperflask skill)
- Testing tools for agents
- Your coding agent installed and authenticated in the dev container

## Agent in the dev container

When creating a project, Hyperflask-Start asks which coding agent you want to use: Claude Code, OpenAI Codex or OpenCode.

The selected agent is installed in the dev container. Your credentials and settings are mounted from your host machine, so the agent is authenticated and ready to use from a terminal inside the container (`claude`, `codex` or `opencode`).

| Agent | Mounted from the host |
| --- | --- |
| Claude Code | `~/.claude` and `~/.claude.json` |
| OpenAI Codex | `~/.codex` |
| OpenCode | `~/.config/opencode` and `~/.local/share/opencode` |

!!! note
    On macOS, Claude Code stores its credentials in the Keychain. You will need to log in once inside the container.

Running the agent inside the dev container gives it access to the same environment as your app: dependencies, database, browser for testing, etc.

## Installing the agent skill

The hyperflask skill contains the full Hyperflask documentation. It is installed automatically in projects created with Hyperflask-Start.

To install or update it in an existing project, run:

```
npx skills add https://hyperflask.dev --skill hyperflask
```

## Customizing AGENTS.md

The provided file is very generic and does not describe your project. Add your project description at the top of the file.