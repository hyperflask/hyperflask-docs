# Setup

## Requirements

Use [Hyperflask-Start](https://github.com/hyperflask/hyperflask-start) to create new projects and VS Code as editor (as the starter template deeply integrates with it).

What you will need:

- [Docker](https://www.docker.com/)
- [VS Code](https://code.visualstudio.com/)

If you are on Windows, use [WSL](https://learn.microsoft.com/en-us/windows/wsl/install).

Python is not needed on your machine, everything will be executed inside containers.

## Installation

Launch the following command to create your project:

    curl -L https://raw.githubusercontent.com/hyperflask/hyperflask-start/start.sh | bash

This will prompt you for some options and create the project in a new folder.

## Development environment

Open your project folder in VS Code. It should prompt you to "re-open workspace in development container" which you should accept. VS Code will create and start the development container and re-launch itself.

You are now developping from the container inside which you will find Python 3.11, Node & npm and hyperflask installed.