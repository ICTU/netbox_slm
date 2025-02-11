# NetBox SLM

<p align="center"><i>NetBox SLM is a plugin for lifecycle management of software components, including versions and installations.</i></p>

<div align="center">
<a href="https://pypi.org/project/netbox_slm/"><img src="https://img.shields.io/pypi/v/netbox_slm" alt="PyPi"/></a>
<a href="https://github.com/ICTU/netbox_slm/stargazers"><img src="https://img.shields.io/github/stars/ICTU/netbox_slm" alt="Stars Badge"/></a>
<a href="https://github.com/ICTU/netbox_slm/network/members"><img src="https://img.shields.io/github/forks/ICTU/netbox_slm" alt="Forks Badge"/></a>
<a href="https://github.com/ICTU/netbox_slm/pulls"><img src="https://img.shields.io/github/issues-pr/ICTU/netbox_slm" alt="Pull Requests Badge"/></a>
<a href="https://github.com/ICTU/netbox_slm/issues"><img src="https://img.shields.io/github/issues/ICTU/netbox_slm" alt="Issues Badge"/></a>
<a href="https://github.com/ICTU/netbox_slm/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/ICTU/netbox_slm?color=2b9348"></a>
<a href="https://github.com/ICTU/netbox_slm/blob/master/LICENSE"><img src="https://img.shields.io/github/license/ICTU/netbox_slm?color=2b9348" alt="License Badge"/></a>
</div>


## Known Issues

- WARNING: This plugin is only tested with a single NetBox version at this time.
- CSV/Bulk imports for SoftwareProduct, Version and Installation are currently broken (WIP)

## Installation Guide

When using the Docker version of NetBox, first follow the `netbox-docker` [quickstart](https://github.com/netbox-community/netbox-docker#quickstart) instructions to clone the `netbox-docker` repository and set up the ``docker-compose.override.yml``.

Next, follow these instructions (based on the NetBox docker variant
[instructions](https://github.com/netbox-community/netbox-docker/wiki/Configuration#custom-configuration-files))
to install the NetBox SLM plugin:

1. Add ``netbox_slm`` to the ``PLUGINS`` list in
   ``configuration/plugins.py``.
2. Create a ``plugin_requirements.txt`` with ``netbox-slm`` as
   contents.
3. Create a ``Dockerfile-SLM`` with contents:

   ```
   FROM netboxcommunity/netbox:vX.Y.Z

   COPY ./plugin_requirements.txt /
   RUN /opt/netbox/venv/bin/pip install --no-warn-script-location -r /plugin_requirements.txt
   ```

4. Create a ``docker-compose.override.yml`` with contents:

   ```
   version: '3.7'
   services:
     netbox:
       ports:
         - 8000:8080
       build:
         context: .
         dockerfile: Dockerfile-SLM
       image: netbox:slm
     netbox-worker:
       image: netbox:slm
     netbox-housekeeping:
       image: netbox:slm
   ```

Now, build the image: ``docker compose build --no-cache``

And finally, run NetBox with the SLM plugin: ``docker compose up``

## Releasing Guide

To draft a release;

update the `netbox_slm/__init__.py` file to reflect the new version, then from the *src*
directory run

   ```
   $ python -m build
   $ twine upload dist/*
   ```

On GitHub create a similar tag and version.


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

   ```
   $ git clone https://github.com/netbox-community/netbox
   $ cd netbox
   ```
   
install the virtual environment
   
   ```
   $ pipenv shell
   $ pipenv install
   ```

create and edit `netbox/configuration.py` (based on the template file) add these lines at the end of the file;
   
   ```
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

   ```
   $ git clone https://github.com/ICTU/netbox_slm
   $ cd netbox_slm
   $ ./start-netbox.sh
   ```
   
This will start NetBox locally (requires Docker) and forward the Redis
and PostgreSQL ports to the localhost (make sure there’s no processes
using these ports or change the Dockerfile(s) accordingly)

Note, you can also start and stop NetBox by hand:

   ```
   $ cd netbox-docker
   $ docker compose up -d
   ```
   
or stop the stack with

   ```
   $ docker compose down
   ```
   
# to start fresh:

   ```
   $ docker compose down
   $ docker volume rm netbox-docker_netbox-postgres-data  # et cetera
   $ docker compose up -d --force-recreate
   ```
   
this will require you to re-run the migrate commando's for `netbox_slm`, see further down below

Go back to the NetBox `configuration.py` file and update the PostgreSQL and
Redis connection strings (username, password) to the ones the NetBox
Docker backend is using, for example (using default user and passwords
from the NetBox Docker example):

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
   
Now you can run commands from the NetBox repository like this;

   ```
   $ cd netbox/netbox
   $ export PYTHONPATH=../../netbox_slm/netbox_slm/  # or with the pipenv activated run `python3 setup.py develop` from the netbox_slm directory
   $ python3 manage.py migrate netbox_slm
   $ python3 manage.py runserver 8001
   ```

Visit http://127.0.0.1:8001 in the browser to see the auto reloading version of the NetBox UI.
Port 8000 is taken by the Docker ran variant.


## Get in touch

Point of contact for this repository is [Mart Visser](https://github.com/MartVisser), who can be reached by [opening a new issue in this repository's issue tracker](https://github.com/ICTU/netbox_slm/issues/new).
