# Server push

Allow your frontend to react to server events using [Server Sent Events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events) (SSE).

!!! info
    This feature is provided by [Flask-Mercure-SSE](https://github.com/hyperflask/flask-mercure-sse)

## Publishing events

Use `app.sse.publish(event_name, data)` for publishing a new event. By default, anybody listening on the SSE endpoint will see these events. Add `private=True` to only send to authentified clients.

```py
current_app.sse.publish("messages", "hello world")
```

Data sent with the event can be a string or a json serializable object. You can send rendered component by calling components programmatically:

```py
current_app.sse.publish("messages", current_app.components.ChatMessage(msg="hello world"))
```

## Listening for events

Hyperflask provides some components to leverage the htmx [sse extension](https://four.htmx.org/extensions/hx-sse). 

```jinja
<{MercureStream topic="messages"}>
    {# default content #}
</{MercureStream}>
```

| Property | Required | Type | Description | Default |
|----------|----------|------|-------------|---------|
|topic|Yes|string|The topic name|
|private|No|bool|Whether to use an authentified url|False
|hx_swap|No|string|The swap strategy|beforeend
|type|No|string|The type of event to listen to|message
|auto_scroll|No|bool|Whether to keep the div scrolled at the bottom when receiving new items|False
|Any additional properties|||Will be used as attributes of the div|

To create a div which content will be replaced on each new message, use `hx_swap="innerHTML"`.

!!! info
    Using Hyperflask components is optional and the htmx sse extension or any EventSource can be used directly.
    
    Retrieve the stream URL for an event using `mercure_hub_url(event_names)`. Use `mercure_authentified_hub_url(event_names)` to create authentified URLs that can receive private events.

    ```html
    <div hx-sse:connect="{{mercure_authentified_hub_url('messages')}}" hx-swap="beforeend">
    </div>
    ```

    The htmx sse extension only swaps messages without a type and dispatches typed messages as DOM events.
    Use the `hx-sse:swap` attribute provided by Hyperflask to swap typed messages, on the connected element or its descendants:

    ```html
    <div hx-sse:connect="{{mercure_authentified_hub_url(['topic1', 'topic2'])}}">
        <div hx-sse:swap="topic1" hx-swap="beforeend"></div>
        <div hx-sse:swap="topic2" hx-swap="beforeend"></div>
    </div>
    ```

## Using with models

Model objects can be used as topic and/or data when publishing and subscribing. Combined with models rendering capability, this makes it easy to publish rendered objects on a stream.

When using a model class as topic, the topic will be the class name. When using a model object, the topic will be scoped to the object id.

```py
class TodoList(Model):
    pass

class TodoItem(Model):
    __macro__ = "TodoItem"

todolist = TodoList()
item1 = TodoItem()

# publish the rendered item using the <{TodoItem}/> component
# on the todolist stream named "TodoList/{id}" (where id will be replaced by the list id)
current_app.sse.publish(todolist, item1)
```

## Multiplexing a stream

Publish messages on multiple topics and set a type:

```py
current_app.sse.publish("topic1", "data", type="topic1")
current_app.sse.publish("topic2", "data", type=True) # same effect without repeating topic in type
```

!!! tip
    Add `mercure_type_is_topic: true` to your config file to make it the default behavior.

Connect to multiple topics at once and distinguish messages using their type:

```jinja
<{MercureStreamContext topics=["topic1", "topic2"]}>
    <{MercureStream type="topic1"}>

    </{MercureStream}>
    <{MercureStream type="topic2"}>

    </{MercureStream}>
</{MercureStreamContext}>
```

## Using a Mercure hub on another origin

By default, the Mercure hub is served on the same origin as your app (under `/.well-known/mercure`, proxied by Caddy in the [Docker image](deploy.md)). This is the recommended setup.

If the browser connects to a hub on another origin (eg. `mercure_public_hub_url: https://hub.example.com/.well-known/mercure`), htmx 4 will refuse to connect:

 - htmx only performs same-origin requests by default ([`mode` config](https://four.htmx.org/reference/config/htmx-config-mode))
 - htmx sends `HX-*` headers with every request, which the Mercure hub rejects as it only allows the `authorization`, `cache-control` and `last-event-id` headers in cross-origin requests

Setting `htmx_config: {mode: cors}` is not enough because of the headers, and it would allow all htmx requests to reach other origins.
Instead, only allow SSE connections to go cross-origin using an htmx extension. Create *app/assets/mercure.js*:

```js
// Connects to a Mercure hub hosted on another origin
htmx.registerExtension("mercure-cross-origin", {
  htmx_before_request(elt, detail) {
    const request = detail.ctx.request;
    if (!elt.hasAttribute("hx-sse:connect") || new URL(request.action, location.href).origin === location.origin) return;
    request.mode = "cors";
    // the Mercure hub only allows the authorization, cache-control and last-event-id headers
    for (const name of Object.keys(request.headers)) {
      if (name.toLowerCase().startsWith("hx-")) delete request.headers[name];
    }
  }
});
```

Declare it as a [bundle](assets.md#bundles) in your *config.yml*:

```yaml
assets_bundles:
  - mercure.js
```

The hub must also allow your app origin using the [`cors_origins` directive](https://mercure.rocks/docs/hub/config).

!!! note
    Use the global `htmx` object rather than importing `htmx.org` in your bundles, otherwise a second instance of htmx would be bundled.
    Authentified hub URLs carry the subscription JWT in the URL so cookies are not needed.
