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