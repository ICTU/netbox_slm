from netbox.api.viewsets import NetBoxModelViewSet
from rest_framework.routers import APIRootView

from netbox_slm.api.serializers import (
    SoftwareProductSerializer, SoftwareProductVersionSerializer, SoftwareProductInstallationSerializer,
)
from netbox_slm.filtersets import (
    SoftwareProductFilterSet, SoftwareProductVersionFilterSet, SoftwareProductInstallationFilterSet,
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
    filterset_class = SoftwareProductFilterSet


class SoftwareProductVersionViewSet(NetBoxModelViewSet):
    queryset = SoftwareProductVersion.objects.all()
    serializer_class = SoftwareProductVersionSerializer
    filterset_class = SoftwareProductVersionFilterSet


class SoftwareProductInstallationViewSet(NetBoxModelViewSet):
    queryset = SoftwareProductInstallation.objects.all()
    serializer_class = SoftwareProductInstallationSerializer
    filterset_class = SoftwareProductInstallationFilterSet
