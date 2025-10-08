# Static content

Hyperflask makes it easy to build pages out of static content !

## Content pages

No python code will be executed on content pages.

Content pages can use the following formats:

- **html**: a standard jinja template
- **md**: a standard jinja template that will be rendered using markdown

All formats can have a YAML frontmatter defining variables that will be injected in the page object.

Use the `layout` property in the frontmatter to use a layout for the page. This uses Jinja extends sustem. The default block name will be `content`. You can provide an alternative block name after the template name separated by a colon.

```md
---
layout: layouts/default.html:body
---
# Hello world
```

## Collections

Collections are a way to manage a collection of static pages generated from a content source.

!!! info
    This feature is provided by [Flask-Collections](https://github.com/hyperflask/flask-collections)

Your app can have multiple collections. Each collection has a set of entries.

Each entry has a "slug", some content and a set of properties. Formats for each entries varies depending on the collection type.

When the `is_markdown` property is set to true (which is automatic if a file-based entry has the *.md* extension), the content is rendered as markdown.

When using a filename, it can contain a date prefix in the form of YYYY-MM-DD. The date will be available as the `date` property.

### File-backed collections

In a directory named after the collection located in *app/collections*, use one file per entry.

Example:

```
app/collections
  blog/
    2025-01-01-new-year.md
    2025-02-01-second-month.md
```

Example *2025-01-01-new-year.md*:

```
---
title: "Happy new year!"
---
Hello world
```

### Data-backed collections

These are collections where entries are all stored in a single structed file like CSV, JSON or YAML.

Example *app/collections/blog.csv*:

```
slug,date,title,content
new-year,2025-01-01,"Happy new year!","Hello world"
```

An sqlite database can also be used using the *.db* extension. A table or query must be provided a config.

### Configuring collections

Collections can be configured under the `COLLECTIONS` key. Create a subkey named after the collection that contains a dict of options.

By default, collections are bound to a url under a path named after the collection. This can be overriden using the `url` config key.  
You can also provide a layout template for collection entries. This template will receive an `entry` and `content` variable.

```
collections:
    blog:
        url: /blog
        layout: layouts/post.html
    categories:
        path: meta.db
        table: categories
```

To prevent a collection from being exposed via a URL, set url to false.

### Accessing collections programmatically

Collections are accessible under `app.collections`.

```py
for post in app.collections.blog:
    print((post.slug, post.title, post.url))
```

## Content strategies

!!! info
    This feature uses [Frozen-Flask](https://frozen-flask.readthedocs.io/en/latest/)

### Dynamic (default)

Static site generation is disabled. All routes will be served by the Flask app.

### Hybrid

Static site generation is enabled. GET routes will be statically generated. 

When in production, URLs will be first matched against static files and fallback to the Flask app otherwise.

To activate, add `static_mode: hybrid` in `config.yml`.

### 100% static site

Build your website locally and upload the statically generated site to a static hosting provider.

Check out the [deployment guide](/guides/deploy#static-site-generation)

To activate, add `static_mode: static` in `config.yml`.