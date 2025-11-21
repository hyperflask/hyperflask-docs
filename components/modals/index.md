# Modals

Use the `Modal` component to create an [HTML dialog element](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog).

```jinja
<{Button onclick="modal1.showModal()" }>Say hello</{Button}>
<{Modal id="modal1"}>
    <{ModalTitle}>Hello!</{ModalTitle}>
    <p>
        How are you doing today ?
    </p>
    <{ModalActions}>
        <{Button}>Close</{Button}>
    </{ModalActions}>
</{Modal}>
```

## Pattern for modal components

Create a backend-driven modal that auto opens when called. Uses the built-in hf-modal htmx extension.

Example *components/SignupModal.jpy*:

```jpy
---
from hyperflask import htmx_redirect

def get():
    pass

def post():
    form = page.form()
    if form.validate():
        # ...
        return htmx_redirect("/")
---
{% form %}
<{Modal}>
    <{ModalTitle}>Hello!</{ModalTitle}>
    <{ModalForm form}>
        <{FormField form.email.email("Email") }/>
        <{FormField form.password.password("Password") }/>
        <{SubmitButton}>Signup</{}>
    </{ModalForm}>
</{Modal}>
```

Using `<{ModalForm}>` ensures that the modal closes on successfull submit. When the `action` attribute is not provided, the URL of the component is used.

!!! tip
    You can also use `htmx_oob()` to update the page instead of redirecting

In a page:

```jinja
<{Button hf_modal=url_for('SignupModal')}>Signup</{}>
```
