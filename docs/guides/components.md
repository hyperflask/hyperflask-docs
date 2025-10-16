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