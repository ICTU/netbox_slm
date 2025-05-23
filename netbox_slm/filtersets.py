from django.db.models import Q
from django_filters import CharFilter, ModelMultipleChoiceFilter, MultipleChoiceFilter

from dcim.models import Device, Manufacturer
from netbox.filtersets import NetBoxModelFilterSet
from netbox_slm.models import (
    SoftwareProduct,
    SoftwareProductVersion,
    SoftwareProductInstallation,
    SoftwareLicense,
    SoftwareReleaseTypes,
)
from virtualization.models import Cluster, VirtualMachine


class SoftwareProductFilterSet(NetBoxModelFilterSet):
    """Filter capabilities for SoftwareProduct instances."""

    name = CharFilter(lookup_expr="icontains")
    description = CharFilter(lookup_expr="icontains")

    manufacturer_id = ModelMultipleChoiceFilter(queryset=Manufacturer.objects.all())

    class Meta:
        model = SoftwareProduct
        fields = tuple()

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = (
            Q(name__icontains=value)
            | Q(description__icontains=value)
            | Q(manufacturer__name__icontains=value)
            | Q(comments__icontains=value)
        )
        return queryset.filter(qs_filter)


class SoftwareProductVersionFilterSet(NetBoxModelFilterSet):
    """Filter capabilities for SoftwareProductVersion instances."""

    name = CharFilter(lookup_expr="icontains")
    description = CharFilter(lookup_expr="icontains")
    filename = CharFilter(lookup_expr="icontains")

    release_type = MultipleChoiceFilter(choices=SoftwareReleaseTypes.choices)

    manufacturer_id = ModelMultipleChoiceFilter(
        field_name="software_product__manufacturer",
        queryset=Manufacturer.objects.all(),
    )

    software_product_id = ModelMultipleChoiceFilter(
        queryset=SoftwareProduct.objects.all(),
        label="Software Product",
    )

    class Meta:
        model = SoftwareProductVersion
        fields = tuple()

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = (
            Q(name__icontains=value)
            | Q(description__icontains=value)
            | Q(software_product__name__icontains=value)
            | Q(software_product__manufacturer__name__icontains=value)
            | Q(comments__icontains=value)
        )
        return queryset.filter(qs_filter)


class SoftwareProductInstallationFilterSet(NetBoxModelFilterSet):
    """Filter capabilities for SoftwareProductInstallation instances."""

    device_id = ModelMultipleChoiceFilter(queryset=Device.objects.all())
    virtualmachine_id = ModelMultipleChoiceFilter(
        queryset=VirtualMachine.objects.all(),
        label="Virtual Machine",
    )
    cluster_id = ModelMultipleChoiceFilter(queryset=Cluster.objects.all())
    software_product_id = ModelMultipleChoiceFilter(
        queryset=SoftwareProduct.objects.all(),
        label="Software Product",
    )
    version_id = ModelMultipleChoiceFilter(queryset=SoftwareProductVersion.objects.all())

    class Meta:
        model = SoftwareProductInstallation
        fields = tuple()

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = (
            Q(software_product__name__icontains=value)
            | Q(software_product__manufacturer__name__icontains=value)
            | Q(version__name__icontains=value)
            | Q(comments__icontains=value)
        )
        return queryset.filter(qs_filter)


class SoftwareLicenseFilterSet(NetBoxModelFilterSet):
    """Filter capabilities for SoftwareLicense instances."""

    name = CharFilter(lookup_expr="icontains")
    description = CharFilter(lookup_expr="icontains")
    type = CharFilter(lookup_expr="icontains")
    spdx_expression = CharFilter(lookup_expr="icontains", label="SPDX expression")
    stored_location = CharFilter(lookup_expr="icontains")

    software_product_id = ModelMultipleChoiceFilter(
        queryset=SoftwareProduct.objects.all(),
        label="Software Product",
    )
    version_id = ModelMultipleChoiceFilter(queryset=SoftwareProductVersion.objects.all())
    installation_id = ModelMultipleChoiceFilter(queryset=SoftwareProductInstallation.objects.all())

    class Meta:
        model = SoftwareLicense
        fields = ("support",)

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = (
            Q(name__icontains=value)
            | Q(description__icontains=value)
            | Q(software_product__name__icontains=value)
            | Q(version__name__icontains=value)
            | Q(installation__device__name__icontains=value)
            | Q(installation__virtualmachine__name__icontains=value)
            | Q(installation__cluster__name__icontains=value)
            | Q(comments__icontains=value)
        )
        return queryset.filter(qs_filter)
