# Setup

## Requirements

Hyperflask simplifies development environments by standardizing everything around containers.

VS Code is also the recommended editor (and currently the only one with syntax highlighting for Jinjapy files).

What you will need:

- A UNIX like system (Linux, MacOS or [WSL on Windows](https://learn.microsoft.com/en-us/windows/wsl/install))
- [Docker](https://www.docker.com/)
- [VS Code](https://code.visualstudio.com/) with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

Python is not needed on your machine, everything will be executed inside containers.

## Installation using Hyperflask-Start

We will use [Hyperflask-Start](https://github.com/hyperflask/hyperflask-start) to create our project.

Launch the following command to create your project:

    curl -L https://raw.githubusercontent.com/hyperflask/hyperflask-start/main/start.sh | bash

This will prompt you for some options and create the project in a new folder.

## Launching using VS Code and dev containers

Open your project folder in VS Code. It should prompt you to "re-open workspace in development container" which you should accept. VS Code will create and start the development container and re-launch itself.

You are now developping from the container inside which you will find Python 3.11, Node & npm and hyperflask installed.

## Advanced

Although **VS Code with dev containers is the recommended experience**, it is not mandatory. Hyperflask apps are standard python apps and you can install their requirements in a virtualenv and start a server using the CLI.

### Launching without dev containers

First [create a project using Hyperflask-Start](#installation-using-hyperflask-start).

1. Ensure that your system meet the requirements:
    - Python (>=3.10)
    - [uv](https://docs.astral.sh/uv/)
    - [nodejs](https://nodejs.org/fr) (>=22)
2. Run `npm install`
3. Launch app using `uv run hyperflask dev`

### Launching with devcontainers-cli

If you are not using VS Code but want to use dev containers, a CLI tool is available:

1. [Install devcontainers-cli](https://github.com/devcontainers/cli#npm-install)
2. Start dev container: `devcontainer up --workspace-folder .`
3. Launch your app: `devcontainer exec uv run hyperflask dev`
3. Go to http://localhost:5000

### Installation without Hyperflask-Start

This installation method works with any python package manager

1. Ensure that your system meet the requirements
2. Create your project directory: `mkdir example-project && cd example-project`
2. Create and activate a virtualenv: `python -m venv .venv && source .venv/bin/activate`
3. `pip install hyperflask`
4. Run `hyperflask init .`
5. Run `npm install`
6. Start a development server using `hyperflask dev`
