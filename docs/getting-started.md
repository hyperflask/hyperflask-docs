---
hide: [navigation]
---
# Getting started

Welcome to Hyperflask! In this getting started guide will create a simple chat app with authentication.

We will use [Hyperflask-Start](https://github.com/hyperflask/hyperflask-start) to create our project and VS Code as editor (as the starter template deeply integrates with it).

What you will need:

- [Docker](https://www.docker.com/)
- [VS Code](https://code.visualstudio.com/)

If you are on Windows, use [WSL](https://learn.microsoft.com/en-us/windows/wsl/install).

Python is not needed on your machine, everything will be executed inside containers.

## Installation

Launch the following command to create your project:

    curl -L https://raw.githubusercontent.com/hyperflask/hyperflask-start/start.sh | bash

This will prompt you for some options and create the project in a new folder.

Open your project folder in VS Code. It should prompt you to "re-open workspace in development container" which you should accept. VS Code will create and start the development container and re-launch itself.

You are now developping from the container inside which you will find Python 3.11, Node & npm and hyperflask installed.

## Running your app

In VS Code, press F5 or "Start debugging" in the command palette.

The browser will automatically open to your new site!

## First look at the code base

In your project folder, you will find the following files and folders:

 - **app**: your app code
    - **assets**: scripts and stylesheets that will be bundled using [esbuild](https://esbuild.github.io/)
    - **components**: components to compose your app
    - **pages**: your site pages
 - **public**: all files in this folder are publicly accessible
 - **tests**: tests using [pytest](https://pytest.org)
 - **Dockerfile**: Dockerfile to build your production image
 - **pyproject.toml**: list python dependencies and tool options
 - **package.json**: list javascript dependencies
 - **tailwind.config.js**: tailwind configuration

## Starting our chat app

First, let's add a `ChatMessage` component to render one message. In `app/components/ChatMessage.jpy`:

```
<div class="message">
    {{props.message|markdown}}
</div>
```

The [component]() is made of a [jinja template](https://jinja.palletsprojects.com/). It receives a `props` variable that contains all the properties passed to the component.

!!! info
    Note the `jpy` file extension which references a new file format named [jinjapy](https://github.com/hyperflask/jinjapy)

Let's use this component, to render a thread. Replace the content of `app/pages/index.jpy` with the following:

```
{% use_layout %}
<div id="messages">
    <{ChatMessage message="First message!" }/>
    <{ChatMessage message="Second message!" }/>
</div>
```

Here you can see that we are using a [special syntax](https://github.com/hyperflask/flask-super-macros?tab=readme-ov-file#usage) to call our component and pass it some props.

Now we want to be able to send messages. We will add the ability to render messages through an HTTP call. Replace `app/components/ChatMessage.jpy` with the following:

```
---
from hyperflask import request

def post():
    return {"message": request.form["message"]}
---
<div class="message">
    {{props.message|markdown}}
</div>
```

We have added some python code in the [frontmatter]() of the component. We define a `post` function that tells hyperflask that this component can receive POST requests.

The function then returns the properties that will be used to render the component.

Let's add a form to our chat interface. Replace `app/pages/index.jpy` with the following:

```
{% use_layout %}
<div id="messages">
    {# messages will display here #}
</div>
<{HxForm hx_post=url_for("ChatMessage") hx_target="#messages" hx_swap="beforeend"}>
    <{TextareaField name="message" placeholder="Chat" }/>
    <{SubmitBtn}>Send</{}>
</{HxForm}>
```

We are using [built-in hyperflask components]() to create our form and [htmx](https://htmx.org/) to submit our form using AJAX.

Using `hx-target` and `hx-swap` we are telling htmx to put the returned content from our component call at the end of the messages div.

Try it now and chat with yourself!

## Making it persistent

Now let's ensure that our chat is persisted and that reloading the page does not clear the chat history.

Hyperflask uses [sqlorm](https://hyperflask.github.io/sqlorm/) as its ORM.

Create your first model. In `app/models.py`, add the following:

```py
from hyperflask import db
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
<div class="message">
    {{props.message.message|markdown}}
</div>
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
<{HxForm hx_post=url_for("ChatMessage") hx_target="#messages" hx_swap="beforeend"}>
    <{TextareaField name="message" placeholder="Chat" }/>
    <{SubmitBtn}>Send</{}>
</{HxForm}>
```

## Adding real-time chat

Up until now, you could only chat with yourself. We will now refactor our app to become real-time.

First, we will create a "resource" mapped to our `Message` model. Create `app/resources.py` with the following:

```py
from hyperflask.resources import Resource
from .models import Message

class MessageResource(Resource):
    model = Message
    url_prefix = "/messages"
    macro = "ChatMessage(message)"
```

Note that using the `macro` prop, we are telling hyperflask to render this resource using our `ChatMessage` component by passing the object as the `message` prop.

!!! info
    Why macro and not component ? Components are a layer above jinja macros. All defined components have a corresponding macro. But you can also [define pure jinja macros]().

Modify the component back to its simpler state as message creation will now be handled via the resource:

```
<div class="message">
    {{props.message.message|markdown}}
</div>
```

Finally, use the resource in the page:

```
---
from app.resources import MessageResource

page.messages = MessageResource.list()
---
{% use_layout %}
<div id="messages">
    {! messages !}
</div>
<{HxForm hx_post=messages.url() hx_swap="none"}>
    <{TextareaField name="message" placeholder="Chat" }/>
    <{SubmitBtn}>Send</{}>
</{HxForm}>
```

We are now using a [reactive directive]() to render our messages. Reactive directives use the resource system to add real-time reactivity to your page.
In this case, this list of messages will be automatically updated as soon as we insert or delete messages.

Notice also that we have changed the form action to post to the resource rather than the component. We are also ignoring the return of this call.

!!! note
    Although it may feel like magic, reactive directives work in a well defined way:

      - resources are exposed through a REST API (docs available at <http://localhost:5000/api/docs>)
      - updates to resources are notified through an SSE stream
      - on the frontend, it listens to the stream and updates the list accordingly
    
    Reactive directives work with any resource objects, whether list of them or their properties. However, using a non-resource object will print the value as usual.

With a total of 27 lines of code, you now have a real-time and persisted chat room!

## Adding authentication

First, let's install the [hyperflask-auth]() extension. In a VS Code terminal (while connected to the dev container), execute `poetry add hyperflask-auth`.

As we will not deal with [database migrations]() during this tutorial, delete your existing database: `rm databases/app.db`.

!!! info
    Hyperflask-Auth provices login and signup pages as well as everything you need for a professional authentication flow.

Let's create a user model and change our existing model to be bound to users:


```py
from hyperflask import db
from hyperflask_auth import UserMixin, UserRelatedMixin
import datetime

class User(UserMixin, db.Model):
    pass

class Message(UserRelatedMixin, db.Model):
    message: str
    timestamp: datetime.datetime = db.Column(default=datetime.datetime.utcnow)
```

Modify the component to display the author:

```
<div class="message">
    <strong class="me-1">{{props.message.user.username}}</strong>
    {{props.message.message|markdown}}
</div>
```

Finally, add `page.login_required()` at the top of your page frontmatter to require authentication to access it.

## Deploying to production

Signup for an account on [AWS]() or [Digital Ocean]() (recommended), create a virtual machine, then run the following command from a VS Code terminal (while connected to the dev container):

    hyperflask deploy

Your host information will be requested then the deployment will happen automatically. Connect to your domain and voilà!