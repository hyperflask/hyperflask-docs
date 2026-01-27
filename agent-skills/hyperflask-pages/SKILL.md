---
name: hyperflask-pages
description: Create pages and routes in Hyperflask apps.
---
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
# Metadata

Hyperflask can manage a page metadata for you. This is necessary for SEO.

Set metadata by defining `page.metadata` to a dict. This only works on pages using the default layout.

```jpy
---
page.metadata = {
    "title": "Page title"
}
---
{% use_layout %}
My page
```

## Title

Set the `title` property on `page.metadata`.

You can use the `SITE_TITLE` configuration option to determine how your title looks like. `SITE_TITLE` can have different values:

 - If it's a string with no template markers, it will always be used as the page title (it overrides all others)
 - If it's a string with a template marker `%s`, the page title will be replaced. (eg: with `SITE_TITLE="%s | My site`, the page title would be "Page title | Site title")
 - It can be a dict with a `template` key and a `default` key. If no page title is provided, the default value is used, otherwise the template value is used.

Pages can override the title in all cases using a dict with an `absolute` key:

```py
page.metadata = {
    "title": {"absolute": "Page title"}
}
```

## Common metadata

You can set any other common metadata on the `page.metadata` dict. Depending on their name, some metadata will be included as `<link>` tags.

Values can be lists to generate multiple tags of the same name.

```py
page.metadata = {
    "description": "My awesome page",
    "keywords": ["awesome", "amazing"], # in the case of keywords, the list is joined
    "icon": asset_url("icon.png"),
    "author": ["John", "Peter"]
}
```

Will generate:

```html
<meta name="description" content="My awesome page">
<meta name="keywords" content="awesome,amazing">
<link rel="icon" href="/static/icon.png">
<meta name="author" content="John">
<meta name="author" content="Peter">
```

### Keywords

Keywords can be a list list, in which case the list is joined as comma separated values.

### Authors

```py
page.metadata = {
    "author": [
        "John",
        {"name": "Peter", "url": "/authors/peter"}
    ]
}
```

Will generate:

```html
<meta name="author" content="John">
<link rel="author" href="/authors/peter">
<meta name="author" content="Peter">
```

### Alternates

```py
page.metadata = {
    "alternate-lang": {
        "en-US": "/en",
        "fr-FR": "/fr"
    },
    "alternate-media": {
        "only screen and (max-width: 600px)": "/mobile"
    },
    "alternate-type": {
        "application/rss+xml": "/rss"
    }
}
```

Will generate:

```html
<link rel="alternate" hreflang="en-US" href="/en">
<link rel="alternate" hreflang="de-DE" href="/fr">
<link rel="alternate" media="only screen and (max-width: 600px)" href="/mobile">
<link rel="alternate" type="application/rss+xml" href="/rss">
```

### Robots

```py
page.metadata = {
    "robots": {
        "index": True,
        "follow": True,
        "nocache": False
    },
    "googlebot": {
        "index": True,
        "max-video-preview": -1
    }
}
```

Will generate:

```html
<meta name="robots" content="index, follow">
<meta name="googlebot" content="index, max-video-preview:-1">
```

## OpenGraph

```py
page.metadata = {
    "opengraph": {
        "title": "My article",
        "site_name": "My site",
        "image": {
            "url": asset_url("og.png", _external=True),
            "width": 800,
            "height": 600,
            "alt": "My image"
        }
    }
}
```

Will generate:

```html
<meta name="og:title" content="My article">
<meta name="og:site_name" content="My site">
<meta name="og:image" content="http://localhost:5000/static/og.png">
<meta name="og:image:width" content="800">
<meta name="og:image:height" content="600">
<meta name="og:image:alt" content="My image">
```

## Twitter

```py
page.metadata = {
    "twitter": {
        "creator": "@example",
        "image": asset_url("twitter.png", _external=True)
    }
}
```

Will generate:

```html
<meta name="twitter:creator" content="@hyperflask">
<meta name="twitter:image" content="http://...">
```

## JSON-LD

```py
page.metadata = {
    "json-ld": {
        "@context": "https://schema.org/",
        "@type": "Recipe",
        "name": "Banana Bread Recipe",
        "description": "The best banana bread recipe you'll ever find! Learn how to use up all those extra bananas.",
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": 4.7,
            "ratingCount": 123
        },
        "video": {
            "@type": "VideoObject",
            "name": "How To Make Banana Bread",
            "description": "This is how you make banana bread, in 5 easy steps.",
            "contentUrl": "https://www.example.com/video123.mp4"
        }
    }
}
```

Will generate:

```html
<script type="application/ld+json">
{
    "@context": "https://schema.org/",
    "@type": "Recipe",
    "name": "Banana Bread Recipe",
    "description": "The best banana bread recipe you'll ever find! Learn how to use up all those extra bananas.",
    "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": 4.7,
    "ratingCount": 123
    },
    "video": {
    "@type": "VideoObject",
    "name": "How To Make Banana Bread",
    "description": "This is how you make banana bread, in 5 easy steps.",
    "contentUrl": "https://www.example.com/video123.mp4"
    }
}
</script>
```

## Apple

```py
page.metadata = {
    "apple": {
        "itunes-app": "app-id=XXX",
        "web-app-capable": "yes"
        "touch-icon": asset_url("apply-icon.png", _external=True)
    }
}
```

Will generate:

```html
<meta name="apple-itunes-app" content="app-id=XXX">
<meta name="apple-web-app-capable" content="yes">
<link rel="apple-touch-icon" href="http://localhost:5000/static/apple-icon.png">
```

## Applinks

```py
page.metadata = {
    "applinks": {
        "ios": {
            "url": "http://...",
            "app_store_id": "XXX"
        },
        "android": {
            "package": "com.example...",
            "app_name": "XXX"
        }
    }
}
```

Will generate:

```html
<meta property="al:ios:url" content="https://...">
<meta property="al:ios:app_store_id" content="XXX">
<meta property="al:android:package" content="com.example....">
<meta property="al:android:app_name" content="XXX">
```

## Common metadata for all pages

Use the `SITE_METADATA` configuration option.

Example, in `config.yml`:

```yml
site_metadata:
    robots:
        index: false
```

The default configuration will be deeply merged with the page provided configuration.

## Generating metadata ouside of pages

Use `hyperflask.utils.metadata_tags()` to generate metadata tags according to the configuration object passed as first argument.