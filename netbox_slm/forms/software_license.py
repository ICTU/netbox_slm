from django.forms import DateField
from django.urls import reverse_lazy

from netbox.forms import NetBoxModelForm, NetBoxModelImportForm, NetBoxModelBulkEditForm, NetBoxModelFilterSetForm
from netbox_slm.models import SoftwareProduct, SoftwareProductVersion, SoftwareProductInstallation, SoftwareLicense
from utilities.forms.fields import CommentField, DynamicModelChoiceField, TagFilterField, LaxURLField
from utilities.forms.widgets import APISelect, DatePicker


class SoftwareLicenseForm(NetBoxModelForm):
    """Form for creating a new SoftwareLicense object."""

    comments = CommentField()

    stored_location_url = LaxURLField(required=False)

    software_product = DynamicModelChoiceField(
        queryset=SoftwareProduct.objects.all(),
        required=True,
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
            "tags",
            "comments",
        )


class SoftwareLicenseFilterForm(NetBoxModelFilterSetForm):
    model = SoftwareLicense
    fieldsets = ((None, ("q", "tag")),)
    tag = TagFilterField(model)


class SoftwareLicenseImportForm(NetBoxModelImportForm):
    class Meta:
        model = SoftwareLicense
        fields = (
            "name",
            "description",
            "type",
            "stored_location",
            "stored_location_url",
            "start_date",
            "expiration_date",
        )


class SoftwareLicenseBulkEditForm(NetBoxModelBulkEditForm):
    software_product = DynamicModelChoiceField(queryset=SoftwareProduct.objects.all(), required=False)
    version = DynamicModelChoiceField(queryset=SoftwareProductVersion.objects.all(), required=False)
    installation = DynamicModelChoiceField(queryset=SoftwareProductInstallation.objects.all(), required=False)
    model = SoftwareLicense
    fieldsets = (
        (
            None,
            (
                "software_product",
                "version",
                "installation",
            ),
        ),
    )
