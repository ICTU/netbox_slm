from django.forms import DateField, CharField, MultipleChoiceField
from django.urls import reverse_lazy

from dcim.models import Manufacturer
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm, NetBoxModelImportForm, NetBoxModelBulkEditForm
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
            "description",
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
        FieldSet("name", "description", "filename", "release_type", "manufacturer_id", "software_product_id"),
    )
    selector_fields = ("q", "filter_id", "name")

    tag = TagFilterField(model)

    name = CharField(required=False)
    description = CharField(required=False)
    filename = CharField(required=False)

    release_type = MultipleChoiceField(required=False, choices=SoftwareReleaseTypes.choices)

    manufacturer_id = DynamicModelMultipleChoiceField(
        queryset=Manufacturer.objects.all(),
        required=False,
        label="Manufacturer",
    )
    software_product_id = DynamicModelMultipleChoiceField(
        queryset=SoftwareProduct.objects.all(),
        required=False,
        label="Software Product",
    )


class SoftwareProductVersionBulkImportForm(NetBoxModelImportForm):
    release_type = CharField(help_text=f"Release type (possible values: {SoftwareReleaseTypes.values})")

    class Meta:
        model = SoftwareProductVersion
        fields = (
            "name",
            "description",
            "software_product",
            "release_date",
            "end_of_support",
            "filename",
            "file_checksum",
            "release_type",
            "tags",
        )


class SoftwareProductVersionBulkEditForm(NetBoxModelBulkEditForm):
    model = SoftwareProductVersion
    fieldsets = (
        FieldSet(
            "release_date",
            "documentation_url",
            "end_of_support",
            "filename",
            "file_checksum",
            "file_link",
            "release_type",
            "software_product",
        ),
    )
    nullable_fields = ("release_date", "documentation_url", "end_of_support", "filename", "file_checksum", "file_link")

    tag = TagFilterField(model)
    comments = CommentField()

    release_date = DateField(required=False, widget=DatePicker())
    documentation_url = CharField(required=False)
    end_of_support = DateField(required=False, widget=DatePicker())
    filename = CharField(required=False)
    file_checksum = CharField(required=False)
    file_link = CharField(required=False)

    release_type = MultipleChoiceField(required=False, choices=SoftwareReleaseTypes.choices)

    software_product = DynamicModelChoiceField(
        queryset=SoftwareProduct.objects.all(),
        required=False,
        label="Software Product",
    )
