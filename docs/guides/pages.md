# Pages

Easily create static and dynamic pages with a layout.

!!! info
    This feature is provided by [Flask-File-Routes](https://github.com/hyperflask/flask-file-routes)

## Dynamic pages

Dynamic pages can use the following formats:

- **jpy**: jinjapy hybrid format that let you execute code before rendering the template
- **py**: python code only

A jinjapy file contains 2 sections:

- Some Python code enclosed by lines containg 3 dashes "---"
- A body containing some Jinja template code

Both are optional:

- If the python code is missing, the file only contains a Jinja template
- If the python code is left unclosed (the file starts with "---" on a single line followed by some python code), the file has no template

The python code has a few global variables injected when executed: `page`, `request`, `abort`, `redirect`, `url_for`, `current_app`, `render_template`.

## Content pages

No python code will be executed on content pages.

Content pages can use the following formats:

- **html**: a standard jinja template
- **md**: a standard jinja template that will be rendered using markdown

All formats can have a YAML frontmatter defining variables that will be injected in the page object.

## How routing works

The URL rule is constructed using the following rules:

- `index.ext` file are roots
- folder hierarchy are transformed to url paths:
    - `posts/release-annoucement.ext` converts to `/posts/release-annoucement`
    - `posts/index.ext` converts to `/posts`
    - `folder/subfolder/page.ext` converts to `/folder/subfolder/page`
- placeholders are allowed in filenames:
    - `posts/<slug>.ext` converts to `/posts/<slug>`

The placeholder value is available through the [`page` object](#the-page-object) (eg: `page.slug`).

## The page template

Templates are powered by [Jinja](https://jinja.palletsprojects.com/en/stable/).

We recommend reading the [Flask templating guide](https://flask.palletsprojects.com/en/stable/templating/).

Hyperflask includes built-ins UI components powered by [DaisyUI](https://daisyui.com/). Check out the [Components](/guides/components/#built-in-ui-components) guide.

## Layouts

Hyperflask makes managing layouts for your pages easier. Layouts are saved in the *app/layouts* folder. The default layout can be overriden at *app/layouts/default.html*.
(Hyperflask provides a default layout when none is created)

For a page to use a layout, include the `{% use_layout %}` at the top of the template. Layouts can provide multiple placeholders to fill in named "blocks". Content outside of blocks will be added to the default block named "content".

Example template:

```html
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