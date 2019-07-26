# Thoth

Thoth is a bullet journal application in Python and TypeScript. Meant to replace the physical book,
intended to be used on any smart device. Named after the egyptian god Thoth, god of writing,
magic, wisdom, and the moon.

## Setup

``make install``
``make assets``

## Migrations

Once all the builds have completed successfully, apply the migrations using the Django built-in migration tools.
Execute ``poetry run python manage.py migrate``

Thoth's ``user`` and ``entries`` models are minimal, extension is simple. If extended, you must apply
the migrations by running the following.
``poetry run python manage.py makemigrations ; poetry run python manage.py migrate``.

## Running

### Frontend development

The frontend javascript is compiled from typescript using babel. Any changes made to the frontend will require execution of ``make assets`` in order to recompile.


### Development

Running in a development environment is simple, after setup, use poetry to run Django's ``manage.py`` with,
``poetry run python manage.py runserver``

### Production

When deploying the application to a production environment, you'll want to keep the application alive forever. Though, this is not the only option here, running a [systemd](https://www.freedesktop.org/wiki/Software/systemd/) service to manage a [gunicorn](https://gunicorn.org) server is recommended.

#### Gunicorn server example

To run the gunicorn server manually from command line inside from our virtual environment.
``poetry run gunicorn --access-logfile - --workers 3 --bind unix:$HOME/path/to/thoth/thoth.sock index.wsgi:application``

To enable service management with `systemd` place the above line in a script named `run.sh` in the project root.

#### Systemd service example

The following `.service` file should be in `/etc/systemd/system/`.

```
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=thoth
Group=www-data
WorkingDirectory=/path/to/thoth
ExecStart=/bin/sh /path/to/thoth/run.sh


[Install]
WantedBy=multi-user.target
```

### Questions, Issues and Contributions

Any questions in regards to this software, feel free to send an email to, [me@brockramsey.com](mailto:me@brockramsey.com).

If any issues occur when accessing/using this application, please file a [bug report issue](https://github.com/bramz/thoth/issues/new).

To contribute, fork this repository, apply changes to a local branch and [create a pull request](https://github.com/bramz/thoth/compare). All contributions are welcome and will be reviewed accordingly.
