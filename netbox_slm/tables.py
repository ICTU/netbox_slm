import django_tables2 as tables
from django.db.models import Count, F, Value

from netbox.tables import NetBoxTable, ToggleColumn, columns
from netbox_slm.models import SoftwareProduct, SoftwareProductVersion, SoftwareProductInstallation, SoftwareLicense


class SoftwareProductTable(NetBoxTable):
    """Table for displaying SoftwareProduct objects."""

    pk = ToggleColumn()
    name = tables.LinkColumn()
    manufacturer = tables.Column(accessor="manufacturer", linkify=True)
    installations = tables.Column(accessor="get_installation_count")

    tags = columns.TagColumn(url_name="plugins:netbox_slm:softwareproduct_list")

    class Meta(NetBoxTable.Meta):
        model = SoftwareProduct
        fields = (
            "pk",
            "name",
            "description",
            "manufacturer",
            "installations",
            "tags",
        )
        default_columns = (
            "pk",
            "name",
            "manufacturer",
            "installations",
            "tags",
        )

    def order_installations(self, queryset, is_descending):
        queryset = queryset.annotate(count=Count("softwareproductinstallation__id")).order_by(
            ("-" if is_descending else "") + "count"
        )
        return queryset, True


class SoftwareProductVersionTable(NetBoxTable):
    """Table for displaying SoftwareProductVersion objects."""

    pk = ToggleColumn()
    name = tables.LinkColumn()
    software_product = tables.Column(accessor="software_product", verbose_name="Software Product", linkify=True)
    manufacturer = tables.Column(accessor="software_product__manufacturer", linkify=True)
    installations = tables.Column(accessor="get_installation_count")

    tags = columns.TagColumn(url_name="plugins:netbox_slm:softwareproductversion_list")

    class Meta(NetBoxTable.Meta):
        model = SoftwareProductVersion
        fields = (
            "pk",
            "name",
            "description",
            "software_product",
            "manufacturer",
            "release_date",
            "end_of_support",
            "release_type",
            "installations",
            "tags",
        )
        default_columns = (
            "pk",
            "name",
            "manufacturer",
            "software_product",
            "release_date",
            "installations",
            "tags",
        )

    def order_installations(self, queryset, is_descending):
        queryset = queryset.annotate(count=Count("softwareproductinstallation__id")).order_by(
            ("-" if is_descending else "") + "count"
        )
        return queryset, True


class SoftwareProductInstallationTable(NetBoxTable):
    """Table for displaying SoftwareProductInstallation objects."""

    pk = ToggleColumn()
    platform = tables.Column(accessor="platform", linkify=True)
    type = tables.Column(accessor="render_type")
    manufacturer = tables.Column(accessor="software_product__manufacturer", linkify=True)
    software_product = tables.Column(accessor="software_product", verbose_name="Software Product", linkify=True)
    version = tables.Column(accessor="version", linkify=True)

    tags = columns.TagColumn(url_name="plugins:netbox_slm:softwareproductinstallation_list")

    class Meta(NetBoxTable.Meta):
        model = SoftwareProductInstallation
        fields = (
            "pk",
            "platform",
            "type",
            "manufacturer",
            "software_product",
            "version",
            "tags",
        )
        default_columns = (
            "pk",
            "platform",
            "type",
            "manufacturer",
            "software_product",
            "version",
            "tags",
        )

    def order_platform(self, queryset, is_descending):
        device_annotate = queryset.filter(device__isnull=False).annotate(platform_value=F("device__name"))
        vm_annotate = queryset.filter(virtualmachine__isnull=False).annotate(platform_value=F("virtualmachine__name"))
        cluster_annotate = queryset.filter(cluster__isnull=False).annotate(platform_value=F("cluster__name"))
        queryset_union = device_annotate.union(vm_annotate).union(cluster_annotate)
        return queryset_union.order_by(f"{'-' if is_descending else ''}platform_value"), True

    def order_type(self, queryset, is_descending):
        device_annotate = queryset.filter(device__isnull=False).annotate(render_type=Value("device"))
        vm_annotate = queryset.filter(virtualmachine__isnull=False).annotate(render_type=Value("virtualmachine"))
        cluster_annotate = queryset.filter(cluster__isnull=False).annotate(render_type=Value("cluster"))
        queryset_union = device_annotate.union(vm_annotate).union(cluster_annotate)
        return queryset_union.order_by(f"{'-' if is_descending else ''}render_type"), True


class SoftwareLicenseTable(NetBoxTable):
    """Table for displaying SoftwareLicense objects."""

    pk = ToggleColumn()
    name = tables.LinkColumn()

    type = tables.Column()
    spdx_expression = tables.Column(verbose_name="SPDX expression")
    stored_location = tables.Column(accessor="stored_location_txt", linkify=lambda record: record.stored_location_url)

    manufacturer = tables.Column(accessor="software_product__manufacturer", linkify=True)
    software_product = tables.Column(accessor="software_product", verbose_name="Software Product", linkify=True)
    version = tables.Column(accessor="version", linkify=True)
    installation = tables.Column(accessor="installation", linkify=True)

    tags = columns.TagColumn(url_name="plugins:netbox_slm:softwarelicense_list")

    class Meta(NetBoxTable.Meta):
        model = SoftwareLicense
        fields = (
            "pk",
            "name",
            "description",
            "type",
            "spdx_expression",
            "stored_location",
            "start_date",
            "expiration_date",
            "manufacturer",
            "software_product",
            "version",
            "installation",
            "support",
            "license_amount",
            "tags",
        )
        default_columns = (
            "pk",
            "name",
            "type",
            "manufacturer",
            "software_product",
            "installation",
            "expiration_date",
            "tags",
        )

    def render_installation(self, **kwargs):
        return f"{kwargs['record'].installation.platform}"
