from django import forms
from django.urls import reverse_lazy
from django.utils.translation import gettext as _

from dcim.models import Manufacturer, Device
from netbox.forms import (
    NetBoxModelForm,
    NetBoxModelCSVForm,
    NetBoxModelBulkEditForm,
    NetBoxModelFilterSetForm,
)
from netbox_slm.models import SoftwareProduct, SoftwareProductVersion, SoftwareProductInstallation
from utilities.forms import (
    DynamicModelChoiceField, APISelect, TagFilterField, ChoiceField
)
from virtualization.models import VirtualMachine


class SoftwareProductForm(NetBoxModelForm):
    """Form for creating a new SoftwareProduct object."""

    manufacturer = DynamicModelChoiceField(
        queryset=Manufacturer.objects.all(),
        required=False,
    )

    class Meta:
        model = SoftwareProduct
        fields = ("name", "manufacturer", "description", "tags")


class SoftwareProductFilterForm(NetBoxModelFilterSetForm):
    model = SoftwareProduct
    fieldsets = (
        (None, ('q', 'tag')),
    )

    tag = TagFilterField(model)


class SoftwareProductCSVForm(NetBoxModelCSVForm):
    class Meta:
        model = SoftwareProduct
        fields = ("name", "manufacturer",)


class SoftwareProductBulkEditForm(NetBoxModelBulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=SoftwareProduct.objects.all(),
        widget=forms.MultipleHiddenInput(),
    )

    class Meta:
        model = SoftwareProduct
        nullable_fields = []


class SoftwareProductVersionForm(NetBoxModelForm):
    """Form for creating a new SoftwareProductVersion object."""
    name = forms.CharField(label=_("Version"))

    software_product = DynamicModelChoiceField(
        queryset=SoftwareProduct.objects.all(),
        widget=APISelect(
            attrs={"data-url": reverse_lazy("plugins-api:netbox_slm-api:softwareproduct-list")}
        ),
    )

    class Meta:
        model = SoftwareProductVersion
        fields = ("name", "software_product", "tags")


class SoftwareProductVersionFilterForm(NetBoxModelFilterSetForm):
    model = SoftwareProductVersion
    fieldsets = (
        (None, ('q', 'tag')),
    )

    tag = TagFilterField(model)


class SoftwareProductVersionCSVForm(NetBoxModelCSVForm):
    class Meta:
        model = SoftwareProductVersion
        fields = ("name",)


class SoftwareProductVersionBulkEditForm(NetBoxModelBulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=SoftwareProduct.objects.all(),
        widget=forms.MultipleHiddenInput(),
    )

    class Meta:
        model = SoftwareProductVersion
        nullable_fields = []


class SoftwareProductInstallationForm(NetBoxModelForm):
    """Form for creating a new SoftwareProductInstallation object."""

    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=False,
    )
    virtualmachine = DynamicModelChoiceField(
        queryset=VirtualMachine.objects.all(),
        required=False,
    )
    software_product = DynamicModelChoiceField(
        queryset=SoftwareProduct.objects.all(),
        required=True,
        widget=APISelect(
            attrs={"data-url": reverse_lazy("plugins-api:netbox_slm-api:softwareproduct-list")}
        ),
    )
    version = DynamicModelChoiceField(
        queryset=SoftwareProductVersion.objects.all(),
        required=True,
        widget=APISelect(
            attrs={"data-url": reverse_lazy("plugins-api:netbox_slm-api:softwareproductversion-list")}
        ),
        query_params={
            'software_product': '$software_product',
        }
    )

    class Meta:
        model = SoftwareProductInstallation
        fields = ("device", "virtualmachine", "software_product", "version", "tags")

    def clean_version(self):
        version = self.cleaned_data['version']
        software_product = self.cleaned_data['software_product']
        if version not in software_product.softwareproductversion_set.all():
            raise forms.ValidationError(_(f"Version `{version}` doesn't exist on {software_product}, make sure you've "
                                          f"selected a compatible version or first select the software product."))
        return version

    def clean(self):
        if not any([self.cleaned_data['device'], self.cleaned_data['virtualmachine']]):
            raise forms.ValidationError(_("Installation requires atleast one virtualmachine or device destination."))
        return super(SoftwareProductInstallationForm, self).clean()


class SoftwareProductInstallationFilterForm(NetBoxModelFilterSetForm):
    model = SoftwareProductInstallation
    fieldsets = (
        (None, ('q', 'tag',)),
    )

    tag = TagFilterField(model)


class SoftwareProductInstallationCSVForm(NetBoxModelCSVForm):
    class Meta:
        model = SoftwareProductInstallation
        fields = tuple()


class SoftwareProductInstallationBulkEditForm(NetBoxModelBulkEditForm):
    software_product = DynamicModelChoiceField(
        queryset=SoftwareProduct.objects.all(),
        required=False
    )
    version = DynamicModelChoiceField(
        queryset=SoftwareProductVersion.objects.all(),
        required=False
    )
    model = SoftwareProductInstallation
    fieldsets = (
        (None, ('software_product', 'version',)),
    )
