import django_filters
from django.db.models import Q
from extras.filters import TagFilter
from netbox.filtersets import PrimaryModelFilterSet
from netbox_slm.models import SoftwareProduct, SoftwareProductVersion


class SoftwareProductFilter(PrimaryModelFilterSet):
    """Filter capabilities for SoftwareProduct instances."""

    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )
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


class SoftwareProductVersionFilter(SoftwareProductFilter):
    class Meta:
        model = SoftwareProductVersion
        fields = ("name",)  # "tag")
