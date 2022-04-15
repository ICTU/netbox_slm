Software Lifecycle Management
-----------------------------

*Netbox Plugin for lifecycle management of software components, including versions and installations*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

--------------

Installation Guide
~~~~~~~~~~~~~~~~~~

WARNING: This plugin is only tested with Netbox 3.2 at this time.

When using the Docker version of Netbox, first follow the `netbox-docker
quickstart <https://github.com/netbox-community/netbox-docker#quickstart>`__
instructions to clone the netbox-docker repo and set up the
``docker-compose.override.yml``.

Next, follow these instructions (based on the `Netbox docker variant
instructions <https://github.com/netbox-community/netbox-docker/wiki/Configuration#custom-configuration-files>`__)
to install the Netbox SLM plugin:

1. Add ``netbox_slm`` to the ``PLUGINS`` list in
   ``configuration/extra.py``.
2. Create a ``plugin_requirements.txt`` with ``netbox-slm==0.98`` as
   contents.
3. Create a ``Dockerfile-SLM`` with contents:

.. code:: dockerfile

   FROM netboxcommunity/netbox:v3.2.X

   COPY ./plugin_requirements.txt /
   RUN /opt/netbox/venv/bin/pip install --no-warn-script-location -r /plugin_requirements.txt

4. Create a ``docker-compose.override.yml`` with contents:

.. code:: yaml

   version: '3.4'
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

Now, build the image: ``docker compose build --no-cache``

And finally, run Netbox with the SLM plugin: ``docker compose up``

Releasing Guide
~~~~~~~~~~~~~~~

To draft a release;

update the setup.py file to reflect the new version, then from the *src*
directory run

::

   # make sure to update the version in netbox_slm/__init__.py
   $ python setup.py sdist
   $ twine upload dist/*

On Github.com create a similar tag and version. These steps could be
automated with a github workflow.

n.b. Currently the plugin is configured to use a personal pypi account,
this should be changed.

Developer Guide (local installation)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Follow the steps below on your local system to run netbox and the
netbox_slm plugin in developer mode*

Setup
~~~~~

The goal below is to run all Netbox components in Docker and run a local
Netbox Django copy with auto-reload to develop the plugin pointing to
the Dockerized postgres and redis instances, basically ignoring the
netbox docker runtime server.

Steps
~~~~~

::

   from your projects directory clone the netbox repository

   $ git clone https://github.com/netbox-community/netbox
   $ cd netbox

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

The Netbox installation above will be used to run Django management
commands like runserver, makemigrations and migrate, which will be
explained in the next steps below;

::

   from your projects directory clone the netbox-slm repository

   $ git clone https://github.com/ICTU/netbox_slm
   $ cd netbox_slm
   $ ./start-netbox.sh

This will start Netbox locally (requires Docker) and forward the redis
and postgres ports to the localhost (make sure there’s no processes
using these ports or change the dockerfiles accordingly)

Note, you can also start and stop netbox by hand:

::

   $ cd netbox-docker
   $ docker-compose up -d

   or stop the stack with

   $ docker-compose down

   # to start fresh:

   $ docker-compose down
   $ docker volume rm netbox-docker_netbox-postgres-data  # et cetera
   $ docker-compose up -d --force-recreate

   this will require you to re-run the migrate commando's for netbox-slm, see further down below

Go back to the netbox configuration.py file and update the postgres and
redis connection strings (username, password) to the ones the netbox
docker backend is using, for example (using default user and passwords
from the netbox docker example):

::

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

Now you can run commands from the netbox repository like this;

::

   $ cd netbox/netbox
   $ export PYTHONPATH=../../netbox-slm/src/
   $ python3 manage.py migrate netbox_slm
   $ python3 manage.py runserver 8001

Visit http://127.0.0.1:8001 in the browesr to see the auto reloading
version of the netbox UI. Port 8000 is taken by the docker ran variant.
