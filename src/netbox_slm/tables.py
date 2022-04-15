import django_tables2 as tables

from django.db.models import Count
from django_tables2.utils import Accessor
from netbox_slm.models import SoftwareProduct, SoftwareProductVersion, SoftwareProductInstallation
from netbox.tables import NetBoxTable, ChoiceFieldColumn, ToggleColumn, columns


class SoftwareProductTable(NetBoxTable):
    """Table for displaying SoftwareProduct objects."""

    pk = ToggleColumn()
    name = tables.LinkColumn()
    manufacturer = tables.Column(
        accessor=Accessor('manufacturer'),
        linkify=True
    )
    installations = tables.Column(accessor='get_installation_count', verbose_name='Installations')

    tags = columns.TagColumn(
        url_name="plugins:netbox_slm:softwareproduct_list",
    )

    class Meta(NetBoxTable.Meta):
        model = SoftwareProduct
        fields = (
            "pk",
            "name",
            "manufacturer",
            "description",
            "installations",
            "tags",
        )
        default_columns = (
            "pk",
            "name",
            "manufacturer",
            "description",
            "installations",
            "tags",
        )
        sequence = (
            "manufacturer",
            "name",
            "description",
            "installations",
        )

    def order_installations(self, queryset, is_descending):
        queryset = queryset.annotate(
            count=Count('softwareproductinstallation__id')
        ).order_by(("-" if is_descending else "") + "count")
        return queryset, True


class SoftwareProductVersionTable(NetBoxTable):
    """Table for displaying SoftwareProductVersion objects."""

    pk = ToggleColumn()
    name = tables.LinkColumn(verbose_name='Version')
    software_product = tables.Column(
        accessor=Accessor('software_product'),
        linkify=True
    )
    manufacturer = tables.Column(
        accessor=Accessor('software_product__manufacturer'),
        linkify=True
    )
    installations = tables.Column(accessor='get_installation_count', verbose_name='Installations')

    tags = columns.TagColumn(
        url_name="plugins:netbox_slm:softwareproductversion_list",
    )

    class Meta(NetBoxTable.Meta):
        model = SoftwareProductVersion
        fields = (
            "pk",
            "name",
            "software_product",
            "manufacturer",
            "installations",
            "tags",
        )
        default_columns = (
            "pk",
            "name",
            "software_product",
            "manufacturer",
            "installations",
            "tags",
        )
        sequence = (
            "manufacturer",
            "software_product",
            "name",
            "installations",
        )

    def order_installations(self, queryset, is_descending):
        queryset = queryset.annotate(
            count=Count('softwareproductinstallation__id')
        ).order_by(("-" if is_descending else "") + "count")
        return queryset, True


class SoftwareProductInstallationTable(NetBoxTable):
    """Table for displaying SoftwareProductInstallation objects."""

    pk = ToggleColumn()
    name = tables.LinkColumn()
    device = tables.Column(
        accessor=Accessor('device'),
        linkify=True
    )
    virtualmachine = tables.Column(
        accessor=Accessor('virtualmachine'),
        linkify=True
    )
    platform = tables.Column(
        accessor='get_platform',
        linkify=True
    )
    type = tables.Column(accessor='render_type')
    software_product = tables.Column(
        accessor=Accessor('software_product'),
        linkify=True
    )
    version = tables.Column(
        accessor=Accessor('version'),
        linkify=True
    )

    tags = columns.TagColumn(
        url_name="plugins:netbox_slm:softwareproductinstallation_list",
    )

    class Meta(NetBoxTable.Meta):
        model = SoftwareProductInstallation
        fields = (
            "pk",
            "name",
            "platform",
            "type",
            "software_product",
            "version",
            "tags",
        )
        default_columns = (
            "pk",
            "platform",
            "type",
            "software_product",
            "version",
            "tags",
        )

    def order_platform(self, queryset, is_descending):
        queryset = queryset.order_by(("device" if is_descending else "virtualmachine"))
        return queryset, True

    def order_type(self, queryset, is_descending):
        queryset = queryset.order_by(("device" if is_descending else "virtualmachine"))
        return queryset, True

    def render_software_product(self, value, **kwargs):
        return f"{kwargs['record'].software_product.manufacturer.name} - {value}"
