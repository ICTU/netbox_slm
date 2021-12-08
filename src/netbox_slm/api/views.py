from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.routers import APIRootView

from extras.api.views import CustomFieldModelViewSet
from netbox_slm.api.serializers import SoftwareProductSerializer, SoftwareProductVersionSerializer
from netbox_slm.filters import SoftwareProductFilter, SoftwareProductVersionFilter
from netbox_slm.models import SoftwareProduct, SoftwareProductVersion


class NetboxSLMRootView(APIRootView):
    """
    NetboxSLM API root view
    """

    def get_view_name(self):
        return "NetboxSLM"


class SoftwareProductViewSet(CustomFieldModelViewSet):
    queryset = SoftwareProduct.objects.all()
    serializer_class = SoftwareProductSerializer
    filterset_class = SoftwareProductFilter

    # @action(detail=True, methods=["get"])
    # def records(self, request, pk=None):
    #     records = Record.objects.filter(zone=pk)
    #     serializer = RecordSerializer(records, many=True, context={"request": request})
    #     return Response(serializer.data)


class SoftwareProductVersionViewSet(CustomFieldModelViewSet):
    queryset = SoftwareProductVersion.objects.all()
    serializer_class = SoftwareProductVersionSerializer
    filterset_class = SoftwareProductVersionFilter

    # @action(detail=True, methods=["get"])
    # def records(self, request, pk=None):
    #     records = Record.objects.filter(zone=pk)
    #     serializer = RecordSerializer(records, many=True, context={"request": request})
    #     return Response(serializer.data)

# for reference: https://github.com/auroraresearchlab/netbox-dns/blob/main/netbox_dns/api/views.py