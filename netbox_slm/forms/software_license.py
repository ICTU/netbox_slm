from django.forms import CharField, DateField, ChoiceField, IntegerField, NullBooleanField
from django.urls import reverse_lazy

from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm, NetBoxModelImportForm, NetBoxModelBulkEditForm
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
    comments = CommentField()

    stored_location_url = LaxURLField(required=False)
    start_date = DateField(required=False, widget=DatePicker())
    expiration_date = DateField(required=False, widget=DatePicker())

    software_product = DynamicModelChoiceField(
        queryset=SoftwareProduct.objects.all(),
        required=True,
        label="Software Product",
    )
    version = DynamicModelChoiceField(
        queryset=SoftwareProductVersion.objects.all(),
        required=False,
        widget=APISelect(attrs={"data-url": reverse_lazy("plugins-api:netbox_slm-api:softwareproductversion-list")}),
        query_params=dict(software_product="$software_product"),
    )
    installation = DynamicModelChoiceField(
        queryset=SoftwareProductInstallation.objects.all(),
        required=False,
        widget=APISelect(
            attrs={"data-url": reverse_lazy("plugins-api:netbox_slm-api:softwareproductinstallation-list")}
        ),
        query_params=dict(software_product="$software_product"),
    )

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
            "name",
            "description",
            "type",
            "stored_location",
            "support",
            "software_product_id",
            "version_id",
            "installation_id",
        ),
    )
    selector_fields = ("q", "filter_id", "name")

    tag = TagFilterField(model)

    name = CharField(required=False)
    description = CharField(required=False)
    type = CharField(required=False)
    stored_location = CharField(required=False)
    support = ChoiceField(required=False, choices=BOOLEAN_WITH_BLANK_CHOICES)

    software_product_id = DynamicModelMultipleChoiceField(
        queryset=SoftwareProduct.objects.all(),
        required=False,
        label="Software Product",
    )
    version_id = DynamicModelMultipleChoiceField(
        queryset=SoftwareProductVersion.objects.all(),
        required=False,
        label="Version",
    )
    installation_id = DynamicModelMultipleChoiceField(
        queryset=SoftwareProductInstallation.objects.all(),
        required=False,
        label="Installation",
    )


class SoftwareLicenseBulkImportForm(NetBoxModelImportForm):
    support = NullBooleanField(required=False, help_text="Support (values other than 'True' and 'False' are ignored)")

    class Meta:
        model = SoftwareLicense
        fields = (
            "name",
            "description",
            "software_product",
            "type",
            "stored_location",
            "start_date",
            "expiration_date",
            "support",
            "license_amount",
            "version",
            "installation",
            "tags",
        )


class SoftwareLicenseBulkEditForm(NetBoxModelBulkEditForm):
    model = SoftwareLicense
    fieldsets = (
        FieldSet(
            "type",
            "stored_location",
            "stored_location_url",
            "start_date",
            "expiration_date",
            "support",
            "license_amount",
            "software_product",
            "version",
            "installation",
        ),
    )
    nullable_fields = (
        "type",
        "stored_location",
        "stored_location_url",
        "start_date",
        "expiration_date",
        "support",
        "license_amount",
        "version",
        "installation",
    )

    tag = TagFilterField(model)
    comments = CommentField()

    type = CharField(required=False)
    stored_location = CharField(required=False)
    stored_location_url = LaxURLField(required=False)
    start_date = DateField(required=False, widget=DatePicker())
    expiration_date = DateField(required=False, widget=DatePicker())
    support = ChoiceField(required=False, choices=BOOLEAN_WITH_BLANK_CHOICES)
    license_amount = IntegerField(required=False, min_value=0)

    software_product = DynamicModelChoiceField(
        queryset=SoftwareProduct.objects.all(),
        required=False,
        label="Software Product",
    )
    version = DynamicModelChoiceField(
        queryset=SoftwareProductVersion.objects.all(),
        required=False,
        widget=APISelect(attrs={"data-url": reverse_lazy("plugins-api:netbox_slm-api:softwareproductversion-list")}),
        query_params=dict(software_product="$software_product"),
    )
    installation = DynamicModelChoiceField(
        queryset=SoftwareProductInstallation.objects.all(),
        required=False,
        widget=APISelect(
            attrs={"data-url": reverse_lazy("plugins-api:netbox_slm-api:softwareproductinstallation-list")}
        ),
        query_params=dict(software_product="$software_product"),
    )
