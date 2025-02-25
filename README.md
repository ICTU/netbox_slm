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


## Installation Guide

When using the Docker version of NetBox, first follow the `netbox-docker` [quickstart](https://github.com/netbox-community/netbox-docker#quickstart) instructions to clone the `netbox-docker` repository and set up the ``docker-compose.override.yml``.

Note that this plugin is only tested against a single NetBox version at this time, see [Dockerfile-CI](https://github.com/ICTU/netbox_slm/blob/master/ci/Dockerfile-CI).

Next, follow these instructions (based on the NetBox docker variant [instructions](https://github.com/netbox-community/netbox-docker/wiki/Configuration#custom-configuration-files)) to install the NetBox SLM plugin:

1. Add ``netbox_slm`` to the ``PLUGINS`` list in
   ``configuration/plugins.py``.
2. Create a ``plugin_requirements.txt`` with ``netbox-slm`` as
   contents.
3. Create a ``Dockerfile-SLM`` with contents:

```dockerfile
FROM netboxcommunity/netbox:vX.Y.Z

COPY ../pyproject.toml /tmp/
RUN uv pip install -r /tmp/pyproject.toml
```

4. Create a ``docker-compose.override.yml`` with contents:

```yaml
version: "3.7"
services:
  netbox:
    ports:
      - "8000:8080"
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


## Get in touch

Point of contact for this repository is [Mart Visser](https://github.com/MartVisser), who can be reached by [opening a new issue in this repository's issue tracker](https://github.com/ICTU/netbox_slm/issues/new).
