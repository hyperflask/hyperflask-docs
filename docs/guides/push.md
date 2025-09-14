# Server push

Allow your frontend to react to server events using [Server Sent Events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events) (SSE).

!!! info
    This feature is provided by [Flask-Mercure-SSE](https://github.com/hyperflask/flask-mercure-sse)

## Publishing events

Use `app.sse.publish(event_name, data)` for publishing a new event. By default, anybody listening on the SSE endpoint will see these events. Add `private=True` to only send to authentified clients.

```py
current_app.sse.publish("message", "hello world")
```

Data sent with the event can be a string or a json serializable object. You can send rendered component by calling components programmatically:

```py
current_app.sse.publish("message", current_app.components.ChatMessage(msg="hello world"))
```

## Listening for events

Use htmx [sse extension](https://htmx.org/extensions/sse/) to connect to the SSE stream. Retrieve the stream URL for an event using `mercure_hub_url(event_names)`. Use `mercure_authentified_hub_url(event_names)` to create authentified URLs that can receive private events.

```html
<div id="messages" hx-ext="sse" sse-connect="{{mercure_authentified_hub_url('messages')}}" hx-swap="beforeend">
</div>
```

Hyperflask also provides a component that encapsulates the previous html:

```
<{MercureStream topic="messages" id="messages"}>
</{MercureStream}>
```

## Differences between dev and prod

While in development, a lightweight dev-only implementation of a Mercure hub is used. It is not meant to be used by more than a few users at once and is for testing only with minimum setup.

When going into production, a proper [Mercure Hub](https://mercure.rocks/docs/hub/install) should be used. The Mercure Hub is bundled inside the production image and will be run alongside your app.