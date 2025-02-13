from django.forms import ValidationError
from django.urls import reverse_lazy

from dcim.models import Device
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm, NetBoxModelImportForm
from netbox_slm.models import SoftwareProductInstallation, SoftwareProduct, SoftwareProductVersion
from utilities.forms.fields import (
    CommentField,
    DynamicModelChoiceField,
    TagFilterField,
    DynamicModelMultipleChoiceField,
)
from utilities.forms.rendering import FieldSet
from utilities.forms.widgets import APISelect
from virtualization.models import VirtualMachine, Cluster


class SoftwareProductInstallationForm(NetBoxModelForm):
    """Form for creating a new SoftwareProductInstallation object."""

    comments = CommentField()

    device = DynamicModelChoiceField(queryset=Device.objects.all(), required=False)
    virtualmachine = DynamicModelChoiceField(
        queryset=VirtualMachine.objects.all(),
        required=False,
        label="Virtual Machine",
    )
    cluster = DynamicModelChoiceField(queryset=Cluster.objects.all(), required=False)
    software_product = DynamicModelChoiceField(
        queryset=SoftwareProduct.objects.all(),
        required=True,
        label="Software Product",
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
        fields = (
            "device",
            "virtualmachine",
            "cluster",
            "software_product",
            "version",
            "tags",
            "comments",
        )

    def clean_version(self):
        version = self.cleaned_data["version"]
        software_product = self.cleaned_data["software_product"]
        if version not in software_product.softwareproductversion_set.all():
            raise ValidationError(
                f"Version '{version}' doesn't exist on {software_product}, make sure you've "
                f"selected a compatible version or first select the software product."
            )
        return version


class SoftwareProductInstallationFilterForm(NetBoxModelFilterSetForm):
    model = SoftwareProductInstallation
    fieldsets = (
        FieldSet("q", "filter_id", "tag"),
        FieldSet("device", "virtualmachine", "cluster", "software_product", "version"),
    )
    selector_fields = ("filter_id", "q")

    tag = TagFilterField(model)

    device = DynamicModelMultipleChoiceField(
        queryset=Device.objects.all(),
        required=False,
    )
    virtualmachine = DynamicModelMultipleChoiceField(
        queryset=VirtualMachine.objects.all(),
        required=False,
        label="Virtual Machine",
    )
    cluster = DynamicModelMultipleChoiceField(
        queryset=Cluster.objects.all(),
        required=False,
    )
    software_product = DynamicModelMultipleChoiceField(
        queryset=SoftwareProduct.objects.all(),
        required=False,
        label="Software Product",
    )
    version = DynamicModelMultipleChoiceField(
        queryset=SoftwareProductVersion.objects.all(),
        required=False,
    )


class SoftwareProductInstallationBulkImportForm(NetBoxModelImportForm):
    class Meta:
        model = SoftwareProductInstallation
        fields = (
            "device",
            "virtualmachine",
            "cluster",
            "software_product",
            "version",
            "tags",
            "comments",
        )
