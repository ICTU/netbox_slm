from rest_framework import serializers

from netbox.api.serializers import PrimaryModelSerializer, OrganizationalModelSerializer
# from netbox_slm.api.nested_serializers import (
#     NestedRecordSerializer,
#     NestedNameServerSerializer,
# )
from netbox_slm.models import SoftwareProduct


class SoftwareProductSerializer(PrimaryModelSerializer):
    display = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_slm-api:softwareproduct-detail"
    )

    class Meta:
        model = SoftwareProduct
        fields = [
            'id', 'display', 'url', 'name', 'tags', 'custom_field_data', 'created', 'last_updated',
        ]

    def get_display(self, obj):
        return obj.name
