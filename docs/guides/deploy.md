# Deploy to production

!!! info
    This feature is provided by [Docker Web Deploy](https://github.com/hyperflask/docker-web-deploy)

## Build & deploy

Run the following command:

```
$ uv run hyperflask deploy
```

## Build only

When using Hyperflask-Start, the app is containerized. Run `docker build .` to build the image.