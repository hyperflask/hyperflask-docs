# Hosting platforms

## Fly.io

Fly.io is the fastest way to deploy a container. It can even scales to 0 and be automatically restarted when new requests arrive, brining hosting cost down.

1. [Install flyctl](https://fly.io/docs/flyctl/install/), their CLI utility: `curl -L https://fly.io/install.sh | sh`
2. Create an account with `fly auth signup` or log in with `fly auth login`.
3. Run `fly launch`
4. Run `fly deploy` to redeploy your app

## VPS or bare metal

[Kamal](https://kamal-deploy.org/) and [Uncloud](https://uncloud.run/) are 2 great options to deploy your app on a VPS.

Example using Uncloud:

1. Install: `curl -fsS https://get.uncloud.run/install.sh | sh`
2. Initialize a machine: `uc machine init root@your-server-ip`
3. Build your image: `docker build . -t my-app-image`
4. Deploy your app: `uc run -p yourdomain.com:80/https my-app-image`

## Static hosting

- [Netlify](https://www.netlify.com/)
- [Static.app](https://static.app/)