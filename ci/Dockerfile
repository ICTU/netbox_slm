ARG PYTHON_VERSION=3.10
FROM python:${PYTHON_VERSION}-alpine AS compile-image

WORKDIR /build
RUN python -m venv /opt/netbox/venv
ENV PATH="/opt/netbox/venv/bin:$PATH"

COPY ../ /build

RUN pip install -U .[build]
RUN python -m build
RUN pip install --no-index /build

FROM netboxcommunity/netbox:v3.7.2

ARG PYTHON_VERSION=3.10
COPY --from=compile-image /opt/netbox/venv/lib/python${PYTHON_VERSION}/site-packages/netbox_slm /opt/netbox/venv/lib/python${PYTHON_VERSION}/site-packages/netbox_slm
