# Hosting platforms

Make sure you have read the [deployment guide](/guides/deploy).

!!! note
    Commercial services mentionned here are chosen for their quality. No commercial affiliation.

## Fly.io

Fly.io is the fastest way to deploy a container. It can even scales to 0 and be automatically restarted when new requests arrive, bringing hosting cost down.

1. [Install flyctl](https://fly.io/docs/flyctl/install/), their CLI utility: `curl -L https://fly.io/install.sh | sh`
2. Create an account with `fly auth signup` or log in with `fly auth login`.
3. Run `fly launch --secret "FLASK_SECRET_KEY=$(uv run hyperflask gen secret-key)"`
4. Run `fly deploy` to redeploy your app

### Using litestream

1. Create a storage: `fly storage create`
2. Add the following section to your `fly.toml` file:

```toml
[env]
  LITESTREAM_ENDPOINT = "fly.storage.tigris.dev"
  LITESTREAM_BUCKET = "YOUR_BUCKET_NAME"
  LITESTREAM_REGION = "auto"
```

Re-deploy using `fly deploy`

(Credentials for the storage will be provided directly by the platform)

## Digital Ocean

Digital Ocean is an affordable and easy to use all around infrastructure provider. Their [App Platform]() service allows to deploy container images.

1. Create a [container registry](https://cloud.digitalocean.com/registry)
2. Login locally to your registry (follow the provided instructions)
3. [Build your app image](/guides/deploy) using the name `registry.digitalocean.com/<YOUR_REGISTRY>/<IMAGE_NAME>`
4. Push your app image: `docker push registry.digitalocean.com/<YOUR_REGISTRY>/<IMAGE_NAME>`
5. [Create a new app](https://cloud.digitalocean.com/apps/new?source_provider=docr) on Digital Ocean
    - Choose your container registry and your image
    - Add `FLASK_SECRET_KEY` as App-level environment variable, choose encrypt (value can be generated using `uv run hyperflask gen secret-key`)
6. Validate app and wait for deployment

## VPS or bare metal

[Kamal](https://kamal-deploy.org/) and [Uncloud](https://uncloud.run/) are 2 great options to deploy your app on a VPS.

Example using Uncloud:

1. Install: `curl -fsS https://get.uncloud.run/install.sh | sh`
2. Initialize a machine: `uc machine init root@your-server-ip`
3. Create a `.env.production` file and add your production environment variables (notable `FLASK_SECRET_KEY`)
3. Build your image: `docker build --env-file .env.production . -t my-app-image`
4. Deploy your app: `uc run -p yourdomain.com:80/https my-app-image`

## Static hosting

Some well-known providers:

- [Neocities](https://neocities.org/)
- [Netlify](https://www.netlify.com/)
- [Static.app](https://static.app/)