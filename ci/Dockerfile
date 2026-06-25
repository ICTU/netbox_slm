ARG PYTHON_VERSION=3.14
FROM python:${PYTHON_VERSION}-alpine AS compile-image
# Python version build arg is not actually supported by NetBox container image, only used for maintenance convenience

WORKDIR /build
RUN python3 -m venv /opt/netbox/venv &&\
    source /opt/netbox/venv/bin/activate

COPY ../ /build

RUN pip install -U .[build] &&\
    python -m build &&\
    pip install --no-index /build

FROM netboxcommunity/netbox:v4.6.3
ARG PYTHON_VERSION=3.14

COPY --from=compile-image /opt/netbox/venv/lib/python${PYTHON_VERSION}/site-packages/netbox_slm /opt/netbox/venv/lib/python${PYTHON_VERSION}/site-packages/netbox_slm
