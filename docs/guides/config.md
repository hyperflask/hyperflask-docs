# Configuration

Hyperflask configuration is stored in a YAML file called *config.yml* at the root of your project folder.

Loaded configuration is then available through `app.config`.

To prevent including secret variables in the config file, you can use environment variables. Any variable prefixed using `FLASK_` will be used a a configuration value.
`FLASK_SECRET_KEY` would be available under `app.config['SECRET_KEY']`.

A *.env* file containing environment variables can be placed at the root of your project folder. It will be automatically loaded.

!!! info
    This feature is provided by [Flask-Configurator](https://github.com/hyperflask/flask-configurator)

## Environment-specific configuration

Hyperflask defines the concept of environments to load different set of configs depending on the execution context.

The default environment is named *production*. When debug is activated, the environment is set to * development*.
The environment can be overriden using the `ENV` configuration (or `FLASK_ENV` environment variable).

An environment specific configuration file can be created. It will be loaded after *config.yml* and will override its values.
The format should be *config.env_name.yml*, so *config.production.yml* or *config.development.yml* for the default environments.

An environment specific *.env* file can also be created following the format *.env.env_name*, so *.env.production* or *.env.development*.

## Common configuration values

See [Flask documentation](https://flask.palletsprojects.com/en/stable/config/#builtin-configuration-values) for the full list of Flask options.

Each Flask extension may have their own configuration.

| Key | Type | Description | Default value |
| --- | --- | --- | --- |
| SECRET_KEY | str | The encryption key for all secret values (including the session) (set by default in .env) | random
| SITE_TITLE | str |  |
| SITE_LANG | str |  |
| HTMX_EXT | list[str] |  |
| HTMX_BOOST_SITE | bool |  |
| EMAIL_BACKGROUND_COLOR | str |  |
| EMAIL_BACKGROUND_ACCENT_COLOR | str |  |
| STATIC_MODE | str |  |
| MARKDOWN_OPTIONS | dict |  |
| FLASH_TOAST_OOB | bool | Whether to add flash messages to htmx request as oob swaps |
| FLASH_TOAST_REMOVE_AFTER | str | Use the remove-me htmx extension to auto remove the toast alerts after some time |
| INIT_DATABASE | bool | Whether to automatically init the db on start |