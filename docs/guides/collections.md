# Collections

Collections are a way to manage a collection of static pages generated from a content source.

!!! info
    This feature is provided by [Flask-Collections](https://github.com/hyperflask/flask-collections)

Your app can have multiple collections. Each collection has a set of entries.

Each entry has a "slug", some content and a set of properties. Formats for each entries varies depending on the collection type.

When the `is_markdown` property is set to true (which is automatic if a file-based entry has the *.md* extension), the content is rendered as markdown.

When using a filename, it can contain a date prefix in the form of YYYY-MM-DD. The date will be available as the `date` property.

## File-backed collections

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

## Data-backed collections

These are collections where entries are all stored in a single structed file like CSV, JSON or YAML.

Example *app/collections/blog.csv*:

```
slug,date,title,content
new-year,2025-01-01,"Happy new year!","Hello world"
```

An sqlite database can also be used using the *.db* extension. A table or query must be provided a config.

## Configuring collections

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

## Accessing collections programmatically

Collections are accessible under `app.collections`.

```py
for post in app.collections.blog:
    print((post.slug, post.title, post.url))
```