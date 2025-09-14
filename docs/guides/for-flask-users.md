# For Flask users

Hyperflask is a framework built on top of [Flask](https://flask.palletsprojects.com/) combining multiple extensions into a unique experience.

Instead of creating an instance of `Flask` for your app, you create an instances of `Hyperflask`. See [the project's homepage](https://github.com/hyperflask/hyperflask#flask-extensions) for a list of all extensions used by Hyperflask. A lot of them are developed as part of the Hyperflask organization.

The `flask` module can be replaced by `hyperflask` for all your Flask related imports.

The `hyperflask` command should be used instead of `flask` to run and manage your app.

```py
# app.py
from hyperflask import Hyperflask, request

app = Hyperflask(__name__)

@app.route('/')
def index():
    return render_template_string("hello {{name}}", name=request.args.get('name', 'world'))
```
```
$ hyperflask dev
```