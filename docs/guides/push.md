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

Hyperflask provides some components to leverage the htmx [sse extension](https://htmx.org/extensions/sse/). 

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
    Using Hyperflask components is optional and htmx sse extension or any EventSource can be used directly.
    
    Retrieve the stream URL for an event using `mercure_hub_url(event_names)`. Use `mercure_authentified_hub_url(event_names)` to create authentified URLs that can receive private events.

    ```html
    <div hx-ext="sse" sse-connect="{{mercure_authentified_hub_url('messages')}}" sse-swap="message" hx-swap="beforeend">
    </div>
    ```

## Using with models

Model objects can be used as topic and/or data when publishing and subscribing. Combined with models rendering capability, this makes it easy to publish rendered objects on a stream.

When using a model class as topic, the topic will be the class name. When using a model object, the topic will be scoped to the object id.

```py
class TodoList(db.Model):
    pass

class TodoItem(db.Model):
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