# Pages

Easily create static and dynamic pages with a layout.

!!! info
    This feature is provided by [Flask-File-Routes](https://github.com/hyperflask/flask-file-routes)

## Dynamic pages

Pages use the [jinjapy](https://github.com/hyperflask/jinjapy) file format. It combines python code and a [jinja template](#the-page-template). The python code will be executed first on every request, then the template will be rendered. The python code is enclosed inside 2 lines containing 3 dashes "---".

Create new pages in the `app/pages` folder using the `.jpy` extension.

A special [page object](#the-page-object) is available in the python code. Assign values to this object so that they become available in the template.

```jpy
---
page.message = "Hello world"
---
{{ message }}
```

Both the python code or the templates are optional:

- If the python code is missing, the file only contains a Jinja template
- If the python code is left unclosed (the file starts with "---" on a single line followed by some python code), the file has no template

The python code has a few global variables injected when executed: `page`, `request`, `abort`, `redirect`, `url_for`, `current_app`, `render_template`.

!!! tip
    Pages can also be declared using .py files. In this case they will be pure python modules. Use `page.respond()` to send a response.

## The page template

Templates are powered by [Jinja](https://jinja.palletsprojects.com/en/stable/).

We recommend reading the [Flask templating guide](https://flask.palletsprojects.com/en/stable/templating/).

Hyperflask includes built-ins UI components powered by [DaisyUI](https://daisyui.com/). Check out the [Components](/guides/components/#built-in-ui-components) guide.

## Content pages

See [static content](/guides/static#content-pages).

## How routing works

The URL rule is constructed using the following rules:

- `index.jpy` file are roots
- folder hierarchy are transformed to url paths:
    - `posts/release-annoucement.jpy` converts to `/posts/release-annoucement`
    - `posts/index.jpy` converts to `/posts`
    - `folder/subfolder/page.jpy` converts to `/folder/subfolder/page`
- placeholders are allowed in filenames:
    - `posts/<slug>.jpy` converts to `/posts/<slug>`
- surround a folder name with parentheses so that it does not appear in the url
    - `folder/(subfolder)/page.jpy` converts to `/folder/page`

The placeholder value is available through the [`page` object](#the-page-object) (eg: `page.slug`).

## Generating URLs

Use [Flask's `url_for()`](https://flask.palletsprojects.com/en/stable/api/#flask.url_for) function as usual.

Endpoint names follow the following rules:

- `page.jpy` => `page`
- `posts/release-annoucement.jpy` => `posts_release-announcement`
- `posts/index.jpy` => `posts`
- `folder/subfolder/page.jpy` => `folder_subfolder_page`
- `posts/<slug>.jpy` => `posts_<slug>`
- `folder/(subfolder)/page.jpy` => `folder_subfolder_page`

## Layouts

Hyperflask makes managing layouts for your pages easier. Layouts are saved in the *app/layouts* folder. The default layout can be overriden at *app/layouts/default.html*.
(Hyperflask provides a default layout when none is created)

For a page to use a layout, include the `{% use_layout %}` at the top of the template. Layouts can provide multiple placeholders to fill in named "blocks". Content outside of blocks will be added to the default block named "content".

Example template:

```jinja
{% use_layout %}

{% block page_title %}New title!{% endblock %}

My page content
```

`{% use_layout %}` can also be given a template filename as argument to extend from any other template.

!!! tip
    When providing your own layout, you can extend from [*layouts/base.html*](https://github.com/hyperflask/hyperflask/blob/main/hyperflask/layouts/web.html).

## The page object

The `page` object is accessible without import in any pages or can be imported from `hyperflask`.

Any properties set onto the object will be available as a variable in the template.

Some helper methods that immediatly stop the page execution and return a response:

 - return an http error code using `page.abort(http_code)`
 - redirect to another page using `page.redirect(url)`
 - send any [response object](https://flask.palletsprojects.com/en/stable/api/#response-objects) using `page.respond(response)`

URL placeholders are available as read-only properties of the page object.

Additional helpers can be registered on the page object:

```python
@app.page_helper
def method(page):
    return request.method

page.method
```

!!! info
    The page object is accessible under `hyperflask.page` or `g.page` in **all** routes of your app.

    ```python
    from hyperflask import page

    @app.route("/")
    def index():
        page.message = "hello world"
        return render_template_string("{{message}}")
    ```

## Handling different HTTP methods

When using jpy or python files, you can create functions named after http methods in lower case (get, post, put, patch, delete). These functions will be executed after the main body of the python code depending on the request's http method.

Allowed http methods for a route depends on:

 - If no method function is present, the route will be available throught GET only
 - As soon as a method function is present, the route is available through the defined http methods.
 - Possible methods can be defined manually using a comment at the start of the python code listing allowed http methods in the following format: `# methods=GET,POST`

## The request object

A `request` object is available in your pages' python code. It can be used to access the request's data and metadata.

 - Use `request.args` to access query string parameters (`request.args['param-name']`)
 - Use `request.form` to access form data (`request.form['input-name']`)

See Flask [documentation about the request object](https://flask.palletsprojects.com/en/stable/quickstart/#the-request-object) for more information.

## Function-based endpoints

Hyperflask also allows you to create endpoints using python functions like Flask does.

In `app/routes.py`:

```python
from hyperflask.factory import app

@app.route('/my-endpoint')
def my_endpoint():
    return "hello"
```

Templates can also be used. They should be located in the `app/templates` folder.