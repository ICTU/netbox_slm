import django_tables2 as tables
from django.db.models import Count, F, Value

from netbox.tables import NetBoxTable, ToggleColumn, columns
from netbox_slm.models import SoftwareProduct, SoftwareProductVersion, SoftwareProductInstallation, SoftwareLicense


class SoftwareProductTable(NetBoxTable):
    """Table for displaying SoftwareProduct objects."""

    pk = ToggleColumn()
    name = tables.LinkColumn()
    manufacturer = tables.Column(accessor="manufacturer", linkify=True)
    installations = tables.Column(accessor="get_installation_count", verbose_name="Installations")

    tags = columns.TagColumn(url_name="plugins:netbox_slm:softwareproduct_list")

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
        queryset = queryset.annotate(count=Count("softwareproductinstallation__id")).order_by(
            ("-" if is_descending else "") + "count"
        )
        return queryset, True


class SoftwareProductVersionTable(NetBoxTable):
    """Table for displaying SoftwareProductVersion objects."""

    pk = ToggleColumn()
    name = tables.LinkColumn(verbose_name="Version")
    software_product = tables.Column(accessor="software_product", linkify=True)
    manufacturer = tables.Column(accessor="software_product__manufacturer", linkify=True)
    installations = tables.Column(accessor="get_installation_count", verbose_name="Installations")

    tags = columns.TagColumn(url_name="plugins:netbox_slm:softwareproductversion_list")

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
        queryset = queryset.annotate(count=Count("softwareproductinstallation__id")).order_by(
            ("-" if is_descending else "") + "count"
        )
        return queryset, True


class SoftwareProductInstallationTable(NetBoxTable):
    """Table for displaying SoftwareProductInstallation objects."""

    pk = ToggleColumn()
    name = tables.LinkColumn()

    device = tables.Column(accessor="device", linkify=True)
    virtualmachine = tables.Column(accessor="virtualmachine", linkify=True)
    cluster = tables.Column(accessor="cluster", linkify=True)
    platform = tables.Column(accessor="platform", linkify=True)
    type = tables.Column(accessor="render_type")
    software_product = tables.Column(accessor="software_product", linkify=True)
    version = tables.Column(accessor="version", linkify=True)

    tags = columns.TagColumn(url_name="plugins:netbox_slm:softwareproductinstallation_list")

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

    def render_software_product(self, value, **kwargs):
        return f"{kwargs['record'].software_product.manufacturer.name} - {value}"


class SoftwareLicenseTable(NetBoxTable):
    """Table for displaying SoftwareLicense objects."""

    pk = ToggleColumn()
    name = tables.LinkColumn()

    type = tables.Column()
    stored_location = tables.Column(accessor="stored_location_txt", linkify=lambda record: record.stored_location_url)

    software_product = tables.Column(accessor="software_product", linkify=True)
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
            "stored_location",
            "start_date",
            "expiration_date",
            "software_product",
            "version",
            "installation",
            "tags",
        )
        default_columns = (
            "pk",
            "name",
            "expiration_date",
            "software_product",
            "installation",
            "tags",
        )

    def render_software_product(self, value, **kwargs):
        return f"{kwargs['record'].software_product.manufacturer.name} - {value}"

    def render_installation(self, **kwargs):
        return f"{kwargs['record'].installation.platform}"
