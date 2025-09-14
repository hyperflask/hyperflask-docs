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

| Key | Description | Default location | Default value |
| --- | --- | --- | --- |
| SECRET_KEY | The encryption key for all secret values (including the session) | .env | random