from django import forms
from django.urls import reverse_lazy
from django.utils.translation import gettext as _

from dcim.models import Device
from netbox.forms import NetBoxModelForm, NetBoxModelImportForm, NetBoxModelBulkEditForm, NetBoxModelFilterSetForm
from netbox_slm.models import SoftwareProductInstallation, SoftwareProduct, SoftwareProductVersion
from utilities.forms.fields import DynamicModelChoiceField, TagFilterField
from utilities.forms.widgets import APISelect
from virtualization.models import VirtualMachine, Cluster


class SoftwareProductInstallationForm(NetBoxModelForm):
    """Form for creating a new SoftwareProductInstallation object."""

    device = DynamicModelChoiceField(queryset=Device.objects.all(), required=False)
    virtualmachine = DynamicModelChoiceField(queryset=VirtualMachine.objects.all(), required=False)
    cluster = DynamicModelChoiceField(queryset=Cluster.objects.all(), required=False)
    software_product = DynamicModelChoiceField(
        queryset=SoftwareProduct.objects.all(),
        required=True,
        widget=APISelect(attrs={"data-url": reverse_lazy("plugins-api:netbox_slm-api:softwareproduct-list")}),
    )
    version = DynamicModelChoiceField(
        queryset=SoftwareProductVersion.objects.all(),
        required=True,
        widget=APISelect(attrs={"data-url": reverse_lazy("plugins-api:netbox_slm-api:softwareproductversion-list")}),
        query_params={
            "software_product": "$software_product",
        },
    )

    class Meta:
        model = SoftwareProductInstallation
        fields = ("device", "virtualmachine", "cluster", "software_product", "version", "tags")

    def clean_version(self):
        version = self.cleaned_data["version"]
        software_product = self.cleaned_data["software_product"]
        if version not in software_product.softwareproductversion_set.all():
            raise forms.ValidationError(
                _(
                    f"Version `{version}` doesn't exist on {software_product}, make sure you've "
                    f"selected a compatible version or first select the software product."
                )
            )
        return version


class SoftwareProductInstallationFilterForm(NetBoxModelFilterSetForm):
    model = SoftwareProductInstallation
    fieldsets = (
        (
            None,
            (
                "q",
                "tag",
            ),
        ),
    )

    tag = TagFilterField(model)


class SoftwareProductInstallationImportForm(NetBoxModelImportForm):
    class Meta:
        model = SoftwareProductInstallation
        fields = tuple()


class SoftwareProductInstallationBulkEditForm(NetBoxModelBulkEditForm):
    software_product = DynamicModelChoiceField(queryset=SoftwareProduct.objects.all(), required=False)
    version = DynamicModelChoiceField(queryset=SoftwareProductVersion.objects.all(), required=False)
    model = SoftwareProductInstallation
    fieldsets = (
        (
            None,
            (
                "software_product",
                "version",
            ),
        ),
    )
