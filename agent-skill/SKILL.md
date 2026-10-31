---
name: hyperflask
description: Build web apps with Hyperflask, a batteries-included Flask framework for component-driven, HTMX-based apps. Use when creating or modifying a Hyperflask app - file-based pages (.jpy), components, SQLORM models, forms, built-in DaisyUI components, htmx interactivity, assets, static content, emails, background tasks, server push, i18n, users and auth, deployment.
---

# Hyperflask

Hyperflask is a batteries-included framework built on Flask. It is optimized for containerized, component-driven, HTMX-based web apps with SQLORM, Tailwind, DaisyUI, asset bundling, static generation, background tasks, server push, forms and user management.

The `references/` folder contains the full Hyperflask documentation. Before implementing a feature, read the matching reference listed at the end of this file. Prefer the features provided by the framework over re-implementing them.

## Essentials

### Project structure

- The app lives in the `app/` folder. Do not create the Flask `app` object: it is created automatically and available as `hyperflask.factory:app` (`from hyperflask.factory import app, db`).
- `app/models`, `app/routes`, `app/tasks`, `app/cron` and `app/cli` (modules or packages) are imported automatically if they exist.
- Pages go in `app/pages`, components in `app/components`, layouts in `app/layouts`, assets to bundle in `app/assets`, public files in `public/`.
- Configuration lives in `config.yml` and environment variables in `.env`.

### Pages

Pages are `.jpy` files (python code between two `---` lines followed by a Jinja template) in `app/pages`. Routes follow the file hierarchy: `index.jpy` is the folder root, `posts/<slug>.jpy` maps to `/posts/<slug>`, `(folder)` is omitted from the URL.

Example `app/pages/posts/<id>.jpy`:

```jpy
---
from app.models import Post

page.post = Post.get_or_404(page.id)
---
{% use_layout %}
<h1>{{ post.title }}</h1>
```

- Properties set on the `page` object become template variables. URL placeholders are available as `page.<name>`.
- `page`, `request`, `session`, `abort`, `redirect`, `url_for`, `current_app` and `render_template` are available without import in pages.
- Functions named after HTTP methods (`get`, `post`, `put`, `patch`, `delete`) run after the main body for the matching method. Without them, the page only answers GET.
- Include `{% use_layout %}` at the top of the template unless no layout is needed.
- Endpoint names are derived from the path: `posts/index.jpy` is `posts`, `posts/<slug>.jpy` is `posts_<slug>`.

### Components

Components are files in `app/components` named after the component. Call them with the macro tag syntax:

```jinja
<{Card title="Hello" }/>
<{Card title=(post.title) }>{{ post.body }}</{Card}>
```

- `.html` components receive `props` and render their children with `{{ children() }}`.
- `.jpy` components can define `render(**props)` returning template variables, and HTTP method functions (`get`, `post`, ...) that register the component as a route. Use htmx to call them (`url_for('ComponentName')`) and swap only the needed HTML.
- Unlike pages, all python imports are mandatory in components.
- `.js`/`.ts` files define Web Components and `.jsx`/`.tsx` files define React components.
- Use the built-in DaisyUI components (`Button`, `Card`, `Modal`, `Form`, `FormField`, ...) as much as possible.

### Interactivity

- Hyperflask uses htmx 4: attributes are not inherited by default (use the `:inherited` modifier), extensions do not need `hx-ext` and event names use colons (`htmx:after:request`).
- Use Alpine.js for pure frontend interactions inside components.
- Use server push for realtime updates and htmx out-of-band swaps to update several parts of the page from a single request.

### Data

- Models use SQLORM: classes inheriting from `hyperflask.models.Model` with a `table` property and annotated columns. Wrap writes in `with transaction():` (`from hyperflask import transaction`).
- Forms are declared directly in templates (`form.email.email("Email", required=True)`) and validated in the page with `page.form().validate()`.

## References
