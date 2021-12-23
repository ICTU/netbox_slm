## Software Lifecycle Management

### _Netbox Plugin for lifecycle management of software components, including versions and installations_

---

### Installation Guide

Depending on running in Docker (see the netbox-docker repository) add netbox_slm to the plugin_requirements.txt (requires a valid pypi version)

```
netbox-slm==0.1
```

Change the configuration.py to include the plugin:

```
PLUGINS = [
    'netbox_slm',
]
```

### Releasing Guide

_TODO_

### Developer Guide (local installation)

_Follow the steps below on your local system to run netbox and the netbox_slm plugin in developer mode_

### Setup

The goal below is to run all Netbox components in Docker and run a local Netbox Django copy with auto-reload to develop the plugin pointing to the Dockerized postgres and redis instances, basically ignoring the netbox docker runtime server.

### Gotcha's

_Netbox's exception handler seems to supress initial Exceptions, obfuscating missing imports or other Django related issues by re-raising an opague error, e.g. netbox_slm plugin namespace doesnotexist. It's recommended to often check the runtime server or patch Netbox's global exception handler._

### Steps

```
from your projects directory clone the netbox repository

$ git clone https://github.com/netbox-community/netbox
$ cd netbox
$ git checkout f5356b8 (to pin 3.0.9)

install the virtual environment

$ pipenv shell
$ pipenv install

create and edit netbox/configuration.py (based on the template file) add these lines at the end of the file;

DEBUG = True
SECRET_KEY = 'dummy'
DEVELOPER = True
PLUGINS = [
    'netbox_slm',
]
````

The Netbox installation above will be used to run Django management commands like runserver, makemigrations and migrate, which will be explained in the next steps below;

```
from your projects directory clone the netbox-slm repository

$ git clone https://github.com/ICTU/netbox_slm
$ cd netbox_slm
$ ./start-netbox.sh
````

This will start Netbox locally (requires Docker) and forward the redis and postgres ports to the localhost (make sure there's no processes using these ports or change the dockerfiles accordingly)

Note, you can also start and stop netbox by hand:
```
$ cd netbox-docker
$ docker-compose up -d

or stop the stack with

$ docker-compose down

# to start fresh:

$ docker-compose down
$ docker volume rm netbox-docker_netbox-postgres-data  # et cetera
$ docker-compose up -d --force-recreate

this will require you to re-run the migrate commando's for netbox-slm, see further down below
```

Go back to the netbox configuration.py file and update the postgres and redis connection strings (username, password) to the ones the netbox docker backend is using, for example (using default user and passwords from the netbox docker example):

```
<<collapsed>>

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

<<collapsed>>
```

Now you can run commands from the netbox repository like this;

```
$ cd netbox/netbox
$ export PYTHONPATH=../../netbox-slm/src/
$ python3 manage.py migrate netbox_slm
$ python3 manage.py runserver 8001
```

Visit http://127.0.0.1:8001 in the browesr to see the auto reloading version of the netbox UI. Port 8000 is taken by the docker ran variant.
