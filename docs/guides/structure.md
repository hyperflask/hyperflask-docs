# Project structure

!!! info
    This guide assumes you have created your app using Hyperflask-Start

In your project folder, you will find the following files and folders:

 - **app**: your app code
    - **assets**: scripts and stylesheets that will be bundled using [esbuild](https://esbuild.github.io/)
        - **main.css**: tailwind entrypoint
    - **components**: components to compose your app
    - **pages**: your site pages
 - **public**: all files in this folder are publicly accessible
 - **tests**: tests using [pytest](https://pytest.org)
 - **.env**: environment variables
 - **config.yml**: your app configuration file
 - **Dockerfile**: Dockerfile to build your production image
 - **pyproject.toml**: list python dependencies and tool options
 - **package.json**: list javascript dependencies

When using the `hyperflask` command, an Hyperflask app instance will be automatically created from the *app* folder.

!!! info
    If you are coming from Flask, this means you do not create the `app` object yourself.

The actuall application object is available at `hyperflask.factory:app` (or `hyperflask:current_app` when in [app context](https://flask.palletsprojects.com/en/stable/appcontext/)).

The *app* folder is available as a python module and the following packages will be automatically imported from it if they exist:

 - *models* : to define your database models
 - *routes* : to define app routed endpoints
 - *tasks*: to define background tasks using dramatiq
 - *cron*: to define scheduled tasks using dramatiq
 - *cli*: to define command line tasks

To import things from these modules from the rest of your app:

```py
# app/models.py
from hyperflask.factory import db

class MyModel(db.Model):
    pass
```

```py
# anywhere else
from app.models import MyModel
```

## Manually creating the app

An app will be automatically created only if no application can be automatically discovered following the [Flask mechanism](https://flask.palletsprojects.com/en/stable/cli/#application-discovery).

To manually create an app, create an `__init__.py` file in the *app* folder with the following code:

```py
from hyperflask import Hyperflask

app = Hyperflask(__name__)
```

When doing so, no automatic configuration or imports are performed.