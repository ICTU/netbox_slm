from django.forms import CharField, DateField, ChoiceField
from django.urls import reverse_lazy

from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm, NetBoxModelImportForm
from netbox_slm.models import SoftwareProduct, SoftwareProductVersion, SoftwareProductInstallation, SoftwareLicense
from utilities.forms.constants import BOOLEAN_WITH_BLANK_CHOICES
from utilities.forms.fields import (
    CommentField,
    DynamicModelChoiceField,
    TagFilterField,
    LaxURLField,
    DynamicModelMultipleChoiceField,
)
from utilities.forms.rendering import FieldSet
from utilities.forms.widgets import APISelect, DatePicker


class SoftwareLicenseForm(NetBoxModelForm):
    """Form for creating a new SoftwareLicense object."""

    comments = CommentField()

    stored_location_url = LaxURLField(required=False)

    software_product = DynamicModelChoiceField(
        queryset=SoftwareProduct.objects.all(),
        required=True,
        label="Software Product",
        widget=APISelect(attrs={"data-url": reverse_lazy("plugins-api:netbox_slm-api:softwareproduct-list")}),
    )
    version = DynamicModelChoiceField(
        queryset=SoftwareProductVersion.objects.all(),
        required=False,
        widget=APISelect(attrs={"data-url": reverse_lazy("plugins-api:netbox_slm-api:softwareproductversion-list")}),
        query_params={
            "software_product": "$software_product",
        },
    )
    installation = DynamicModelChoiceField(
        queryset=SoftwareProductInstallation.objects.all(),
        required=False,
        widget=APISelect(
            attrs={"data-url": reverse_lazy("plugins-api:netbox_slm-api:softwareproductinstallation-list")}
        ),
        query_params={
            "software_product": "$software_product",
        },
    )
    start_date = DateField(required=False, widget=DatePicker())
    expiration_date = DateField(required=False, widget=DatePicker())

    class Meta:
        model = SoftwareLicense
        fields = (
            "name",
            "description",
            "software_product",
            "type",
            "stored_location",
            "stored_location_url",
            "start_date",
            "expiration_date",
            "support",
            "license_amount",
            "version",
            "installation",
            "tags",
            "comments",
        )


class SoftwareLicenseFilterForm(NetBoxModelFilterSetForm):
    model = SoftwareLicense
    fieldsets = (
        FieldSet("q", "filter_id", "tag"),
        FieldSet(
            "name", "description", "type", "stored_location", "support", "software_product", "version", "installation"
        ),
    )
    selector_fields = ("q", "filter_id", "name")

    tag = TagFilterField(model)

    name = CharField(required=False)
    description = CharField(required=False)
    type = CharField(required=False)
    stored_location = CharField(required=False)
    support = ChoiceField(required=False, choices=BOOLEAN_WITH_BLANK_CHOICES)

    software_product = DynamicModelMultipleChoiceField(
        queryset=SoftwareProduct.objects.all(),
        required=False,
        label="Software Product",
    )
    version = DynamicModelMultipleChoiceField(
        queryset=SoftwareProductVersion.objects.all(),
        required=False,
    )
    installation = DynamicModelMultipleChoiceField(
        queryset=SoftwareProductInstallation.objects.all(),
        required=False,
    )


class SoftwareLicenseBulkImportForm(NetBoxModelImportForm):
    class Meta:
        model = SoftwareLicense
        fields = (
            "name",
            "description",
            "software_product",
            "type",
            "start_date",
            "expiration_date",
            "support",
            "license_amount",
            "version",
            "installation",
            "tags",
            "comments",
        )
