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

!!! info
    Although it is not mandatory, Hyperflask-Start is the officially recommended experience.

Launch the following command to create your project:

    curl -L https://raw.githubusercontent.com/hyperflask/hyperflask-start/main/start.sh | bash

This will prompt you for some options and create the project in a new folder.

Open your project folder in VS Code. It should prompt you to "re-open workspace in development container" which you should accept. VS Code will create and start the development container and re-launch itself.

You are now developping from the container inside which you will find Python 3.11, Node & npm and hyperflask installed.

## Installation without Hyperflask-Start

1. Create your project directory: `mkdir example-project && cd example-project`
2. Create and activate a virtualenv: `python -m venv .venv && source .venv/bin/activate`
3. `pip install hyperflask`
4. Run `hyperflask init .`
5. Start a development server using `hyperflask dev`
