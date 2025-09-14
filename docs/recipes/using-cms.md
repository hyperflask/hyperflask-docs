# Using a CMS

Hyperflask [collections](/guides/collections) can use an external CMS to fetch content. This can improve the content editing experience for your team while giving you increased control on the rendering.

We recommend using [Strapi](https://strapi.io/) as a headless CMS.

Once you have setup a Strapi account (either cloud or self hosted), create a strapi-backed collection using the following configuration in *config.yml*:

```yaml
collections:
    strapi_content_type_name:
        strapi_url: "http://yourstrapidomain.com/api/your-content-type-id"
        auth_token: "your strapi api token"
```