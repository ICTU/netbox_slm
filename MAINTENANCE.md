# Maintenance related tasks


## Version upgrade workflow

1. Update version spec in `netbox_slm/__init__.py` and `sonar-project.properties`
1. Check for any runtime errors and warnings in the `netbox-*` container logs
1. Create new version tag on GitHub, following semantic versioning as: `MAJOR.MINOR.PATCH`
1. Update the `CHANGELOG.md` with new version information and move `[Unreleased]` items to new version section
1. Build the package: `python -m build`
1. Upload the distributions to PyPI: `twine upload --skip-existing dist/*`


## Developer Guide (local installation)

*Follow the steps below on your local system to run NetBox and the
`netbox_slm` plugin in developer mode*

### Setup

The goal below is to run all NetBox components in Docker and run a local
NetBox Django copy with auto-reload to develop the plugin pointing to
the PostgreSQL and Redis container instances, basically ignoring the
NetBox docker runtime server.

### Steps

from your projects directory clone the NetBox repository

```shell
$ git clone https://github.com/netbox-community/netbox
$ cd netbox
```

install the virtual environment

```shell
$ pipenv shell
$ pipenv install
```

create and edit `netbox/configuration.py` (based on the template file) add these lines at the end of the file;

```python
DEBUG = True
SECRET_KEY = 'dummy'
PLUGINS = [
'netbox_slm',
]
```

The NetBox installation above will be used to run Django management
commands like `runserver`, `makemigrations` and `migrate`, which will be
explained in the next steps below;

from your projects directory clone the `netbox_slm` repository

```shell
$ git clone https://github.com/ICTU/netbox_slm
$ cd netbox_slm
$ ./start-netbox.sh
```

This will start NetBox locally (requires Docker) and forward the Redis
and PostgreSQL ports to the localhost (make sure there’s no processes
using these ports or change the Dockerfile(s) accordingly)

Note, you can also start and stop NetBox by hand:

```shell
$ cd netbox-docker
$ docker compose up -d
```

or stop the stack with

```shell
$ docker compose down
```

#### to start fresh:

```shell
$ docker compose down
$ docker volume rm netbox-docker_netbox-postgres-data  # et cetera
$ docker compose up -d --force-recreate
```

this will require you to re-run the migrate commando's for `netbox_slm`, see further down below

Go back to the NetBox `configuration.py` file and update the PostgreSQL and
Redis connection strings (username, password) to the ones the NetBox
Docker backend is using, for example (using default user and passwords
from the NetBox Docker example):

```python
# PostgreSQL database configuration. See the Django documentation for a complete list of available parameters:
#   https://docs.djangoproject.com/en/stable/ref/settings/#databases
DATABASE = {
   'NAME': 'netbox',               # Database name
   'USER': 'netbox',               # PostgreSQL username
   'PASSWORD': 'J5brHrAXFLQSif0K', # PostgreSQL password
   'HOST': 'localhost',            # Database server
   'PORT': '',                     # Database port (leave blank for default)
   'CONN_MAX_AGE': 300,            # Max database connection age
}

# Redis database settings. Redis is used for caching and for queuing background tasks such as webhook events. A separate
# configuration exists for each. Full connection details are required in both sections, and it is strongly recommended
# to use two separate database IDs.
REDIS = {
   'tasks': {
       'HOST': 'localhost',
       'PORT': 6379,
       # Comment out `HOST` and `PORT` lines and uncomment the following if using Redis Sentinel
       # 'SENTINELS': [('mysentinel.redis.example.com', 6379)],
       # 'SENTINEL_SERVICE': 'netbox',
       'PASSWORD': 'H733Kdjndks81',
       'DATABASE': 0,
       'SSL': False,
       # Set this to True to skip TLS certificate verification
       # This can expose the connection to attacks, be careful
       # 'INSECURE_SKIP_TLS_VERIFY': False,
   },
   'caching': {
       'HOST': 'localhost',
       'PORT': 6379,
       # Comment out `HOST` and `PORT` lines and uncomment the following if using Redis Sentinel
       # 'SENTINELS': [('mysentinel.redis.example.com', 6379)],
       # 'SENTINEL_SERVICE': 'netbox',
       'PASSWORD': 'H733Kdjndks81',
       'DATABASE': 1,
       'SSL': False,
       # Set this to True to skip TLS certificate verification
       # This can expose the connection to attacks, be careful
       # 'INSECURE_SKIP_TLS_VERIFY': False,
   }
}
```

Now you can run commands from the NetBox repository like this;

```shell
$ cd netbox/netbox
$ export PYTHONPATH=../../netbox_slm/netbox_slm/  # or with the pipenv activated run `python3 setup.py develop` from the netbox_slm directory
$ python3 manage.py migrate netbox_slm
$ python3 manage.py runserver 8001
```

Visit http://127.0.0.1:8001 in the browser to see the auto reloading version of the NetBox UI.
Port 8000 is taken by the Docker ran variant.
