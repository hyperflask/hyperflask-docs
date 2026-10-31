# Install Hyperflask

> Instructions for coding agents to set up a new Hyperflask project on behalf of the user.
> Human readable documentation is available at <https://hyperflask.dev>.

Hyperflask is a batteries-included full stack web framework built on Flask. It is optimized for containerized, component-driven, HTMX-based web apps.

New projects are created using [Hyperflask-Start](https://github.com/hyperflask/hyperflask-start), the official starter kit. Development happens inside a [dev container](https://containers.dev/): Python is not needed on the host machine.

Follow these steps in order. Do not skip the requirement checks.

## 1. Check the requirements

Required:

- A UNIX like system: Linux, macOS or [WSL on Windows](https://learn.microsoft.com/en-us/windows/wsl/install). On Windows, run all commands from inside WSL.
- [Docker](https://www.docker.com/), with the daemon running. Check with `docker info`.

To work in the dev container, one of:

- [VS Code](https://code.visualstudio.com/) with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) (recommended). Check with `code --list-extensions | grep ms-vscode-remote.remote-containers`.
- [devcontainers-cli](https://github.com/devcontainers/cli#npm-install), to use dev containers from a terminal without VS Code. Check with `devcontainer --version`.

If Docker is missing or not running, stop and ask the user to install or start it. Do not install system software without the user's consent.

Without Docker, Hyperflask can still run directly on the host if it has Python >= 3.11, [uv](https://docs.astral.sh/uv/) and [nodejs](https://nodejs.org) >= 24. This is not the recommended setup: mention it to the user and only use it if they agree.

## 2. Ask the user for the project options

Ask the user for:

- **Project name**: for example `My Hyperflask App`. The project folder is derived from it: lowercased, with spaces, dashes and dots replaced by underscores (`my_hyperflask_app`).
- **Coding agent** to install in the dev container: `claude` (Claude Code), `codex` (OpenAI Codex), `opencode` (OpenCode) or `none`. Default to the agent you are.
- **Parent directory** where the project folder will be created. Default to the current directory.

Make sure the project folder does not already exist.

## 3. Create the project

Run the official `start.sh` script from the parent directory. Provide the options using the `HYPERFLASK_PROJECT_NAME` and `HYPERFLASK_AGENT` environment variables so that it runs without prompting:

```bash
curl -L https://start.hyperflask.dev | HYPERFLASK_PROJECT_NAME="My Hyperflask App" HYPERFLASK_AGENT=claude bash
```

This runs in a docker container using the same image as the dev container. It generates the project with [cruft](https://cruft.github.io/cruft/), creates a `.env` file with a secret key and installs the agent skills (including the hyperflask skill).

If the host already has uv and nodejs, the same can be done without Docker:

```bash
uvx cruft create --no-input --extra-context '{"project_name": "My Hyperflask App", "agent": "claude"}' https://github.com/hyperflask/hyperflask-start
```

Then initialize a git repository in the project folder and make a first commit (`git init && git add . && git commit -m "Initial commit"`). This is required to later update the project from the template using `uvx cruft update`.

## 4. Start the development environment

### With VS Code (recommended)

The dev container must be opened by the user:

1. Open the project folder in VS Code (`code <project_folder>`).
2. Accept the "Reopen in Container" prompt, or run the "Dev Containers: Reopen in Container" command from the Command Palette.
3. Wait for the container to build. Dependencies are installed automatically.
4. In a VS Code terminal, start the development server: `uv run hyperflask dev`

### With devcontainers-cli

From the project folder:

1. Start the dev container: `devcontainer up --workspace-folder .`
2. Start the development server: `devcontainer exec --workspace-folder . uv run hyperflask dev`

The coding agent selected in step 2 is installed in the dev container and authenticated using the user's credentials from the host. It can be launched with `devcontainer exec --workspace-folder . claude` (or `codex`, `opencode`).

### Without containers

From the project folder:

1. `uv sync`
2. `npm install`
3. `uv run hyperflask dev`

## 5. Verify the installation

The development server listens on <http://localhost:5000> with auto-reload enabled. Check that the home page loads.

Emails sent in development are caught by [Mailpit](https://github.com/axllent/mailpit), available at <http://localhost:8025> when using the dev container.

## 6. Next steps

Tell the user the project is ready and summarize:

- Where the project is and how to start the development server.
- That the project contains an `AGENTS.md` file which they should complete with a description of their project.
- That the coding agent is available inside the dev container.

To build the app, use the hyperflask skill installed in the project. It contains the full documentation. If it is missing, install it with `npx skills add https://hyperflask.dev --skill hyperflask`.

Useful links:

- Documentation: <https://hyperflask.dev>
- Getting started tutorial: <https://hyperflask.dev/getting-started/>
- Documentation for LLMs: <https://hyperflask.dev/llms.txt> and <https://hyperflask.dev/llms-full.txt>
