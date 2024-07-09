ARG PYTHON_VERSION=3.11
FROM python:${PYTHON_VERSION}-alpine AS compile-image

WORKDIR /build
RUN python -m venv /opt/netbox/venv
ENV PATH="/opt/netbox/venv/bin:$PATH"

COPY ../ /build

RUN pip install -U .[build]
RUN python -m build
RUN pip install --no-index /build

FROM netboxcommunity/netbox:v4.0.6

ARG PYTHON_VERSION=3.11
COPY --from=compile-image /opt/netbox/venv/lib/python${PYTHON_VERSION}/site-packages/netbox_slm /opt/netbox/venv/lib/python${PYTHON_VERSION}/site-packages/netbox_slm
