from django.db.models import Q

from netbox.filtersets import NetBoxModelFilterSet
from netbox_slm.models import *


class SoftwareProductFilterSet(NetBoxModelFilterSet):
    """Filter capabilities for SoftwareProduct instances."""
    class Meta:
        model = SoftwareProduct
        fields = tuple()

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = Q(name__icontains=value) | \
                    Q(manufacturer__name__icontains=value)
        return queryset.filter(qs_filter)


class SoftwareProductVersionFilterSet(NetBoxModelFilterSet):
    """Filter capabilities for SoftwareProductVersion instances."""
    class Meta:
        model = SoftwareProductVersion
        fields = tuple()

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = Q(name__icontains=value) | \
                    Q(software_product__name__icontains=value) | \
                    Q(software_product__manufacturer__name__icontains=value)
        return queryset.filter(qs_filter)


class SoftwareProductInstallationFilterSet(NetBoxModelFilterSet):
    """Filter capabilities for SoftwareProductInstallation instances."""
    class Meta:
        model = SoftwareProductInstallation
        fields = tuple()

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = Q(software_product__name__icontains=value) | \
                    Q(software_product__manufacturer__name__icontains=value) | \
                    Q(version__name__icontains=value)
        return queryset.filter(qs_filter)
