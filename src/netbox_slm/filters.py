import django_filters
from django.db.models import Q
from django.utils.translation import gettext as _
from extras.filters import TagFilter
from netbox.filtersets import PrimaryModelFilterSet
from netbox_slm.models import SoftwareProduct, SoftwareProductVersion, SoftwareProductInstallation
from utilities.forms import DynamicModelMultipleChoiceField


class BaseFilter(PrimaryModelFilterSet):
    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )


class SoftwareProductFilter(BaseFilter):
    """Filter capabilities for SoftwareProduct instances."""

    name = django_filters.CharFilter(
        lookup_expr="icontains",
    )
    # tag = TagFilter()

    class Meta:
        model = SoftwareProduct
        fields = ("name",)  # "tag")

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = Q(name__icontains=value)  # | Q(status__icontains=value)
        return queryset.filter(qs_filter)


class SoftwareProductVersionFilter(BaseFilter):
    name = django_filters.CharFilter(
        lookup_expr="icontains", label="Version"
    )
    # software_product_id = django_filters.ModelMultipleChoiceFilter(
    #     queryset=SoftwareProduct.objects.all(),
    #     label='SoftwareProduct (ID)',
    # )
    # software_product = django_filters.ModelMultipleChoiceFilter(
    #     field_name='software_product__name',
    #     queryset=SoftwareProduct.objects.all(),
    #     to_field_name='name',
    #     label='SoftwareProduct (name)',
    # )
    # tag = TagFilter()

    class Meta:
        model = SoftwareProductVersion
        fields = ("name", "software_product")  # "tag")

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = Q(name__icontains=value)  # | Q(status__icontains=value)
        return queryset.filter(qs_filter)


class SoftwareProductInstallationFilter(BaseFilter):
    class Meta:
        model = SoftwareProductInstallation
        fields = tuple()  # "tag")

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = Q(software_product__name__icontains=value) | Q(version__name__icontains=value)
        return queryset.filter(qs_filter)
