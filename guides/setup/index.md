# Setup

## Requirements

Hyperflask simplifies development environments by standardizing everything around containers.

VS Code is also the recommended editor (and currently the only one with syntax highlighting for Jinjapy files).

**What you will need:**

- A UNIX like system (Linux, MacOS or [WSL on Windows](https://learn.microsoft.com/en-us/windows/wsl/install))
- [Docker](https://www.docker.com/)
- [VS Code](https://code.visualstudio.com/) with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

Python is not needed on your machine, everything will be executed inside containers.

Additional VS Code extensions will be suggested when you open a project:

 - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
 - [SQLORM Syntax Highlighting](https://marketplace.visualstudio.com/items?itemName=hyperflask.sqlorm-language-support)
 - [Jinjapy Language Support](https://marketplace.visualstudio.com/items?itemName=hyperflask.jinjapy-language-support)

## Starting a new project using Hyperflask-Start

[Hyperflask-Start](https://github.com/hyperflask/hyperflask-start) is the starter kit for Hyperflask projects. It is the recommended experience.

Launch the following command to create your project:

    curl -L https://raw.githubusercontent.com/hyperflask/hyperflask-start/main/start.sh | bash

This will prompt you for some options and create the project in a new folder.

!!! note
    The start.sh script is very simple and uses a container to create a new project using [cookiecutter](https://cookiecutter.readthedocs.io).  
    To directly create a project using cookiecutter, run the following command:
    
    ```
    cookiecutter gh:hyperflask/hyperflask-start
    ```

## Launching using VS Code and dev containers

Open your project folder in VS Code. It should prompt you to "re-open workspace in development container" which you should accept. VS Code will create and start the development container and re-launch itself.

You are now developping from the container inside which you will find recent versions of Python, Node & npm and hyperflask installed.

Once your VS Code workspace is ready, start your app in a VS Code Terminal:

```
uv run hyperflask dev
```

## Advanced

Although **VS Code with dev containers is the recommended experience**, it is not mandatory. Hyperflask apps are standard python apps and you can install their requirements in a virtualenv and start a server using the CLI.

### Launching without dev containers

First [create a project using Hyperflask-Start](#starting-a-new-project-using-hyperflask-start).

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

### Installation without Hyperflask-Start

!!! warning
    All the documentation assumes you are using Hyperflask-Start

This installation method works with any python package manager

1. Ensure that your system meet the requirements
1. Create your project directory: `mkdir example-project && cd example-project`
2. Create and activate a virtualenv: `python -m venv .venv && source .venv/bin/activate`
3. `pip install hyperflask`
5. Run `npm install esbuild tailwindcss @tailwindcss/cli htmx.org htmx-ext-sse bootstrap-icons daisyui`
4. Run `mkdir pages && echo "Hello world" > pages/index.jpy`
6. Start a development server using `hyperflask dev`
