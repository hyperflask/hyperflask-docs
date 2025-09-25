# Files

Manage user uploaded files.

!!! info
    This feature is provided by [Flask-Files](https://github.com/hyperflask/flask-files)

## Upload files to store in models

Add a file column to your model:

```py
from hyperflask.factory import db

class MyModel(db.Model):
    file = Column(type=db.File)
```

In a page using a form:

```jpy
---
form = page.form()
def post():
    if form.validate():
        with db:
            obj = MyModel.create(**form.data)
---
<{Form}>
    <{FormField form.file.file("File") }/>
    <{SubmitButton}>Upload</{}>
</{Form}>
```

Or without forms:

```py
MyModel.create(file=request.files['file'])
```

When accessing the model property, the value is a [file object](https://github.com/hyperflask/flask-files#file-object).

To generate a url for the file:

```jpy
---
page.obj = MyModel.get(1)
---
<img src="{{obj.file}}">
```

## Using S3

To store files on S3 (or compatible services), configure your app as follow:

In *.env*:

```
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
AWS_DEFAULT_REGION=...
```

In *config.yml*:

```
files_default_filesystem: s3
files_base_path: bucket_name
```

## Uploading without models

Use `save_file()` to store a file and get a [file object](https://github.com/hyperflask/flask-files#file-object). File objects are serializable as string or JSON.

```jpy
---
from hyperflask import save_file

form = page.form()

def post():
    if form.validate():
        file = save_file(form.file.data)
        # do something with file object
---
<{Form}>
    <{FormField form.file.file("File") }/>
    <{SubmitButton}>Upload</{}>
</{Form}>
```