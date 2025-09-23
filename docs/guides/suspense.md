# Loading data

There are 2 ways to load data while displaying a loader to the user.

## Using suspense

!!! info
    This feature is provided by [Flask-Suspense](https://github.com/hyperflask/flask-suspense)

Suspense uses response streaming to delay the rendering of parts of the template to the end, allowing you to display loading states as part of a single request. This makes it the most efficient solution.

Let's create a component to render a big data table, in `components/DataTable.jpy`:

```
---
def render():
    return {"data": MyModel.find_all()}
---
<table>
    {% for row in data %}
        <tr>
            ...
        </tr>
    {% endfor %}
</table>
```

As you can see, this component fetches data when it is being rendered. If we were using this component directly, the page render would pause while the data is fetched. The user would have no feedback on what is hapenning.

To prevent this issue, and display a loader, we can wrap the call to this component using a `{% suspense %}` block:

```jinja
{% suspense %}
    <{DataTable}/>
{% fallback %}
    <p>Loading...</p>
{% endsuspense %}
```

Now the page will display immediatly with a loading message. Once the datatable is finished rendering, it will appear instead of the loading message.

This method is also useful when performing API calls.

!!! tip
    You can also use suspense blocks without using components. Use the `defer()` function as [explained in Flask-Suspense doc](https://github.com/hyperflask/flask-suspense).

!!! warning
    Suspense can be used with htmx requests but htmx does not support streaming responses out of the box.
    Add `hx-stream` to elements fetching streaming data to handle it properly.

## Using htmx

Using component endpoints, you can fetch a component on page load.

Let's make the component from the previous section accessible via GET:

```
---
def get():
    pass
def render():
    return {"data": MyModel.find_all()}
---
<table>
    {% for row in data %}
        <tr>
            ...
        </tr>
    {% endfor %}
</table>
```

Then use htmx to fetch the component on load:

```jinja
<div hx-get="{{url_for('DataTable')}}" hx-trigger="load" hx-swap="outerHTML">
    Loading...
</div>
```