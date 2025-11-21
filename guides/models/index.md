# Models

Models are the way to persist data in a database. Hyperflask uses [SQLORM](https://hyperflask.github.io/sqlorm), an easy to use ORM that does not abstract away SQL. By default, Hyperflask apps are configured to use SQLite which has been tuned for great web app performance.

!!! info
    This feature is provided by [Flask-SQLORM](https://github.com/hyperflask/flask-sqlorm)

## Defining models

Models are classes inheriting from `Model`. To define which table they represent, use the `table` class property.

To define column mapping, define properties via annotations. The type used will be [converted to an sql type](https://hyperflask.github.io/sqlorm/models/#column-types).
For more control over the mapping, you can use instantiate `Column()` objects.

Example *app/models.py*:

```python
from hyperflask.factory import db

class Task(db.Model):
    table = "tasks"

    id: int
    title: str = db.Column(type="varchar(20)") # set the column type (used in create_table())
    done = db.Column("completed", bool, default=False) # no annotation, column name is "completed" but property name will be "done"
```

Once columns are defined via annotations or `db.Column` properties, they are accessible as class and instance properties.

[Read more in sqlorm documentation](https://hyperflask.github.io/sqlorm/models/)

## Persisting data

Manipulate model objects as you would with any python objects. The following methods help you execute DML statements:

- `save()` executes `insert()` or `update()` depending on the fact that the object has a primary key or not
- `insert()` executes an insert statement
- `update()` executes an update statement
- `delete()` executes a delete statement
- `refresh()` executes a select statement (same as `get()`) and updates the object attribute values
- `create()` a class method to create and insert an object in one line

These methods (apart from `create()`) return a boolean indicating if the operation was performed.

The data used to insert or update will be limited to "dirty" attributes, which means attributes that have been
modified since the last DML statement. Setting an attribute will automatically flag it as dirty.

To call this methods, you must be in a transaction context. Use the db object to initiate one.

```py
from app.models import db, Task

with db:
    task = Task.create(title="my task") # INSERT INTO tasks (title) VALUES ('my task')

    task = Task()
    task.title = "my task"
    task.save() # INSERT INTO tasks (title) VALUES ('my task')
    # same as task.insert()

    task = Task.get(1)
    task.title = "renamed task"
    task.save() # UPDATE tasks SET title = 'renamed task' WHERE id = 1
    # same as task.update()

    task = Task.get(2)
    task = Task.get_or_404(2) # raise a 404 error if object not found
    task.delete() # DELETE FROM tasks WHERE id = 2

    task = Task()
    task.id = 1
    task.refresh() # SELECT * FROM tasks WHERE id = 1
```

[Read more in sqlorm documentation](https://hyperflask.github.io/sqlorm/models/#manipulating-model-objects)

## Querying data

The following methods can be used to query data:

- `query()` executes the provided statement using [`fetchhydrated()`](https://hyperflask.github.io/sqlorm/executing/#fetching-composite-objects)
- `find_all()` constructs a select statement based on the provided arguments and executes using `query()`
- `find_one()` same as `find_all()` but only returns the first row
- `get()` to find one row by primary key

The two finder methods can take as argument a where condition (sql string) or keyword arguments representing attributes to filter by.

It is not needed to provide a transaction context to call these methods.

```python
todos = Task.query("SELECT * FROM tasks WHERE NOT done")
todos = Task.find_all("NOT done")
todos = Task.find_all(Task.done==False)
todos = Task.find_all(done=False)
task = Task.find_one("id=1")
task = Task.get(1)
```

[Read more in sqlorm documentation](https://hyperflask.github.io/sqlorm/models/#querying-model-objects)

## Rendering model objects

Model objects can be rendered using any jinja macro (components being macros). Set the `__macro__` class property to the name of the macro.

```py
class Task:
    __macro__ = "Task"
```

The macro will be provided an `obj` property. This can be overriden using the syntax `MacroName(property)`.

```py
class Task:
    __macro__ = "Task(task)"
```

In `app/components/Task.html`:

```html
<label>
    <input type="checkbox">
    {{props.task.title}}
</label>
```

Once defined, you can "print" your objects and result sets directly in your templates:

```jpy
---
page.tasks = Task.find_all()
---
{{tasks}}
```

```jpy
---
page.task = Task.get(1)
---
{{task}}
```

## Managing the schema

Hyperflask will automatically create missing tables on start. It will not however alter existing tables.

To manage your schema, you can use migrations as [described in the sqlorm documentation](https://hyperflask.github.io/sqlorm/schema/#migrations).

Initialize migrations using the following command: `uv run hyperflask db init-migrations --set-version`.
This will create a migration file at *data/migrations/000_initial.sql*.

Once migrations are activated, they will be auto applied on application start. This can be disabled using `init_database: false` in the config, in which case run your migrations using `uv run hyperflask db migrate`.

To create a new migration version for a new model use: `uv run hyperflask db init-migrations MyModel`

## Choosing a database

By default, Hyperflask uses [SQLite](https://sqlite.org) with [optimizations](https://fractaledmind.com/2023/09/07/enhancing-rails-sqlite-fine-tuning/) for usage in web applications.

If SQLite is not a good fit for your app, we recommend [PostgreSQL](https://www.postgresql.org/). In this case install the postgresql dbapi adapter using `uv add psycopg[binary]` then set the `sqlorm_uri` configuration parameter to the postgresql connection string.

## Going further

[Read sqlorm documentation](https://hyperflask.github.io/sqlorm/)