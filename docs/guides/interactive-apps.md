# Interactive apps

Hyperflask can be used to create interactive apps thanks to HTMX.

## HTMX introduction

HTMX has [comprehensive documentation](https://htmx.org/docs/) but this section will cover the essential.

TODO

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
<button hx-get="{{url_for('TodoItemForm')}}" hx-target="previous" hx-swap="beforeend">Add todo</button>
```

*app/components/TodoItem.jpy*:

```jpy
---
from app.models import db, Todo

def get():
    todo = Todo.get_or_404(request.args['id'])
    return {"todo": todo}

def delete():
    with db:
        todo = Todo.get_or_404(request.args['id'])
        todo.delete()
    return ""
---
<tr>
    <td>{{props.todo.title}}</td>
    <td>
        <button hx-get="{{url_for('TodoItemForm', id=props.todo.id)}}" hx-target="closest tr" hx-swap="outerHTML">Edit</button>
        <button hx-delete="{{url_for('TodoItem', id=props.todo.id)}}" hx-target="closest tr" hx-swap="delete">Delete</button>
    </td>
</tr>
```

*app/components/TodoItemForm.jpy*:

```jpy
---
from hyperflask import request, current_app
from app.models import db, Todo

def get():
    todo = Todo.get_or_404(request.args['id']) if "id" in request.args else None
    return {"todo": todo}

def post():
    with db:
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
        <button hx-get="{{url_for('TodoItemForm', id=props.todo.id if props.todo else None)}}" hx-include="closest tr" hx-target="closest tr" hx-swap="outerHTML">Save</button>
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