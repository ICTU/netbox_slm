from django import forms
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from netbox.forms import (
    NetBoxModelForm,
    NetBoxModelCSVForm,
    NetBoxModelBulkEditForm,
    NetBoxModelFilterSetForm,
)
from dcim.models import Manufacturer, Device
from netbox_slm.models import SoftwareProduct, SoftwareProductVersion, SoftwareProductInstallation
from utilities.forms import (
    BootstrapMixin, DynamicModelChoiceField, APISelect, DynamicModelMultipleChoiceField
)
from virtualization.models import VirtualMachine


class SoftwareProductForm(NetBoxModelForm):
    """Form for creating a new SoftwareProduct object."""

    manufacturer = DynamicModelChoiceField(
        queryset=Manufacturer.objects.all(),
        required=False,
        # initial_params={
        #     'device_types': 'device_type'
        # }
    )

    class Meta:
        model = SoftwareProduct
        fields = ("name", "manufacturer", "description", "tags")


class SoftwareProductFilterForm(NetBoxModelFilterSetForm):
    """Form for filtering SoftwareProduct instances."""

    model = SoftwareProduct

    q = forms.CharField(required=False, label="Search")

    name = forms.CharField(
        required=False,
        label="Name",
    )

    # tag = TagFilterField(SoftwareProduct)


class SoftwareProductCSVForm(NetBoxModelCSVForm):
    class Meta:
        model = SoftwareProduct
        fields = ("name",)


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

    # def clean(self):
    #     import pdb;pdb.set_trace()
    #     return super(SoftwareProductVersionForm, self).clean()


class SoftwareProductVersionFilterForm(NetBoxModelFilterSetForm):
    """Form for filtering SoftwareProductVersion instances."""

    model = SoftwareProductVersion

    q = forms.CharField(required=False, label="Search")

    name = forms.CharField(
        required=False,
        label="Name",
    )

    # tag = TagFilterField(SoftwareProduct)


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
        # initial_params={
        #     'device_types': 'device_type'
        # }
    )
    virtualmachine = DynamicModelChoiceField(
        queryset=VirtualMachine.objects.all(),
        required=False,
        # initial_params={
        #     'device_types': 'device_type'
        # }
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

    def clean(self):
        if not any([self.cleaned_data['device'], self.cleaned_data['virtualmachine']]):
            raise forms.ValidationError(_("Installation requires atleast one virtualmachine or device destination."))
        return super(SoftwareProductInstallationForm, self).clean()


class SoftwareProductInstallationFilterForm(NetBoxModelFilterSetForm):
    """Form for filtering SoftwareProductInstallation instances."""

    model = SoftwareProductInstallation

    q = forms.CharField(required=False, label="Search")

    # tag = TagFilterField(SoftwareProduct)


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
    # nullable_fields = ('',)