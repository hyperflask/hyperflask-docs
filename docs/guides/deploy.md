# Deploying

!!! info
    This feature is provided by [Docker Web Deploy](https://github.com/hyperflask/docker-web-deploy)

## Build & deploy using Hyperflask-Start

Run the following command:

```
$ uv run hyperflask deploy
```

## Static site generation

Run `hyperflask build`. You site will be generated in the `_site` folder.

!!! tip
    Use `hyperflask csp-header` to print the CSP policy to properly configure your web server.

## Building for production

### Only building the docker image

When using Hyperflask-Start, the app is containerized. Run `docker build .` to build the image.

### Without docker

Run `hyperflask build` to build assets and static content.

In production, assets will not be built and nodejs is not required. Ensure that the file `app/assets.json` and the `public` directory are shipped.

If you have static content, it will be generated in the *_site* folder. You can use a proxy server like nginx to serve urls from this folder first or fallback to your app for hybrid content mode.

## Monitoring

Check out the [recipe on monitoring](/recipes/monitoring).