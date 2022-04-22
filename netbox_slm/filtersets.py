from netbox.filtersets import NetBoxModelFilterSet
from netbox_slm.models import *


class SoftwareProductFilterSet(NetBoxModelFilterSet):
    """Filter capabilities for SoftwareProduct instances."""
    class Meta:
        model = SoftwareProduct
        fields = tuple()


class SoftwareProductVersionFilterSet(NetBoxModelFilterSet):
    """Filter capabilities for SoftwareProductVersion instances."""
    class Meta:
        model = SoftwareProductVersion
        fields = tuple()


class SoftwareProductInstallationFilterSet(NetBoxModelFilterSet):
    """Filter capabilities for SoftwareProductInstallation instances."""
    class Meta:
        model = SoftwareProductInstallation
        fields = tuple()
