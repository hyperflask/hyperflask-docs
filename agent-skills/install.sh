#!/bin/bash

install-skill() {
    mkdir -p .claude/skills
    cd .claude/skills
    wget --no-parent -r https://hyperflask.dev/agent-skills/$1
}

# wrap in main to prevent partial execution if failed download
main() {
    command -v wget >/dev/null 2>&1 || { echo "wget is required but not installed."; exit 1; }

    install-skill hyperflask
    install-skill hyperflask-ai
    install-skill hyperflask-assets
    install-skill hyperflask-background-tasks
    install-skill hyperflask-components
    install-skill hyperflask-emails
    install-skill hyperflask-files
    install-skill hyperflask-forms
    install-skill hyperflask-metadata
    install-skill hyperflask-models
    install-skill hyperflask-push
    install-skill hyperflask-security-headers
    install-skill hyperflask-ui
    install-skill hyperflask-users-and-auth
}

main