# Scaling

Hyperflask is made of different processes. It uses [honcho](https://honcho.readthedocs.io/en/latest/) as process manager.

| Process | Description | Defaut port | Can be multiplied
| --- | --- | --- | --- |
| web | The application server handling HTTP requests | 5000 | Yes
| mercurehub | The mercure hub server for SSE | 5500 | No
| worker | The worker that executes background tasks | | Yes
| scheduler | The worker that will trigger cron jobs | | No

Each of these processes can be started independently.

 - web processes can be served by a load balancer proxy (like nginx)
 - worker processes can be hosted on different machines and multipled to handle more tasks

You won't be able to use SQLite as a database once you reach scaling issues. We recommend switching to PostgreSQL.

## Scaling workers

If you are hosting workers on another machine than the app server, a queue server will be needed.

[Dramatiq](https://dramatiq.io/), the background tasks library at the heart of Hyperflask, can use [different brokers](https://dramatiq.io/advanced.html#brokers).

The easiest is to install [valkey](https://valkey.io/) and use the redis broker.

## Using multiple database servers

SQLORM supports using [multiple engines](https://github.com/hyperflask/flask-sqlorm#using-multiple-engines).

For example, you can have a primary server for read/writes and a replica for reads.