---
name: hyperflask-components
description: Create component-driven Hyperflask apps. Components can be backend-only, frontend-only, or both. Components can be used to build interactive apps.
---
# Components

Components are essentials pieces of Hyperflask apps. They can be interactive, are isolated and can apply to the frontend or backend.

!!! info
    This feature is in part provided by [Flask-Super-Macros](https://github.com/hyperflask/flask-super-macros)

## HTML components

HTML components are re-usable pieces of HTML. Define them in the *app/components* folder. The filename is the component name.
They are rendered on the backend.

Components can recieve parameters named *props*.

For example, to create a dropdown component, let's create the file *app/components/Dropdown.html*:

```jinja
<div class="dropdown">
    <button>{{props.label}}</button>
    <ul class="dropmenu">
        {% for item in props.items %}
            <li>{{item}}</li>
        {% endfor %}
    </ul>
</div>
```

Here, the component must be provided 2 parameters: label and items.

To call this component, we use a [special syntax](https://github.com/hyperflask/jinja-super-macros?tab=readme-ov-file#new-macro-tags-syntax) in our templates:

 - `<{ComponentName prop1=value prop2=value }/>` : to call a component without providing children
 - `<{ComponentName prop1=value }>...</{ComponentName}>` : to provide children

To use python expressions as prop values, surround them with parentheses: `<{Component prop1=(1+1) }/>`

Back to our example:

```
<{Dropdown label="Colors" items=["red", "blue"] }/>
```

Now, let's rework our component to use another component for the dropdown items.

```jinja
<div class="dropdown">
    <button>{{props.label}}</button>
    <ul class="dropmenu">
        {{children()}}
    </ul>
</div>
```

Now create *app/components/DropdownItem.html*:

```jinja
<li>
    <a href="{{prop.url}}">{{children()}}</a>
</li>
```

And finally, let's create a dropdown:

```jinja
<{Dropdown label="Countries"}>
    <{DropdownItem url=url_for('countries', code="fr")}>France</{DropdownItem}>
    <{DropdownItem url=url_for('countries', code="hk")}>Hong Kong</{DropdownItem}>
<{/Dropdown}>
```

!!! info
    Components are in fact jinja macros. Any jinja macro can be called using the new macro tag syntax.  
    [Read more about Flask Super Macros](https://github.com/hyperflask/flask-super-macros)

### Backend logic

HTML components can have their own custom backend logic. Read on to the [next guide about interactive apps](/guides/interactive-apps).

## Frontend interactions using Alpine.js

[Alpine.js](https://alpinejs.dev/) can be used to add interactivity to your component on the frontend. Alpine is bundled with Hyperflask and automatically loaded when used as part of a component.

Example using the previous *app/components/Dropdown.html*:

```jinja
<div class="dropdown" x-data="{ open: false }">
    <button @click="open = true">{{props.label}}</button>
    <ul class="dropmenu" x-show="open">
        {{children()}}
    </ul>
</div>
```

## Styling and scripting

Scripts and styles can be embedded in components and bundled automatically.

See [Embedded scripts and styles in the Assets guide](/guides/assets/#embedded-scripts-and-styles)

## Pure frontend components

Pure frontend components can be created using *.js* (or *.ts*) files for Web Components or *.jsx* (or *.tsx*) for React components.

!!! tip
    New adapters can be created for other frontend frameworks and component libraries.
    You can also force which adapter to use for one or multiple files.

### Web Components

In the case of Web Components, the js file should define the custom element and register it. The filename should be named after the component name (use underscores instead of dashes).

When the component is used as part of a template, the custom tag will be used and the file included in the page assets.

Example, *app/components/custom_dropdown.js*:

```js
class CustomDropdown extends HTMLElement {
    // ...
}

customElements.define('custom-dropdown', CustomDropdown);
```

In a template: `<{custom_dropdown}/>`

!!! tip
    [lit](https://lit.dev/) is a great library to implement Web Components. To use with Hyperflask, simply install it and use it as described in their documentation.

### React components

Define react components as usual in a jsx file named after the component. You must export your component as default. Call them in your template like any other component. Each component call will create an independant react tree.

!!! important
    React is not bundled with Hyperflask. You will need to install it using npm.

Properties provided to the component will be serialized to JSON. You cannot provide children.

Example, *app/components/Dropdown.jsx*:

```js
export default function Dropdown(props) {
    return <div></div>;
}
```

In a template: `<{Dropdown}/>`

## Built-in UI components

Hyperflask includes a rich library of UI components powered by [DaisyUI](https://daisyui.com).

Check out the [Components library](/components)

## Components with custom logic

For backend components, you can execute business logic before rendering the template.
Use a jinjapy file instead of html file (.jpy extension) and implement the render function.

The render function will be provided the props as arguments.

```jpy
---
def render(prop1, prop2):
    # custom logic
    return {"var": "value"} # template variables
---
{{var}}
```

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
<{button hx-get=url_for('TodoItemForm') hx-target="previous" hx-swap="beforeend"}>Add todo</{button}>
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
        <{button hx-get=url_for('TodoItemForm', id=props.todo.id) hx-target="closest tr" hx-swap="outerHTML"}>Edit</{button}>
        <{button hx-delete=url_for('TodoItem', id=props.todo.id) hx-target="closest tr" hx-swap="delete"}>Delete</{button}>
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