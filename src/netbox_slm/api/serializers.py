from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer
from netbox_slm.models import (
    SoftwareProduct, SoftwareProductVersion, SoftwareProductInstallation,
)


class SoftwareProductSerializer(NetBoxModelSerializer):
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
        return f"{obj.manufacturer.name} - {obj.name}"


class SoftwareProductVersionSerializer(NetBoxModelSerializer):
    display = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_slm-api:softwareproductversion-detail"
    )

    class Meta:
        model = SoftwareProductVersion
        fields = [
            'id', 'display', 'url', 'name', 'software_product', 'tags', 'custom_field_data', 'created', 'last_updated',
        ]

    def get_display(self, obj):
        return obj.name


class SoftwareProductInstallationSerializer(NetBoxModelSerializer):
    display = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_slm-api:softwareproductinstallation-detail"
    )

    class Meta:
        model = SoftwareProductInstallation
        fields = [
            'id', 'display', 'url', 'device', 'virtualmachine', 'software_product', 'version', 'tags',
            'custom_field_data', 'created', 'last_updated',
        ]

    def get_display(self, obj):
        return obj
