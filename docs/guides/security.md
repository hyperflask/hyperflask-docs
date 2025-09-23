# Security

## HTTPS

If you are serving your website behing https, add `server_secured: true` in your config.

This will:

 - force https as the default scheme in url_for()
 - force session cookies to be secured
 - set the `Strict-Transport-Security` to `max-age=31556926; includeSubDomains` (override with `hsts_header` config)

## Content Security Policy

A [Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP) (CSP) is activated by default.

When a policy is active, `X-XSS-Protection: 1; mode=block` and `X-Content-Type-Options: nosniff` headers are also set.

You can disable the CSP header using `csp_header: false` in the config.

### Default policy

| Directive | Sources | Notes |
| --- | --- | --- |
| default-src | 'self' | Will add all safe sources from the config |
| script-src | {default-src} 'unsafe-eval' 'unsafe-inline' |
| style-src | {default-src} 'unsafe-eval' 'unsafe-inline' |
| manifest-src | 'self' |
| connect-src | http: ws: | Will use secure versions if server_secured is true
| img-src | * data: blob: |
| media-src | * data: blob: |
| frame-src | * data: blob: |
| object-src | * data: blob: |

**This policy is a compromise** between safe good defaults requiring a lot of configuration and an easy to use policy as good starting point.

If you are not using any inline scripts, it is recommended to add `csp_unsafe_inline: false` to your config

Unsafe evals are authorized because they are required by Alpine.js. However, Alpine [provides a special build](https://alpinejs.dev/advanced/csp) that works with unsafe eval disabled. This build will be used if unsafe eval is disabled. To disable use `csp_unsafe_eval: false`.

!!! important
    When disabling unsafe eval, install `@alpinejs/csp` first or your javascript builds will not work.

!!! warning
    unsafe-inline is always added in debug mode for compatibility with Flask-DebugToolbar

### Safe sources

Define safe sources using the `csp_safe_src` config.

```yaml
csp_safe_src: ["'self'", "*.gstatic.com", "fonts.googleapis.com"]
```

These sources can be used in any directive of a custom policy using the `'safe-src'` keyword.

### Disable embedding via iframes

To disable embedding via iframes, add `csp_frame_ancestors: false` to your config.

To only allow embedding from a list of sources, set the value to a list of sources.

### Custom policy

The `csp_header` can be a dict where keys are directive names. Using a dict will completely override the default policy. However, unsafe eval and inline configuration still applies. Disable them so they don't impact your custom policy.

## Referrer Policy

The `Referrer-Policy` is set by default to `strict-origin-when-cross-origin`.

Change by setting the `referrer_policy` config.