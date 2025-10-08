# Monitoring

Monitoring is critical when running app in production. It gives you visibility across your infrastructure and allows you to debug issues without touching production servers.

[Sentry](https://sentry.io/) provides error monitoring allowing you to quickly investigate errors in production. Sentry can also provide performance monitoring, equivalent to OpenTelemetry traces.

[OpenTelemetry](https://opentelemetry.io/) is a set of standards meant to observe production environments across the stack, from server to application.

Both are needed for proper monitoring of your infrastructure but Sentry may be sufficient when running on managed hosting providers.

## Error monitoring using Sentry

It can be easily setup using [Flask-Sentry](https://github.com/hyperflask/flask-sentry):

Install Flask-Sentry:

    uv add flask-sentry

Activate the extension in *config.yml*:

```yml
flask_extensions:
    - "flask_sentry:Sentry":
        dsn: "http://DSN"
```

To track frontend errors, override the default layout in *app/layouts/default.html*:

```jinja
{% extends "layouts/base.html %}

{% block head_assets %}
    {{ init_sentry() }}
{% endblock %}
```

## When using a VPS

When deploying to a VPS, it is recommend to install the [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/) to gather all telemetry data before forwarding it to a remote service.

You can [install the collector](https://opentelemetry.io/docs/collector/installation/) as a container then:

- [Configure the collector to collect hostmetrics](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/hostmetricsreceiver#collecting-host-metrics-from-inside-a-container-linux-only)
- Collect application metrics using [Flask-Observability](https://github.com/hyperflask/flask-observability) and point to the collector

[Grafana](https://grafana.com) is a great service to store and visualize your monitoring data. Their cloud service has a generous free tier but it is hard to self host.  
It can be used as an [OLTP endpoint](https://grafana.com/docs/grafana-cloud/send-data/otlp/send-data-otlp/) to collect OpenTelemetry data. [Configure the collector](https://opentelemetry.io/docs/collector/configuration/#exporters) to export to this endpoint.

[Signoz](https://signoz.io) is an alternative that is purpose built for OpenTelemetry and that can be easily self hosted.

## Uptime monitoring

Uptime monitoring allows you to recieve alerts when your infrastructure is completely down and measures how long it has been down.

Check out [UptimeRobot](https://uptimerobot.com) (commercial service, no affiliation).