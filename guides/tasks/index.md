# Background tasks

Perform long-running or blocking tasks in the background.

!!! info
    This feature uses [Dramatiq](https://dramatiq.io) and [Periodiq](https://gitlab.com/bersace/periodiq)


## Creating tasks

Tasks are python functions decorated with `@app.actor`.

In *app/tasks.py*:

```py
from hyperflask.factory import app

@app.actor
def fetch_url(url):
    # ...
```

## Queuing tasks

Tasks can be queued for execution from anywhere:

```py
from app.tasks import fetch_url
fetch_url.send("http://...")
```

## Scheduled tasks (cron jobs)

```py
from hyperflask.factory import app
from hyperflask import cron

@app.actor(periodiq=cron("1 * * * *"))
def do_something_every_day(url):
    # ...
```

## Brokers

The component queueing and dispatching tasks is called a "broker". Dramatiq supports multiple brokers: [Rabbitmq](https://dramatiq.io/advanced.html#brokers), [Redis](https://dramatiq.io/advanced.html#brokers), [Amazon SQS](https://github.com/Bogdanp/dramatiq_sqs), [Postgresql](https://gitlab.com/dalibo/dramatiq-pg).

The default broker used in Hyperflask uses [sqlite](https://github.com/hyperflask/dramatiq-sqlite). It does not require any kind of setup but will not scale past 1 server. If you want to offload your background processing to a second server, use redis or postgresql.