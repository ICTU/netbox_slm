from django.forms import DateField, CharField, MultipleChoiceField
from django.urls import reverse_lazy

from dcim.models import Manufacturer
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm, NetBoxModelImportForm
from netbox_slm.models import SoftwareProduct, SoftwareProductVersion, SoftwareReleaseTypes
from utilities.forms.fields import (
    CommentField,
    DynamicModelChoiceField,
    TagFilterField,
    DynamicModelMultipleChoiceField,
)
from utilities.forms.rendering import FieldSet
from utilities.forms.widgets import APISelect, DatePicker


class SoftwareProductVersionForm(NetBoxModelForm):
    """Form for creating a new SoftwareProductVersion object."""

    comments = CommentField()

    release_date = DateField(required=False, widget=DatePicker())
    end_of_support = DateField(required=False, widget=DatePicker())

    software_product = DynamicModelChoiceField(
        queryset=SoftwareProduct.objects.all(),
        required=True,
        label="Software Product",
        widget=APISelect(attrs={"data-url": reverse_lazy("plugins-api:netbox_slm-api:softwareproduct-list")}),
    )

    class Meta:
        model = SoftwareProductVersion
        fields = (
            "name",
            "software_product",
            "release_date",
            "documentation_url",
            "end_of_support",
            "filename",
            "file_checksum",
            "file_link",
            "release_type",
            "tags",
            "comments",
        )


class SoftwareProductVersionFilterForm(NetBoxModelFilterSetForm):
    model = SoftwareProductVersion
    fieldsets = (
        FieldSet("q", "filter_id", "tag"),
        FieldSet("name", "filename", "release_type", "manufacturer", "software_product"),
    )
    selector_fields = ("q", "filter_id", "name")

    tag = TagFilterField(model)

    name = CharField(required=False)
    filename = CharField(required=False)

    release_type = MultipleChoiceField(required=False, choices=SoftwareReleaseTypes.choices)

    manufacturer = DynamicModelMultipleChoiceField(
        queryset=Manufacturer.objects.all(),
        required=False,
    )
    software_product = DynamicModelMultipleChoiceField(
        queryset=SoftwareProduct.objects.all(),
        required=False,
        label="Software Product",
    )


class SoftwareProductVersionBulkImportForm(NetBoxModelImportForm):
    class Meta:
        model = SoftwareProductVersion
        fields = (
            "name",
            "software_product",
            "release_date",
            "end_of_support",
            "filename",
            "file_checksum",
            "release_type",
            "tags",
            "comments",
        )
