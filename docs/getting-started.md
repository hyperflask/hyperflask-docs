---
hide: [navigation]
---
# Getting started

Welcome to Hyperflask! In this getting started guide will cover the basics and create a simple chat app with authentication.

The result of this tutorial is available as a git repository at <https://github.com/hyperflask/getting-started>.

## Meet Hyperflask

Hyperflask is an opiniated full stack rapid web development framework. It uses Python on the backend, powered by the Flask framework and javascript with htmx on the frontend.

Hyperflask includes everything you need to develop an app from start to finish: 
 
 - Easy backend development
 - UI framework and components
 - Sending emails
 - Background tasks
 - Deployment

Check out the full list of technologies used in Hyperflask on the [Why Hyperflask page](/why)

## What you will need to install and run Hyperflask

Hyperflask simplifies development environments by standardizing everything around containers.

VS Code is also the recommended editor (and currently the only one with syntax highlighting for Jinjapy files).

What you will need:

- A UNIX like system (Linux, MacOS or [WSL on Windows](https://learn.microsoft.com/en-us/windows/wsl/install))
- [Docker](https://www.docker.com/)
- [VS Code](https://code.visualstudio.com/)

Python is not needed on your machine, everything will be executed inside containers.

## Installation

We will use [Hyperflask-Start](https://github.com/hyperflask/hyperflask-start) to create our project.

Launch the following command to create your project:

    curl -L https://raw.githubusercontent.com/hyperflask/hyperflask-start/main/start.sh | bash

This will prompt you for some options and create the project in a new folder.

Open your project folder in VS Code. It should prompt you to "re-open workspace in development container" which you should accept. VS Code will create and start the development container and re-launch itself.

You are now developping from the container inside which you will find Python 3.11, Node & npm and hyperflask installed.

!!! info
    Although VS Code with development containers is the recommended experience, it is not mandatory. Hyperflask apps are standard python apps and you can install their requirements in a virtualenv and start a server using the CLI.

## Running your app

In VS Code, press F5 or "Start debugging" in the command palette.

The browser will automatically open to your new site!

Auto-reload is enabled.

## First look at the code base

In your project folder, you will find the following files and folders:

 - **app**: your app code
    - **assets**: scripts and stylesheets that will be bundled using [esbuild](https://esbuild.github.io/)
        - **main.css**: tailwind entrypoint
    - **components**: components to compose your app
    - **pages**: your site pages
 - **public**: all files in this folder are publicly accessible
 - **tests**: tests using [pytest](https://pytest.org)
 - **.env**: environment variables
 - **config.yml**: your app configuration file
 - **Dockerfile**: Dockerfile to build your production image
 - **pyproject.toml**: list python dependencies and tool options
 - **package.json**: list javascript dependencies

## Starting our chat app

First, let's create a basic chat window with some messages. Replace the content of `app/pages/index.jpy` with the following:

```
{% use_layout %}
<div id="messages">
    <{ChatBubble}>First message!</{ChatBubble}>
    <{ChatBubble}>Second message!</{ChatBubble}>
</div>
```

This page is made of a jinja template. We are using the `{% use_layout %}` directive to automatically extend from the default layout.

We are using the built-in `ChatBubble` component that is provided by [daisyUI](https://daisyui.com) and comes as part of Hyperflask UI toolkit.

Components are included on the page using a [special jinja syntax](/guides/components).

!!! info
    Note the `jpy` file extension which references the [jinjapy](https://github.com/hyperflask/jinjapy) file format.

## Creating a re-usable component

Now that we have the basic layout of our app, let's extract the chat bubble as an independant component that will handle posting new messages.

We are going to create a `ChatMessage` component to render one message. In `app/components/ChatMessage.jpy`:

```
---
from hyperflask import request

def post():
    return {"message": request.form["message"]}
---
<{ChatBubble}>
    {{props.message|markdown}}
</{ChatBubble}>
```

The [component](/guides/components) is made of a [jinja template](https://jinja.palletsprojects.com/). It receives a `props` variable that contains all the properties passed to the component.

We have added some python code in the frontmatter of the component. We define a `post` function that tells hyperflask that this component can receive POST requests.

The function then returns the properties that will be used to render the component.

Let's add a form to our chat interface. Replace `app/pages/index.jpy` with the following:

```
{% use_layout %}
<div id="messages">
    {# messages will display here #}
</div>
<{HxForm action=url_for("ChatMessage") hx_target="#messages" hx_swap="beforeend"}>
    <{TextareaField name="message" placeholder="Chat" }/>
    <{SubmitButton}>Send</{}>
</{HxForm}>
```

We are using [htmx](https://htmx.org/) to submit our form using AJAX. Using `hx-target` and `hx-swap` we are telling htmx to put the returned content from our component call at the end of the messages div.

Try it now and chat with yourself!

## Making it persistent

Now let's ensure that our chat is persisted and that reloading the page does not clear the chat history.

Hyperflask uses [sqlorm](https://hyperflask.github.io/sqlorm/) as its ORM.

Create your first model. In `app/models.py`, add the following:

```py
from hyperflask.factory import db
import datetime

class Message(db.Model):
    message: str
    timestamp: datetime.datetime = db.Column(default=datetime.datetime.utcnow)
```

Modify our component to save messages:

```
---
from hyperflask import request
from app.models import db, Message

def post():
    with db:
        msg = Message.create(message=request.form["message"])
    return {"message": msg}
---
<{ChatBubble}>
    {{props.message.message|markdown}}
</{ChatBubble}>
```

And finally the page:

```
---
from app.models import Message

page.messages = Message.find_all()
---
{% use_layout %}
<div id="messages">
    {% for msg in messages %}
        <{ChatMessage message=msg }/>
    {% endfor %}
</div>
<{HxForm action=url_for("ChatMessage") hx_target="#messages" hx_swap="beforeend"}>
    <{TextareaField name="message" placeholder="Chat" }/>
    <{SubmitButton}>Send</{}>
</{HxForm}>
```

## Adding real-time chat

Up until now, you could only chat with yourself. We will now refactor our app to become real-time using Server-Sent-Events (SSE).

Rather than sending back a message partial when posting a new message, we will use a dedicated send endpoint that will publish an event containing the message partial.

Modify the `ChatMessage` component back to its simpler state:

```
<{ChatBubble}>
    {{props.message.message|markdown}}
</{ChatBubble}>
```

Now let's create a new component `PostMessageForm` in `app/components/PostMessageForm.jpy` that will handle sending messages.

We will also use the a [form](/guides/forms) in this component to easily validate data.

```
---
from hyperflask import page, current_app
from app.models import db, Message

def post():
    form = page.form()
    if form.validate():
        with db:
            msg = Message.create(**form.data)
        current_app.sse.publish("messages", current_app.components.ChatMessage(message=msg), private=True)
---
{% form %}
<{HxForm form action=url_for("PostMessageForm") hx_swap="none"}>
    <{FormField form.message.textarea(required=True, placeholder="Chat") }/>
    <{SubmitButton}>Send</{}>
</{HxForm}>
```

Let's modify `app/pages/index.jpy` to use our new component and connect to the SSE stream:

```
---
from app.models import Message

page.messages = Message.find_all()
---
{% use_layout %}
<{MercureStream topic="messages"}>
    {% for msg in messages %}
        <{ChatMessage message=msg }/>
    {% endfor %}
</{MercureStream}>
<{PostMessageForm}/>
```

!!! info
    The MercureStream component uses the [htmx SSE extension](https://htmx.org/extensions/sse/) to connect to the sse stream

## Adding authentication

First, let's install the [hyperflask-users](https://github.com/hyperflask/hyperflask-users) extension. In a VS Code terminal (while connected to the dev container), execute `uv add hyperflask-users`.

As we will not deal with [database migrations](/guides/models) during this tutorial, delete your existing database: `rm databases/app.db`.

!!! info
    Hyperflask-Users provices login and signup pages as well as everything you need for a professional authentication flow and user management.

Let's create a user model and change our existing model to be bound to users:


```py
from hyperflask.factory import db
from hyperflask_users import UserMixin, UserRelatedMixin
import datetime

class User(UserMixin, db.Model):
    pass

class Message(UserRelatedMixin, db.Model):
    message: str
    timestamp: datetime.datetime = db.Column(default=datetime.datetime.utcnow)
```

Modify the component `ChatMessage` to display the author:

```
<{ChatBubble header=props.message.user.email}>
    {{props.message.message|markdown}}
</{ChatBubble}>
```

Finally, add `page.login_required()` at the top of your page frontmatter to require authentication to access it.

Upon accessing your site, you will be asked to connect using an email address. No confirmation will be asked on first connection. On further connections, you will be asked for a code to complete the connection. Go to <http://localhost:8025> to access [Mailpit](https://github.com/axllent/mailpit) and read the emails.

## Deploying to production

Signup for an account on Fly.io or any VPS provider (eg: Digital Ocean) then run the following command from a VS Code terminal (while connected to the dev container):

    uv run hyperflask deploy

Some information will be requested then the deployment will happen automatically. Connect to your domain and voilà!

## Going further

Checkout the [Github repository](https://github.com/hyperflask/getting-started) with the result of this tutorial and more. It also includes a nice UI, chat rooms, etc...