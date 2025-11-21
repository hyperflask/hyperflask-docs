---
date: 2025-11-11
authors:
  - maximebf
---
# Blending SQL and Python with SQLORM

At $dayjob, I use [SQLAlchemy](https://www.sqlalchemy.org/) as an ORM. It's an amazing project, powerful and flexible. However, I've always felt some of the design choices didn't fit how I like to use an ORM. Notably:

- I'm not a big fan of the [Unit of Work](https://martinfowler.com/eaaCatalog/unitOfWork.html) pattern and the fact that you do not control when DML queries are issued. I like queries to be executed as soon as they are called in code.
- I do not want my objects to be "attached" to a session or a specific database. I want to be able to fetch from one database and insert into another using the same object.
- I mostly want plain objects to map a table row.
- I want to write SQL by hand for complex queries. I do not want to use a query builder or DSL, I prefer writing actual SQL.
- I do not care about abstracting the database. I usually choose a database server when starting a project and optimize for it.
- Stay as close to DB-API as possible.

With these ideas in mind, [SQLORM](https://github.com/hyperflask/sqlorm) was born. (The name isn't great — I'm bad at finding names for projects like this.) It's inspired by many ORMs while bringing some unique features.

<!-- more -->

(As a side note, I know many other Python ORMs exist, but to me SQLAlchemy is the best. I don't like the API or codebase of the others.)

The main feature of SQLORM is that SQL is front and center. You can create SQL queries as standard Python functions, using the docblock to write the *templated* SQL statement:

```py
from sqlorm import sqlfunc

@sqlfunc
def tasks_completion_report(start_date, end_date):
    """SELECT done_at, COUNT(*) count
       FROM tasks
       WHERE done_at >= %(start_date)s AND done_at <= %(end_date)s
       GROUP BY done_at"""
```

In this example, `start_date` and `end_date` are parameters and will be properly escaped. Executing the function will run the SQL query in the active transaction.

[Connections](https://hyperflask.github.io/sqlorm/engine/) and [transactions](https://hyperflask.github.io/sqlorm/sessions-and-transactions/) are used via context managers. The `Engine` class manages DB-API connections.

```py
from sqlorm import Engine
import datetime

engine = Engine.from_uri("sqlite://app.db")

with engine:
    report = tasks_completion_report(datetime.date(2025, 1, 1), datetime.date.today())
```

SQLORM provides [many utilities](https://hyperflask.github.io/sqlorm/sql-utilities/) to help you build SQL statements, as well as [fetch related rows in a single query](https://hyperflask.github.io/sqlorm/executing/#composite-rows).

Rows are returned as dicts by default, but you can [hydrate objects instead](https://hyperflask.github.io/sqlorm/executing/#fetching-objects):

```py
class Task:
    pass

@sqlfunc(model=Task)
def find_tasks():
    "SELECT * FROM tasks"

with engine:
    tasks = find_tasks()
```

Now, we don't want to write endless simple statements to re-create basic CRUD functionality, so SQLORM provides a [`Model` class](https://hyperflask.github.io/sqlorm/models/). It follows the [Active Record pattern](https://en.wikipedia.org/wiki/Active_record_pattern).

```py
from sqlorm import Model

class Task(Model):
    pass

with engine:
    tasks = Task.find_all()

    task = Task.create(title="my task")

    task = Task.find_one(id=1)
    task.done = True
    task.save()
```

Of course, model classes can have [SQL methods](https://hyperflask.github.io/sqlorm/models/#sql-methods-on-models) !

```py
class Task(Model):
    @classmethod
    def find_todos(cls):
        "SELECT * FROM tasks WHERE not done"

    def toggle(self):
        "UPDATE tasks SET done = not done WHERE id = %(self.id)s"

with engine:
    tasks = Task.find_todos()
    task = next(tasks)
    task.toggle()
```

As you've noticed, model classes [do not need to know the columns in advance](https://hyperflask.github.io/sqlorm/models/#handling-unknown-columns). However, it's good practice to define the columns for auto completion, type checking and DDL statements generation. SQLORM lets you do that [using Python annotations](https://hyperflask.github.io/sqlorm/models/#defining-models):

```py
from sqlorm import PrimaryKey

class Task(Model):
    id: PrimaryKey[int]
    title: str
    done: bool
```

Model classes provide many more utilities for handling relationships, lazy loading, column types, etc.

As mentioned earlier, model classes are not attached to any particular engine — they run on the engine provided by the current context. This makes it easy to implement patterns such as reading from a replica and writing to the primary.

We can implement reading from a replica and writing to the primary in a few lines:

```py
main = Engine.from_uri("postgresql://main")
replica = Engine.from_uri("postgresql://replica")

with replica:
    task = Task.get(1)
    if not task.done:
        with main:
            task.toggle()
```

SQLORM has many more powerful features. It is [well documented](https://hyperflask.github.io/sqlorm) and provides an [integration with Flask](https://github.com/hyperflask/flask-sqlorm). Try it out !