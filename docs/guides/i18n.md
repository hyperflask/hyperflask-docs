# Internationalization

!!! info
    This feature is provided by [Flask-Babel-Hyper](https://github.com/hyperflask/flask-babel-hyper)

## Marking strings for translation

Use [gettext functions](https://docs.python.org/3/library/gettext.html#module-gettext) to mark all strings requiring translation.

In templates:

```jinja
{{_("this string will be translated")}}
```

In python:

```py
from hyperflask import _

_("this string will be translated")
```

Other available functions:

|Full name|Short name|Description|
|---|---|---|
|gettext|_|Return a localized string|
|ngettext|_n|Like gettext(), but consider plural forms|
|pgettext|_p|Like gettext(), but specify the context|
|lazy_gettext|_lazy|Like gettext(), but evaluation is delayed|

!!! tip
    Format strings should be resolved after the translation has happenned.

    Bad: `_("hello %(name)s" % {"name": "world"})`

    Good: `_("hello %(name)s") % {"name": "world"}`

## Creating a translation

Run the following command:

```
$ hyperflask babel init LOCALE
```

Where LOCALE should be a locale code (eg: `fr`)

Translate the generated po file in *app/translations/{LOCALE}/LC_MESSAGES* using a tool like [poedit](https://poedit.net/).

Once all the translations have been completed, run the following command:

```
$ hyperflask babel compile
```

## Locale detection

Locale is automatically selected from, in order:

 - the `locale` query string parameter
 - the browser's Accept-Language header
 - the default locale

When the locale is set via the query string parameter, it is stored in the session until further change.

## Updating translations

Run the following command:

```
$ hyperflask babel update
```

Add missing translations in po files then run the following command:

```
$ hyperflask babel compile
```