from django.forms import DateField
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from netbox.forms import NetBoxModelForm, NetBoxModelImportForm, NetBoxModelBulkEditForm, NetBoxModelFilterSetForm
from netbox_slm.models import SoftwareProduct, SoftwareProductVersion, SoftwareProductInstallation, SoftwareLicense
from utilities.forms.fields import DynamicModelChoiceField, TagFilterField
from utilities.forms.widgets import APISelect, DatePicker


class SoftwareLicenseForm(NetBoxModelForm):
    """Form for creating a new SoftwareLicense object."""

    software_product = DynamicModelChoiceField(
        queryset=SoftwareProduct.objects.all(),
        required=True,
        widget=APISelect(
            attrs={"data-url": reverse_lazy("plugins-api:netbox_slm-api:softwareproduct-list")}
        ),
    )
    version = DynamicModelChoiceField(
        queryset=SoftwareProductVersion.objects.all(),
        required=False,
        widget=APISelect(
            attrs={"data-url": reverse_lazy("plugins-api:netbox_slm-api:softwareproductversion-list")}
        ),
        query_params={
            'software_product': '$software_product',
        }
    )
    installation = DynamicModelChoiceField(
        queryset=SoftwareProductInstallation.objects.all(),
        required=False,
        widget=APISelect(
            attrs={"data-url": reverse_lazy("plugins-api:netbox_slm-api:softwareproductinstallation-list")}
        ),
        query_params={
            'software_product': '$software_product',
        }
    )
    start_date = DateField(
        label=_('Start date'),
        required=False,
        widget=DatePicker()
    )
    expiration_date = DateField(
        label=_('Expiration date'),
        required=False,
        widget=DatePicker()
    )

    class Meta:
        model = SoftwareLicense
        fields = ("name", "description", "type", "stored_location", "start_date", "expiration_date",
                  "software_product", "version", "installation", "tags")


class SoftwareLicenseFilterForm(NetBoxModelFilterSetForm):
    model = SoftwareLicense
    fieldsets = (
        (None, ('q', 'tag',)),
    )

    tag = TagFilterField(model)


class SoftwareLicenseImportForm(NetBoxModelImportForm):
    class Meta:
        model = SoftwareLicense
        fields = ("name", "description", "type", "stored_location", "start_date", "expiration_date",)


class SoftwareLicenseBulkEditForm(NetBoxModelBulkEditForm):
    software_product = DynamicModelChoiceField(
        queryset=SoftwareProduct.objects.all(),
        required=False
    )
    version = DynamicModelChoiceField(
        queryset=SoftwareProductVersion.objects.all(),
        required=False
    )
    installation = DynamicModelChoiceField(
        queryset=SoftwareProductInstallation.objects.all(),
        required=False
    )
    model = SoftwareLicense
    fieldsets = (
        (None, ('software_product', 'version', 'installation',)),
    )
