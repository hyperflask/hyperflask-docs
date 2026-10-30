# Interactive apps

Hyperflask can be used to create interactive apps thanks to HTMX.

## HTMX introduction

HTMX has [comprehensive documentation](https://four.htmx.org/docs) but this section will cover the essential.

!!! info
    Hyperflask uses htmx 4. If you are used to htmx 2, read [what's new in htmx 4](https://four.htmx.org/docs/whats-new-in-htmx-4). Notably:

    - Attributes are not inherited by default: use the `:inherited` modifier (eg. `<div hx-target:inherited="#output">`)
    - Extensions are active as soon as they are loaded, `hx-ext` is not needed anymore
    - Event names use colons (eg. `htmx:after:request` instead of `htmx:afterRequest`)

    Hyperflask configures htmx to not swap error responses (4xx and 5xx) like htmx 2 did. Out of band swaps (like flash messages) are still processed. Use the `HTMX_CONFIG` [configuration](/guides/config) to change htmx options.

HTMX allows you to access AJAX, WebSockets and Server-Sent Events directly in HTML attributes. Instead of writing JavaScript to make requests, you can use attributes like `hx-get`, `hx-post`, and `hx-swap` to specify what should happen.

### Basic example

```html
<button hx-get="/api/message" hx-target="#result">
    Load message
</button>
<div id="result"></div>
```

When clicked, this button makes a GET request to `/api/message` and replaces the content of `#result` with the response.

### Core concepts

- **hx-get/post/put/delete**: Specify the HTTP method and URL
- **hx-target**: Select which element receives the response (uses CSS selectors)
- **hx-swap**: Define how to insert the response (`innerHTML`, `outerHTML`, `beforeend`, etc.)
- **hx-trigger**: Control what event triggers the request (defaults to `click` for buttons)

### Example with form submission

```html
<form hx-post="/todos" hx-target="#todos" hx-swap="beforeend">
    <input type="text" name="title" required>
    <button type="submit">Add Todo</button>
</form>
<div id="todos"></div>
```

Instead of a full page reload, HTMX sends the form data via AJAX and appends the response to `#todos`.

### Response handling

Your backend returns only the HTML fragment needed, not the entire page. This makes interactions faster and reduces bandwidth.

## Interactive components

Components can define their own custom backend logic. Similar to pages, files should use the *jpy* extension and provide a frontmatter with the python code.

Functions named after HTTP methods will be registered as routes. For example, if a *get* function exists, Hyperflask will make the component accessible through GET requests.  
These functions can return a dict with component props to render the component or any other valid Flask response value.

Use HTMX to call your component logic and retrieve only the necessery HTML.

Let's create a todo app:

*app/pages/index.jpy*:

```jpy
---
from app.models import Todo
page.todos = Todo.find_all()
---
<table>
    {% for todo in todos %}
        <{TodoItem todo=todo }/>
    {% endfor %}
</table>
<{button hx-get=url_for('TodoItemForm') hx-target="previous" hx-swap="beforeend"}>Add todo</{button}>
```

*app/components/TodoItem.jpy*:

```jpy
---
from hyperflask import request, transaction
from app.models import dbTodo

def get():
    todo = Todo.get_or_404(request.args['id'])
    return {"todo": todo}

def delete():
    with transaction():
        todo = Todo.get_or_404(request.args['id'])
        todo.delete()
    return ""
---
<tr>
    <td>{{props.todo.title}}</td>
    <td>
        <{button hx-get=url_for('TodoItemForm', id=props.todo.id) hx-target="closest tr" hx-swap="outerHTML"}>Edit</{button}>
        <{button hx-delete=url_for('TodoItem', id=props.todo.id) hx-target="closest tr" hx-swap="delete"}>Delete</{button}>
    </td>
</tr>
```

*app/components/TodoItemForm.jpy*:

```jpy
---
from hyperflask import request, current_app, transaction
from app.models import Todo

def get():
    todo = Todo.get_or_404(request.args['id']) if "id" in request.args else None
    return {"todo": todo}

def post():
    with transaction():
        if "id" in request.values:
            todo = Todo.get_or_404(request.args['id'])
        else:
            todo = Todo()
        todo.title = request.form["title"]
        todo.save()
    return current_app.components.TodoItem(todo=todo) # return another component
---
<tr>
    <td>
        <input type="text" name="title" value="{{props.todo.title if props.todo else ''}}" required>
    </td>
    <td>
        <{button hx-get=url_for('TodoItemForm', id=props.todo.id if props.todo else None) hx-include="closest tr" hx-target="closest tr" hx-swap="outerHTML"}>Save</{button}>
    </td>
</tr>
```

!!! warning
    Unlike pages, all python imports are mandatory in components

!!! warning
    When using Alpine.js in components that will be loaded via htmx, Alpine may not be included automatically.
    To ensure it is included, use `current_app.assets.include('@hyperflask/alpine')` in your page python code.

!!! tip
    The `request` object in Hyperflask uses [htmx-Flask](https://github.com/sponsfreixes/htmx-flask) subclass that [provides easy access to htmx headers](https://github.com/sponsfreixes/htmx-flask?tab=readme-ov-file#usage).
    Note that htmx 4 does not send the `HX-Trigger`, `HX-Trigger-Name` and `HX-Prompt` headers anymore (use `request.headers.get("HX-Source")` instead of `request.htmx.trigger`) and that `HX-Target` now uses the `tag#id` format.

## Pure frontend interactions

For simple frontend interactions, we recommend using [Alpine.js](https://alpinejs.dev/) with html components.

Sometines, you need a truly interactive component. In this case you can use Web Components, React or any other frontend framework. [Creating frontend components](/guides/components/#pure-frontend-components) is fully integrated in Hyperflask component system.

## Highligting active URLs

Use the built-in `hx-active-url` htmx extension. Apply the attribute to anchor elements or their parents. Its value is a class name that will be applied to the anchor element when its url matches window.location.

The url is resolved in the following order: hx-push-url, hx-replace-url, href, hx-get.

```html
<nav hx-active-url="active">
    <a hx-get="/page1" hx-push-url="true">Page 1</a>
    <a href="/page2">Page 2</a>
</nav>
```

When a link is fetching a component, the url may not be the right one. Use `hx-href` to setup the href attribute properly and activate `hx-push-url`:

```html
<nav hx-active-url="active">
    <a hx-get={{url_for('Component')}} hx-href={{url_for('index', id=1)}}>Page 1</a>
</nav>
```

## Removing elements after a delay

Use the built-in `remove-me` htmx extension (a port of the [htmx 1 extension](https://v1.htmx.org/extensions/remove-me/)). The element is removed after the given delay:

```html
<div class="alert" remove-me="5s">Saved!</div>
```

## HTMX utilities

Perform an htmx redirection using `htmx_redirect()`:

```py
from hyperflask import htmx_redirect
def post():
    # ...
    return htmx_redirect("/")
```

Perform an Out-Of-Band (oob) swap using `htmx_oob()`:

```py
from hyperflask import htmx_oob
def post():
    # ...
    return htmx_oob(current_app.components.Sidebar()) # replaces the sidebar element with a new version of itself
```

You can also add out of band elements in your template using the `<{HtmxOob}>` component:

```
<{HtmxOob}><{Sidebar}/></{HtmxOob}>
```

## Realtime apps

Add realtime updates to your app using [push messages](/guides/push).