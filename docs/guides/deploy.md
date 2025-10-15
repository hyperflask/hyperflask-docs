# Deploying

## Build a docker image

When using Hyperflask-Start, a [Dockerfile](https://github.com/hyperflask/hyperflask-start/blob/main/%7B%7Bcookiecutter.project_slug%7D%7D/Dockerfile) is provider to containerized your app.

Run `docker build . -t <image_name>` to build the image.

The image exposes the port 80 and is ready for production.  
[Read about backuping the SQLite database](#backuping-your-sqlite-database).

Use any docker hosting platforms or VPS. Check out our [recipe for hosting providers](/recipes/hosting).

The image exposes some volumes:

- `/app/database`: the database folder. Mount this volume to persist app data.
- `/app/uploads`: the folder where uploaded files are stored. Mount this volume to persist them and [read about other solutions](#storing-uploaded-files).

!!! info
    The image uses [Caddy](https://caddyserver.com/) as proxy server. It proxies request to the web server or the mercure server. It also serves static files.

## Backuping your SQLite database

The provided Dockerfile suppports using [Litestream](https://litestream.io/), a real-time SQLite replication solution. It can replicate your SQLite database to various file storage solution, the most common one being S3 (or compatible).

Build your image with the following env variables:

 - `LITESTREAM_URL`: the replica URL
 - `LITESTREAM_ACCESS_KEY_ID`: access key for the S3 service
 - `LITESTREAM_SECRET_ACCESS_KEY`: secret key for the S3 service
 
Example: `docker build -e LITESTREAM_URL=s3://bucket/app.db -e LITESTREAM_ACCESS_KEY_ID -e LITESTREAM_SECRET_ACCESS_KEY . -t <image_name>`

As an alternative:

- you can provide a `litestream.yml` file in your project directory (it will be copied to `/etc/litestream.yml` on container start)
- you can mount a custom litestream config at runtime: `docker run -v litestream.yml:/etc/litestream.yml ...`

## Storing uploaded files

It is recommended to host files on durable object storage like [AWS S3](https://aws.amazon.com/s3/) or [Cloudflare R2](https://www.cloudflare.com/developer-platform/products/r2/).

You will need to [configure the files storage](/guides/files#using-s3).

## Static site generation

First, it is recommended to check out the [Static content guide](/guides/static).

Run `uv run hyperflask build`. You site will be generated in the `_site` folder.

Use any static hosting platforms, check out our [recipe for hosting providers](/recipes/hosting#static-hosting).

!!! tip
    Use `uv run hyperflask csp-header` to print the CSP policy to properly configure your web server.

## Building without docker

Run `uv run hyperflask build` to build assets and static content.

In production, assets will not be built and nodejs is not required. Ensure that the file `app/assets.json` and the `public` directory are shipped.

If you have static content, it will be generated in the *_site* folder. You can use a proxy server like nginx to serve urls from this folder first or fallback to your app for hybrid content mode.

## Test production mode locally

It is often useful to test your app using its production configuration.

### Using docker

If you have built your app using docker as explained in the first section of this guide, you can start it using:

    docker run --rm -p 5000:80 <image name>

### Without docker

Without using docker, you will not test the full production path but it could be good enough to validate that your app is working properly.

Build your app without docker then run it:

    uv run hyperflask build
    uv run hyperflask run