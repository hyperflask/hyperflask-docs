# Pages

## Using page actions

Page actions allow you to handle multiple actions through a single POST endpoint.

```python
from flask import Flask, render_template_string
from flask_mercure import Mercure
from flask_stream import PushStream, page_action

app = Flask(__name__)
Mercure(app)
stream = PushStream(app)

@app.route("/", methods=["GET", "POST"])
def index():
    
    @page_action
    def on_send():
        stream.append_to("#messages", f"<p>{request.form['message']}</p>")

    @page_action
    def on_clear():
        stream.replace_content("#messages", "")

    return render_template_string("""
        <form {{hx_page_action("send")}}>
            <textarea name="message"></textarea>
            <button type="submit">Send</button>
        </form>
        <div id="messages"></div>
        <button {{hx_page_action("clear")}}>clear all</button>
        {{connect_push_stream(include_scripts=True)}}
    """)
```