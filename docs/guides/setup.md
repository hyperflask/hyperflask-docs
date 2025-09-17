# Setup

## Requirements

Hyperflask simplifies development environments by standardizing everything around containers.

VS Code is also the recommended editor (and currently the only one with syntax highlighting for Jinjapy files).

What you will need:

- A UNIX like system (Linux, MacOS or [WSL on Windows](https://learn.microsoft.com/en-us/windows/wsl/install))
- [Docker](https://www.docker.com/)
- [VS Code](https://code.visualstudio.com/)

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
4. Create `package.json` with required packages (see after)
5. Create a pages directory: `mkdir pages`
6. Create your index page: `echo "hello world" > pages/index.html`
7. Start a development server using `hyperflask dev`

Required npm packages:

```json
{
  "dependencies": {
    "alpinejs": "^3.14.9",
    "bootstrap-icons": "^1.13.1",
    "htmx-ext-sse": "^2.2.3",
    "htmx.org": "^2.0.4"
  },
  "devDependencies": {
    "@tailwindcss/cli": "^4.1.6",
    "daisyui": "^5.0.35",
    "esbuild": "^0.25.4",
    "tailwindcss": "^4.1.6"
  }
}
```