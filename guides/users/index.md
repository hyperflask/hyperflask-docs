# User management

!!! info
    This feature is provided by [Hyperflask-Users](https://github.com/hyperflask/hyperflask-users). It uses [Flask-Login](https://github.com/maxcountryman/flask-login) for session management.

## Installation

    uv add hyperflask-users

## Setup

Hyperflask-Users requires the creation of a user model.

```py
from hyperflask.factory import db
from hyperflask_users import UserMixin

class User(UserMixin, db.Model):
    pass
```

## Protecting pages

Use `page.login_required()` at the start of any page code block to prevent access for unauthentified users.
You can also decorate endpoints and method functions using the `hyperflask_users.login_required` decorator.

```jpy
---
page.login_required()
---
Your email is {{current_user.email}}
```

When a protected page is accessed, if the user is not authentified, it redirects to the default connection page.

The `current_user` object is automatically available in pages. It represents the current user model object.
Use `current_user.is_authentified` to check if a user is authentified.

## Connection using email and code

The default connection mode is using an email with a verification code sent at this email. This prevents the need for storing passwords and reduce the attack surface.

!!! warning
    This means a properly configured email server is needed.

To redirect to the connection page use `url_for('users.connect')`.

## Connection using email and password

Add the following configuration in your app config.yml:

```yaml
users_allowed_flows: ['password']
```

This will disable code based login and require to signup the traditionnal way (keep "connect" in the list of allowed_flows to allow both methods)

## Connection using third party services

TODO