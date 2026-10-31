# Emails

Send emails templated with [MJML](https://mjml.io).

!!! info
    This feature is provided by [Flask-Mailman](https://waynerv.github.io/flask-mailman) and [Flask-Mailman-Templates](https://github.com/hyperflask/flask-mailman-templates)

## Templates

Email templates are located in the *app/emails* folder. The recommended format is MJML for the best possible email compatible html rendering.

Template files can contain a YAML frontmatter with extra metadata like subject. The frontmatter values are templated as well.

```jinja
---
subject: "Welcome {{name}} to example.com!"
---
{% use_layout %}
<mj-text>
    <h1>Hello {{name}},</h1>
    <p>Thank you for joining</p>
</mj-text>
```

A default layout is provided by Hyperflask. Feel free to override it by creating *app/emails/layout.mjml*. Using the directive `{% use_layout %}` ensures that the layout is used for this template.

!!! tip
    When providing your own layout, you can extend from [*base_layout.html*](https://github.com/hyperflask/hyperflask/blob/main/hyperflask/layouts/email.mjml).

## Sending

To send an email, use `send_mail()`:

```py
from hyperflask import send_mail
send_mail("welcome.mjml", "user@example.com")
```

You can provide template variables as keywork arguments.

## Configuring an SMTP server

When developping, [mailpit](https://mailpit.axllent.org/) is running to provide a live view of all the emails you are sending. Access it at <http://localhost:8025>.

!!! info
    When not using Hyperflask-Start, if no backend is defined, mail will be printed on stdout when in debug mode.

For sending email in production, provide the following configuration in your *config.yml*:

```yaml
mail_server: some_server.com
mail_port: 587
mail_username: some_username
mail_password: some_password
mail_use_tls: true
mail_default_sender: no-reply@yourdomain.com
```