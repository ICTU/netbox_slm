import django_tables2 as tables
from django_tables2.utils import Accessor
from netbox_slm.models import SoftwareProduct, SoftwareProductVersion
from utilities.tables import BaseTable, ChoiceFieldColumn, ToggleColumn


class SoftwareProductTable(BaseTable):
    """Table for displaying SoftwareProduct objects."""

    pk = ToggleColumn()
    name = tables.LinkColumn()
    manufacturer = tables.Column(
        accessor=Accessor('manufacturer'),
        linkify=True
    )

    # tags = TagColumn(
    #     url_name="plugins:netbox_dns:zone_list",
    # )

    class Meta(BaseTable.Meta):
        model = SoftwareProduct
        fields = (
            "pk",
            "name",
            "manufacturer",
            # "tags",
        )
        default_columns = (
            "pk",
            "name",
            "manufacturer",
            # "tags",
        )


class SoftwareProductVersionTable(BaseTable):
    """Table for displaying SoftwareProductVersion objects."""

    pk = ToggleColumn()
    name = tables.LinkColumn()
    software_product = tables.Column(
        accessor=Accessor('software_product'),
        linkify=True
    )
    manufacturer = tables.Column(
        accessor=Accessor('software_product__manufacturer'),
        linkify=True
    )

    # tags = TagColumn(
    #     url_name="plugins:netbox_dns:zone_list",
    # )

    class Meta(BaseTable.Meta):
        model = SoftwareProductVersion
        fields = (
            "pk",
            "name",
            "software_product",
            "manufacturer",
            # "tags",
        )
        default_columns = (
            "pk",
            "name",
            "software_product",
            "manufacturer",
            # "tags",
        )
