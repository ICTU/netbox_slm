from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.routers import APIRootView

from netbox.api.viewsets import NetBoxModelViewSet
from netbox_slm.api.serializers import (
    SoftwareProductSerializer, SoftwareProductVersionSerializer, SoftwareProductInstallationSerializer,
)
from netbox_slm.filters import (
    SoftwareProductFilter, SoftwareProductVersionFilter, SoftwareProductInstallationFilter,
)
from netbox_slm.models import (
    SoftwareProduct, SoftwareProductVersion, SoftwareProductInstallation,
)


class NetboxSLMRootView(APIRootView):
    """
    NetboxSLM API root view
    """

    def get_view_name(self):
        return "NetboxSLM"


class SoftwareProductViewSet(NetBoxModelViewSet):
    queryset = SoftwareProduct.objects.all()
    serializer_class = SoftwareProductSerializer
    filterset_class = SoftwareProductFilter


class SoftwareProductVersionViewSet(NetBoxModelViewSet):
    queryset = SoftwareProductVersion.objects.all()
    serializer_class = SoftwareProductVersionSerializer
    filterset_class = SoftwareProductVersionFilter


class SoftwareProductInstallationViewSet(NetBoxModelViewSet):
    queryset = SoftwareProductInstallation.objects.all()
    serializer_class = SoftwareProductInstallationSerializer
    filterset_class = SoftwareProductInstallationFilter
